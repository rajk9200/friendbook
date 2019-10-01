path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static

from django.shortcuts import render
def index(request):
    return render(request,'index.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('accounts/', include('accounts.urls'))

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
