from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from resumesite import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('resumesite.urls')),
    path('signin/', views.signin, name="signin"),
    path('signup/', views.signup, name="signup"),
    path('signout', views.signout, name="signout"),
    path('homepage/', views.homepage, name="homepage"),
    # path('signout', views.signout, name="signout"),
]