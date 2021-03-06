from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy

#def home(request):
    #return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post 
    template_name = 'home.html'
    ordering = ['-post_date']   # odwraca numeracje po dacie
    #ordering = ['-id']   # odwraca numeracje 

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__'
    #fields = ('title', 'body')  

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'   
    #fields = ['title', 'title_TAG' , 'body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html' 
    success_url = reverse_lazy('home')

class LogoutView(ListView):
    model = Post 
    template_name = 'logout.html'

class ProfilView(ListView):
    model = Post 
    template_name = 'profil.html'

class AddCategoryView(CreateView):
    model = Category
    #form_class = PostForm
    template_name = 'add_category.html'
    fields = '__all__'
    #fields = ('title', 'body')  

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats)
    return render(request, 'categories.html',{'cats' : cats.title(), 'category_posts' : category_posts })

class CatView(ListView):
    model = Category 
    template_name = 'cat.html'