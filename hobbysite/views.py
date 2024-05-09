from django.shortcuts import render
from django.http import HttpResponseRedirect
from user_management.models import Profile
from django.urls import reverse

from merchstore.models import Transaction, Product
from wiki.models import Article
from blog.models import Article as BlogArticle
from commissions.models import Commission

def home(request):
    return render(request, "home.html")

def dashboard(request):
    user = request.user.profile
    products_bought = Transaction.objects.filter(buyer=user, product__status='Delivered')
    products_sold = Product.objects.filter(Owner=user, product__status='On Cart')
    wiki_articles_created = Article.objects.filter(author=user)
    blog_articles_created = BlogArticle.objects.filter(author=user)
    commissions_created = Commission.objects.filter(author=user)
    commissions_joined = Commission.objects.filter(
        jobs__applicants__applicant=user,
          ).distinct()


    products_bought = [transaction_obj.product for transaction_obj in products_bought]

    context = {
        'products_bought': products_bought,
        'products_sold': products_sold,
        'wiki_articles_created': wiki_articles_created,
        'blog_articles_created': blog_articles_created,
        'commissions_created': commissions_created,
        'commissions_joined': commissions_joined,
    }

    return render (request, 'dashboard_view.html', context)
