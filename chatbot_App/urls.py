from django.conf.urls import include, url
from .views import MyQuoteBotView
urlpatterns = [

			 url(r'^vatsal/?$', MyQuoteBotView.as_view())
	]