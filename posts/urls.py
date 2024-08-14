from django.urls import path
from . import views
urlpatterns=[
    path('home/',views.home,name='home'),
    path('contact/',views.contact,name="contact"),
    path('skills/',views.skills,name="skills"),
    path('education/',views.education,name="education"),
    path('projects/',views.projects,name="projects"),
    path('resume/',views.resume,name="resume"),
    path('certificates_achievements/',views.certificates_achievements,name="certificates_achievements"),
    path('marksheet0/',views.ms0,name="ms0"),
    path('marksheet1/',views.ms1,name="ms1"),
    path('marksheet2/',views.ms2,name="ms2"),
    path('certificate1/',views.ms6,name="ms6"),
    path('certificate2/',views.ms7,name="ms7"),
    path('certificate3/',views.ms8,name="ms8"),
    path('certificate4/',views.ms9,name="ms9"),
    
]