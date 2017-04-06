from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^about/$', views.about, name='about'),
	#url(r'^accounts/logout/$', logout, {'next_page': '/'}),
	#url('^accounts/', include('django.contrib.auth.urls'), name='login'),
 	#url(r'^accounts/', allauth.urls),
    #Admin Urls
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    #url(r'^admin/', include(admin.site.urls), {'next_page': '/'}),
	
    #url(r'^accounts/', include('allauth.urls')),
]
#Urlpatterns = [
#    url(r'^$', views.post_list, name='post_list'),
#]