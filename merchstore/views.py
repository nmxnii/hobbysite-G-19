from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

from .models import Product, ProductType,transaction, Profile

from .forms import ProductForm,TransactionForm


class ProductListView(ListView): 
    model = ProductType
    template_name = "product_list.html"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        if self.request.session.get('transactionInfo'):
            del self.request.session['transactionInfo']
        context['owned_by_user']=ProductType.objects.all()
        return context


class ProductDetailView(DetailView): 
    model = Product
    template_name = "product_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        if(self.request.user.is_authenticated):
            initial_data = {'product': product, 'buyer':self.request.user.profile}
        initial_data = {'product': product}
        context['transaction_form'] = TransactionForm(initial=initial_data)
        return context

    def dispatch(self,request, *args, **kwargs):
        product=self.get_object()
        transactionInfo=request.session.get('transactionInfo')
        if transactionInfo:
            if self.request.user.profile==product.Owner:
                del request.session['transactionInfo']
                return redirect('merchstore:product_list')
            buyer=self.request.user.profile
            amount=transactionInfo['amount']
            form=TransactionForm()
            
            transaction=form.save(commit=False)
            transaction.product=product
            transaction.buyer=buyer
            transaction.amount=amount
            product.stock=product.stock-amount
            transaction.status="On Cart"
            transaction.save()
            product.save()
            del request.session['transactionInfo']
            return redirect('merchstore:product_cart_view')
        return super().dispatch(request,*args,**kwargs)

    def post(self, request, *args, **kwargs):
        self.object=self.get_object()
        product = self.object
        form = TransactionForm(request.POST)
        ctx=self.get_context_data(**kwargs)
        ctx["errors"]={}

        if form.is_valid():
            transaction = form.save(commit=False)
            amount=transaction.amount
            if (transaction.amount != None) and (transaction.amount != 0):
                if product.stock < transaction.amount:
                        ctx["errors"]["OverBuy"]= True
                        return render(request, self.template_name, context=ctx)
                if request.user.is_authenticated:
                    buyer=self.request.user.profile
                    transaction.product=product
                    transaction.buyer=buyer
                    transaction.amount=amount
                    transaction.status="On Cart"
                    product.stock=product.stock-transaction.amount
                    if product.stock == 0:
                        product.status = "Out of Stock"
                    
                    transaction.save()
                    product.save()
                    return redirect('merchstore:product_cart_view') 
                else:
                    request.session['transactionInfo']={
                        'amount':amount,
                    }
                    login_url=reverse('login')+'?next=' + request.get_full_path()
                    return redirect(login_url)
            ctx["errors"]["NoAmount"]= True
            return render(request, self.template_name, context=ctx)
        # return render(request, self.template_name, context=ctx)        


class TransactionListView(LoginRequiredMixin, ListView):
    model=transaction
    template_name = "product_transaction_list.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)        
        user=Profile.objects.get(user=self.request.user)
        buyer=Profile.objects.all()
        sellerItems=Product.objects.filter(Owner=user)
        product=transaction.objects.filter(product__in=sellerItems)
        totalProducts=0
        
        for total in product:
            if total.amount != None:
                totalProducts += total.amount
        context['itemsSold']=product
        context['buyerAll']=buyer
        context['total']=totalProducts
        return context

class CartView(LoginRequiredMixin, ListView):
    model=transaction
    template_name = "product_cart_view.html"


    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)        
        user=Profile.objects.get(user=self.request.user)
        product=transaction.objects.filter(buyer=user)
        seller=Profile.objects.all()
        totalProducts=0
        
        for total in product:
            if total.amount != None:
                totalProducts += total.amount
        context['itemsBought']=product
        context['sellerAll']=seller
        context['total']=totalProducts

        return context


class ProductCreateView(LoginRequiredMixin,CreateView):
    model=Product
    template_name="product_create.html"
    form_class=ProductForm
    
    def get_initial(self):
        initial = super().get_initial()
        initial['Owner']=self.request.user.profile
        return initial


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model=Product
    form_class=ProductForm
    template_name="product_update.html"

    def get_success_url(self):
        return reverse_lazy('merchstore:product_detail', kwargs={ 'pk': self.object.pk})
    
    def form_valid(self,form):
        product = form.save(commit=False)
        if product.stock == 0:
            product.status = "Out of Stock"
        else:
            product.status = "Available"
        product.save()
        form.instance.Owner=self.request.user.profile
        return super().form_valid(form)
                



