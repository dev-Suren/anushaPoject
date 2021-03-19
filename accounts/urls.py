from django.urls import path

from. import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login', views.login, name='login'),
    path('landingpage', views.landingpage, name='landingpage'),
    path('logout', views.logout, name='logout'),
    path('seekerDashboard', views.seekerDashboard, name='seekerDashboard'),
    path('list_job/', views.list_job, name='list_job'),
    path('jobhome/', views.jobhome, name='jobhome'),
    path('delete_job/<int:id>', views.delete_job, name='delete_job'),

    path('savedJobs/', views.savedJobs, name='saved_jobs'),
    path('appliedJobs/', views.appliedJobs, name='appliedJobs'),
    path('save_job/<int:job_id>', views.save_job, name='save_job'),
    path('apply_job/<int:job_id>', views.apply_job, name='apply_job'),

    path('remove_job/<int:id>', views.remove_job, name='remove_job'),
    path('applicants/', views.applicants, name='applicants'),
    path('applicants/<int:job_id>', views.applicant, name='applicant'),

    path('profile/', views.profile, name='profile'),
    path('job_details/', views.job_details, name='job_details'),

    path('remove_applied_job/<int:id>', views.remove_applied_job, name='remove_applied_job'),

    path("search", views.search, name="search"),
    path('recruiter/',views.recruiter,name="recruiter")
]
