from django.http import JsonResponse
from .models import Category
from django.contrib.auth.hashers import make_password
from .models import User

def register(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = User(username=username, password=make_password(password))
    user.save()
    return JsonResponse({'message': 'User created successfully'}, status=201)

def get_categories(request):
    categories = Category.objects.all()
    data = []
    for category in categories:
        data.append({
            'id': category.id,
            'name': category.name,
            'description': category.description
        })
    return JsonResponse(data, safe=False)

def create_category(request):
    name = request.POST.get('name')
    description = request.POST.get('description')
    category = Category(name=name, description=description)
    category.save()
    return JsonResponse({'message': 'Category created successfully'}, status=201)

def update_category(request, id):
    category = Category.objects.get(id=id)
    name = request.POST.get('name')
    description = request.POST.get('description')
    category.name = name
    category.description = description
    category.save()
    return JsonResponse({'message': 'Category updated successfully'})

def delete_category(request, id):
    category = Category.objects.get(id=id)
    category.delete()
    return JsonResponse({'message': 'Category deleted successfully'})
