from django.conf import settings
from django.views.generic import TemplateView, RedirectView
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, password_change, password_change_done
from bombshellswim.shopper.views import set_value, customize, substep

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bombshellswim.views.home', name='home'),
    # url(r'^bombshellswim/', include('bombshellswim.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^$',               TemplateView.as_view(template_name='home.html')),
    url(r'^about-us',        TemplateView.as_view(template_name='about-us.html')),
    url(r'^how-it-works',    TemplateView.as_view(template_name='how-it-works.html')),
    url(r'^faqs',            TemplateView.as_view(template_name='faqs.html')),
    url(r'^admin/',          include(admin.site.urls)),

    # auth
    url(r'^login',               login, { 'template_name': 'login.html' }),
    url(r'^register',            TemplateView.as_view(template_name='register.html')),

    # password change
    url(r'^accounts/password/change/$',      password_change, { 'template_name': 'password_change.html' }, name='password-change'),
    url(r'^accounts/password/change/done/$', password_change_done, { 'template_name': 'password_change_done.html' }, name='password-change-done'),

    # password reset
	(r'^accounts/password/reset/$', 'django.contrib.auth.views.password_reset', {'post_reset_redirect' : '/accounts/password/reset/done/'} ),
	(r'^accounts/password/reset/done/$', 'django.contrib.auth.views.password_reset_done'),
	(r'^accounts/password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', {'post_reset_redirect' : '/accounts/password/done/'}),
	(r'^accounts/password/done/$', 'django.contrib.auth.views.password_reset_complete'),

    # shopping steps
    url(r'^shop/set_value',                             set_value),
    url(r'^shop/step/(?P<step>1|2|3)',                  customize),
    url(r'^shop/substep/(?P<substep>(1a|1b|2a|3a|3b))', substep),
    url(r'^shop',                                       RedirectView.as_view(url='/shop/step/1')),

)
