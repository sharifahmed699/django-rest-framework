from django.shortcuts import render
from rest_framework import generics
from quoteapp.models import Quote, QuoteCategory
from api.serializers import QuoteSerializer, QuoteCategorySerializer
# Create your views here.

class QuoteAPIView(generics.ListAPIView):
	queryset = Quote.objects.all()
	serializer_class = QuoteSerializer

class QuoteCategoryAPIView(generics.ListAPIView):
	queryset = QuoteCategory.objects.all()
	serializer_class = QuoteCategorySerializer

class QuoteAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Quote.objects.all()
	serializer_class = QuoteSerializer

class QuoteAPINewView(generics.ListCreateAPIView):
	queryset = Quote.objects.all().order_by('-id')[:1]
	serializer_class = QuoteSerializer

