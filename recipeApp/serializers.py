from rest_framework import serializers
from .import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.User
        fields= '__all__'
        
        
class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.Ingredients
        fields= '__all__'
        
class RecipeSerializer(serializers.ModelSerializer):
    ingredient= serializers.MultipleChoiceField()
    class Meta:
        model= models.Recipe
        fields= ['name', 'ingredients', 'description', 'user']
        
    