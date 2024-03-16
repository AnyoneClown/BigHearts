from django.urls import path

from cabinet.views import PostView

urlpatterns = [
    path("posts/", PostView.as_view(), name="post-create"),
    path("posts/<int:pk>/", PostView.as_view(), name="post-detail"),
]

app_name = "cabinet"
