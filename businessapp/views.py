from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Business
from .forms import BusinessForm
from django.shortcuts import get_object_or_404

def index(request):
    return render(request, 'businessapp/index.html')

@csrf_exempt
def perform_operation(request, operation, pk=None):

    if operation == 'create' and request.method == 'POST':
        form = BusinessForm(request.POST)
        if form.is_valid():
            business = form.save()
            return JsonResponse({'id': business.id, 'name': business.name, 'address': business.address, 'owner_info': business.owner_info, 'employee_size': business.employee_size})
        else:
            return JsonResponse({'error': 'Form data is not valid'}, status=400)
        
    if operation == 'update' and request.method == 'POST':

        try:
            business = Business.objects.get(id=pk)
            form = BusinessForm(request.POST, instance=business)
            if form.is_valid():
                form.save()
                return JsonResponse({'message': 'Business updated successfully!'})
            else:
                return JsonResponse({'error': 'Form data is not valid'}, status=400)
        except Business.DoesNotExist:
            return JsonResponse({'error': 'Business does not exist'}, status=404)
        
    elif operation == 'get_business' and request.method == 'GET':
        print("here11")
        business = Business.objects.get(id=pk)
        return JsonResponse({'business': {
            'id': business.id,
            'name': business.name,
            'address': business.address,
            'owner_info': business.owner_info,
            'employee_size': business.employee_size
        }})
        
    elif operation == 'delete' and request.method == 'POST':
        business = get_object_or_404(Business, pk=pk)
        business.delete()
        return JsonResponse({'message': 'Business deleted successfully'})
    
    elif operation == 'list':
        businesses = list(Business.objects.values())
        return JsonResponse({'businesses': businesses})
    
    elif operation == 'search' and request.method == 'GET':
        query = request.GET.get('query', '')
        businesses = Business.objects.filter(name__icontains=query).values()
        return JsonResponse({'businesses': list(businesses)})

