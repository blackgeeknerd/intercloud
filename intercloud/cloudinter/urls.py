from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('list/<int:pk>/', views.student_detail, name='student_detail'),
    path('list', views.student_interview, name='student_interview'),
    path('list', views.student_list, name='student_list'),
    path('approve', views.student_approve, name='student_approve'),
    path('new', views.new_interview, name='new_interview'),
    path('inview', views.inview, name='inview'),
    path('export/csv/', views.export_users_csv, name='export_users_csv'),
    path('list/<int:pk>/comment/', views.add_comment_to_student, name='add_comment_to_student'),
]
