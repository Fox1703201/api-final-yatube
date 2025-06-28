from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedSimpleRouter

from .views import PostViewSet, CommentViewSet, GroupViewSet, FollowViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

router = DefaultRouter()
router.register("posts", PostViewSet, basename="posts")
router.register("groups", GroupViewSet, basename="groups")
router.register("follow", FollowViewSet, basename="follow")

posts_router = NestedSimpleRouter(router, "posts", lookup="post")
posts_router.register("comments", CommentViewSet, basename="post-comments")

urlpatterns = [
    path("v1/", include(router.urls)),
    path("v1/", include(posts_router.urls)),
    path(
        "v1/jwt/create/",
        TokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path("v1/jwt/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("v1/jwt/verify/", TokenVerifyView.as_view(), name="token_verify"),
]
