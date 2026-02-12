from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from .forms import CustomUserCreationForm

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post

from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post

from .forms import CommentForm
from .models import Comment


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

    # Detail view for comments
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
#Add Comment
@login_required
def add_comment(request, pk):
   post = get_object_or_404(Post, pk=pk)

   if request.method == 'POST':
      form = CommentForm(request.POST)
      if form.is_valid():
         comment = form.save(commit=False)
         comment.post = post
         comment.author = request.user
         comment.save()

      return redirect('post-detail', pk=post.pk)     

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