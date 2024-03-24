from django.urls import path

from cabinet.views import PostView, AdminView, UserPost, FilterPosts, SearchPosts, GetPostByUrl

urlpatterns = [
    path("cabinet/posts/", PostView.as_view(http_method_names=["post"]), name="post-create"),
    path("cabinet/user-posts/", UserPost.as_view(http_method_names=["get"]), name="user-posts-list"),
    path("cabinet/posts/<int:pk>/", PostView.as_view(), name="post-detail"),
    path("admin/", AdminView.as_view(http_method_names=["get"]), name="admin-list"),
    path("filter-posts/", FilterPosts.as_view(), name="filter-posts"),
    path("search/", SearchPosts.as_view(), name="search-posts"),
    path("url/", GetPostByUrl.as_view(), name="url-posts"),
]

app_name = "cabinet"
