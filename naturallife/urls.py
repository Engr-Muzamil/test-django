from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('courses/', include('courses.urls')),
    path('accounts/', include('accounts.urls')),   # ✅ FIXED
    path('accounts/', include('django.contrib.auth.urls')),
    path('posts/', include('posts.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# project urls.py

from rest_framework.routers import DefaultRouter
from posts.api_views import PostViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns += router.urls