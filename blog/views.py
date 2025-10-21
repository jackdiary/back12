
from .models import Post
from django.views.generic import ListView, DetailView

class PostList(ListView):
    model = Post
    ordering = '-pk'

class PostDetail(DetailView):
    model = Post






#  def index(request):
#     posts = Post.objects.all().order_by('-pk')
#     return render(
#         request,
#         'blog/index.html',
#         {
#             'posts': posts,
#         }
#     )

def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)
# Create your views here.
    return render(
        request,
        'blog/single_pages.html',
        {
            'post': post,
        }
    )
