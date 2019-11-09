from rest_framework  import serializers
from quoteapp.models import Quote, QuoteCategory

class QuoteSerializer(serializers.ModelSerializer):
	class Meta:
		model = Quote
		fields = ('__all__')

class QuoteCategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = QuoteCategory
		fields = ('__all__')
