from django.urls import path, include
from django.contrib import admin

# for serving static files
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    path('', include('course.urls')),
    # path('api/', include('course.api_urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

