from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_views

from django.views.decorators.csrf import csrf_protect

app_name = 'account'

urlpatterns = [
    #...

 	path('signup/', views.SignUp.as_view(), name='signup'),
	path('password_reset/',auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'),name='password_reset'),
	path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),name='password_reset_done'),
	path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
		name='password_reset_confirm'),
	path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),name='password_reset_complete'),
	path('password_change', auth_views.PasswordChangeView.as_view(template_name='registration/password_change_form.html'), name='password_change'),
	path('password_change/done', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'),name='password_change_done'),
	path('login/', csrf_protect(views.LoginView.as_view()), name='login'),
	path('logout/', views.LogoutView.as_view(), name='logout'),
	#path('profile_student/<str:username>/', views.profile_student, name='profile_student'),
	path('profile_student/<str:username>/', views.StudentProfileView.as_view(), name='profile_student'),
	#path('profile_blogger/<str:username>/', views.profile_blogger, name='profile_blogger'),
	path('profile_blogger/<str:username>/', views.BloggerProfileView.as_view(), name='profile_blogger'),
	
	#path('profile_blogger/<str:username>/', views.ProfileBloggerView.as_view(), name='profile_blogger'),
	path('home/',views.home, name='home'),
]