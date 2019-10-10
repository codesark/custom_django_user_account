from django.contrib import admin
from django.urls import include, path
from .views import homeView

urlpatterns = [
    path('', homeView, name="home"),
    path('admin/', admin.site.urls),
    path('account/', include('accounts.urls'), name="account"),
]
