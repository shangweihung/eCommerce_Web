from django.conf.urls import url
from .views import product_list, product_detail, register, log_in, log_out, story

app_name = 'shop'

urlpatterns = [
    url(r'^$', product_list, name='product_list'),  # $:End of string 
    url(r'^(?P<category_slug>[-\w]+)/$', product_list, name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', product_detail, name='product_detail'),
    url(r'^register$', register, name='register'),
    url(r'^logout$', log_out, name='logout'),
    url(r'^login$', log_in, name='login'),
    url(r'^story$', story, name='story')
]
