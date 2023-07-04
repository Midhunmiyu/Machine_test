
from django.urls import path
from django.contrib.auth import views as auth_views
from polls import views

urlpatterns = [


    path('', views.login_view,name ='login_view'),
    path('logout_view', views.logout_view,name ='logout_view'),

    #admin urls

    path('admindashboard', views.admindashboard,name ='admindashboard'),
    path('add_course', views.add_course, name='add_course'),
    path('view_course', views.view_course, name='view_course'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),

    #customer urls

    path('customer_registration', views.customer_registration,name ='customer_registration'),
    path('customer_dashboard', views.customer_dashboard,name ='customer_dashboard'),
    path('cust_view_course', views.cust_view_course,name ='cust_view_course'),
    path('change-password/',auth_views.PasswordChangeView.as_view(template_name='changepassword.html',success_url = '/passwordchangedone/'),name='change_password'),
    path('passwordchangedone/',auth_views.PasswordChangeView.as_view(template_name='passwordchangedone.html'),name='passwordchangedone'),
]
