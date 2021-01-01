
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from courses.views import CourseListView

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.sitemaps.views import sitemap
from courses.sitemaps import CourseSitemap



sitemaps = {
    'courses': CourseSitemap,
    }

urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(),name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(),name='logout'),
    # change password urls
    path('accounts/password_change/',auth_views.PasswordChangeView.as_view(template_name='students/student/password_change_form.html'),name='password_change'),
    path('accounts/password_change/done/',auth_views.PasswordChangeDoneView.as_view(template_name='students/student/password_change_done.html'),name='password_change_done'),
    # reset password urls
    path('accounts/password_reset/',auth_views.PasswordResetView.as_view(template_name='students/student/password_reset_form.html' ),name='password_reset'),
    path('accounts/password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='students/student/password_reset_done.html' ),name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='students/student/password_reset_confirm.html'),name='password_reset_confirm'),
    path('accounts/reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='students/student/password_reset_complete.html'),name='password_reset_complete'),
    path('accounts/', include('django.contrib.auth.urls')),
    
    path('admin/', admin.site.urls,name='taha'),
    path('course/', include('courses.urls')),
    path('students/', include('students.urls')),
    path('', CourseListView.as_view(), name='course_list'),
    path('api/', include('courses.api.urls', namespace='api')),
    #path('chat/', include('chat.urls', namespace='chat')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
                name='django.contrib.sitemaps.views.sitemap'),
  
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)