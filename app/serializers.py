from rest_framework import serializers
from .models import MainCategory 
from .models import SubCategory

class MainCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MainCategory
        fields = "__all__"


class SubCategorySerializer(serializers.ModelSerializer):
    subcategories=MainCategorySerializer()
    class Meta:
        model = SubCategory
        fields =[
             "name", 
             'slug',
             'ccategory_icon',
             'subcategories',
            
        ]       