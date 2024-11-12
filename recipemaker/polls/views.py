from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from polls.models import Recipe
import random 
from django.template import loader
from django.views.decorators.csrf import csrf_protect, csrf_exempt
import json
from typing import Any

# Create your views here.
# @csrf_protect
def get_recipe_for_today(request):
    recipes = Recipe.objects.all()
    if len(recipes) < 1: 
        return render(request, "polls/insert_meal.html", {})

    context = {
        "todays_meal": recipes[random.randint(0,len(recipes)-1)].name
    }
    return render(request, "polls/insert_meal.html", context)

@csrf_exempt
# TODO: figure out tokens
def insert_recipe(request: HttpRequest):
    params = body_to_dict(request.body)
    
    recipe_name = params["recipe_name"].replace("+", " ")
    
    # TODO: have some sort of message for this case
    if len(Recipe.objects.filter(name=recipe_name)) != 0: 
        return render(request, "polls/insert_meal.html", {})
    
    
    recipe = Recipe(name=recipe_name)
    recipe.save()
    print(recipe.name)
    context = {
        "new_recipe": recipe.name,
    }
    return render(request, "polls/insert_meal.html", context)
    
def body_to_dict(body): 
    params_list: list = []
    
    for info in body.decode().split("="): 
        params_list += info.split("&")
        
    params_dict: dict[str, Any] = {}
    for i in range(0, len(params_list), 2):
        params_dict[params_list[i]] = params_list[i+1]
        
    return params_dict
        
    
    
    