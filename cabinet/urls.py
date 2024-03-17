from django.urls import path

from cabinet.views import PostView

urlpatterns = [
    path("cabinet/posts/", PostView.as_view(), name="post-create"),
    path("cabinet/posts/<int:pk>/", PostView.as_view(), name="post-detail"),
]

app_name = "cabinet"
