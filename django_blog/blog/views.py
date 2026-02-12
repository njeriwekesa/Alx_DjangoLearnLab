from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Post, Comment
from .forms import CustomUserCreationForm, CommentForm

def home(request):
  return render(request, "blog/home.html")


def register(request):
  if request.method == "POST":
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user) #auto login after registration
      return redirect("home")
    
  else:
    form = CustomUserCreationForm()  

  return render(request, "blog/register.html", {"form": form})  

@login_required
def profile(request):
  if request.method == "POST":
    request.user.email = request.POST.get("email")
    request.user.save()
    return redirect("profile")
  
  return render(request, "blog/profile.html")


#CRUD operations for Post
# List all posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-published_date']

# Detail view of a single post
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context
        

# Create new post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# Update post (only author)
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

# Delete post (only author)
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
# CRUD operations for Comments
# Create Comment
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        post = get_object_or_404(Post, pk=self.kwargs['post_id'])
        form.instance.author = self.request.user
        form.instance.post = post
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.object.post.pk})     

# Update Comment
class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
   model = Comment
   fields = ['content']

   def test_func(self):
      comment = self.get_object()
      return self.request.user == comment.author
   
# Delete Comment
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
   model = Comment

   def get_success_url(self):
      return self.object.post.get_absolute_url()

   def test_func(self):
      comment = self.get_object()
      return self.request.user == comment.author 