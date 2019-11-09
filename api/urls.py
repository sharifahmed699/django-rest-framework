from django.urls import path
from api.views import QuoteAPIView, QuoteCategoryAPIView, QuoteAPIDetailView, QuoteAPINewView

urlpatterns = [
	path('', QuoteCategoryAPIView.as_view()),
	path('quotes/', QuoteAPIView.as_view()),
	path('quotes/<int:pk>/', QuoteAPIDetailView.as_view()),
	path('quotes/new/', QuoteAPINewView.as_view())
]
