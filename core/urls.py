from django.conf.urls import include, url
from django.views import generic
from . import views
from dal import autocomplete
from .models import CategoryExpense, CategoryExpenseForm


urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^teste/$', views.UpdateView.as_view(), name='teste'),
	url(r'^about/$', views.about, name='about'),
	url(r'^test-autocomplete/$', views.UpdateCategoryView.as_view(create_field='name', model=CategoryExpense), name='select2_fk'),
		#autocomplete.Select2QuerySetView.as_view(create_field='name', model=CategoryExpense), name='select2_fk'),
	url(
        'test/(?P<pk>\d+)/$',
        views.UpdateView.as_view(
            model=CategoryExpense,
            form_class=CategoryExpenseForm,
        )
    ),
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