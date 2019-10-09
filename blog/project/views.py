from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin 
from .models import Post
from django.views.generic import (ListView,
    DetailView,
    CreateView,
    UpdateView, 
    DeleteView
)


# Create your views here.

context = {
    'posts': Post.objects.all()
}
def home(request):
    return render(request, 'project/home.html', context)




class PostListView(ListView):
    model = Post
    template_name = 'project/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted'] #posts to be rendered from latest to oldest(adding the minus sign helps in this )


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin,CreateView): 
    #for the loginrequiredmixin one has to log in first before he or she is able to create a post
    #one is redirected to the login page
    model = Post
    fields = ['title', 'content']


    def form_valid(self, form):
        form.instance.Personel = self.request.user # sets the form instance to the personel who is currently logged in
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView): 
    model = Post
    fields = ['title', 'content']


    def form_valid(self, form):
        form.instance.Personel = self.request.user 
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()  #it gets the post that we are currently trying to update
        if self.request.user == post.Personel:  # checks the current logged in user and checks if he/she owns the post trying to be edited
            return True 
        return False


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    def test_func(self):
        post = self.get_object()  #it gets the post that we are currently trying to update
        if self.request.user == post.Personel:  # checks the current logged in user and checks if he/she owns the post trying to be edited
          return True 
        return False


def about(request):
    return render(request, 'project/about.html', {'title': 'About'})

