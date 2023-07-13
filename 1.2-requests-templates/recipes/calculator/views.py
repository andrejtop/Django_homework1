from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'blini': {
        'молоко, л': 0.5,
        'яйца, шт': 4,
        'мука, г': 0.170,
        'растительное масло, ст.л.': 1,
        'соль, ч.л.': 0.3,
        'сахар, г': 0.05,
    }
    # можете добавить свои рецепты ;)
}

def recipe_dict(request):
    recipes = list(DATA.keys())
    context = {
        'recipe': recipes
    }
    template = 'home.html'
    return render(request, template, context)

def recipes(request, recipe):
    try:
        recipe_list = {}
        servings = int(request.GET.get("servings", 1))
        for ingridient, amount in DATA[recipe].items():
            recipe_list[ingridient] = round(amount * servings, 2)
            print(ingridient, amount)
        context = {'recipe': recipe_list}
        return render(request, 'calculator/index.html', context)
    except Exception:
        print("What the fuck?")



# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
