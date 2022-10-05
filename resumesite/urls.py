from django.urls import path
#from  . import views
from resumesite import views


urlpatterns = [
    path('resume/', views.home, name="home"),
    path('',views.info,name="info"),
    path('download/', views.download_file, name="download_file"),

    # path('downloadpdf/',views.download_pdf_file,name="download_pdf_file"),
    # path('downloadpdf//', views.download_pdf_file, name="download_pdf_file"),
 # path('download/',views.download,name="download")
]