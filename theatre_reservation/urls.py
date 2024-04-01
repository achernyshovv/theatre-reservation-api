from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

urlpatterns = [
    path("api/theatre/", include("theatre.urls", namespace="theatre")),
    path("api/user/", include("user.urls", namespace="user")),
    path("admin/", admin.site.urls),
    path("api/cinema/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/cinema/doc/swagger/", SpectacularSwaggerView.as_view(url_name="schema"),
         name="swagger-ui"),
    path(
        "api/cinema/doc/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]
