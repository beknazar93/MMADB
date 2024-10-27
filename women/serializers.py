
from rest_framework import serializers

from .models import Women


class WomenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Women
        fields = ('title','second_name','cat_id','content',)