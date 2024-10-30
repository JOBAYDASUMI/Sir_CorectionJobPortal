from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from myProject.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path('signupPage/',signupPage,name='signupPage'),
    path('', signInPage, name='signInPage'),
    path("homePage/", homePage, name='homePage'),
    path("logoutPage/", logoutPage, name='logoutPage'),
    path("ProfilePage/", profilePage, name='profilePage'),

    path('addJob/', addJob, name='addJob'),
    path('createdJob/', createdJob, name="createdJob"),
    path('jobFeed/', jobFeed, name='jobFeed'),
    path('searchJob/',searchJob, name='searchJob'),
    
    
    
    path('applyJob/<str:id>', applyJob, name='applyJob'),
    path('editJob/<str:id>', editJob, name='editJob'),
    path('viewJob/<str:id>', viewJob, name='viewJob'),
    path('deleteJob/<str:id>', deleteJob, name='deleteJob'),
    
    path('skillMatching/',skillMatching, name='skillMatching'),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
