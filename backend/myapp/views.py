from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from .models import User

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def user_view(request, pk=None):
    if request.method == 'GET':
        if pk:
            try:
                user = User.objects.get(pk=pk)
                user_serializer = UserSerializer(user)
                return JsonResponse(user_serializer.data, safe=False)
            except User.DoesNotExist:
                return JsonResponse({"error": "User not found"}, status=404)
        else:
            users = User.objects.all()
            user_serializer = UserSerializer(users, many=True)
            return JsonResponse(user_serializer.data, safe=False, status=200)
    
    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        
        if user_serializer.is_valid():
            user_serializer.save()
            response_data = {
                "data": user_serializer.data
            }
            return JsonResponse(response_data, safe=False, status=201)
        
        # Extracting field errors and formatting the response
        errors = user_serializer.errors
        error_messages = {}
        for field, messages in errors.items():
            error_messages[field] = " ".join(messages)

        return JsonResponse({"error": error_messages}, safe=False, status=400)
    
    elif request.method == 'PUT':
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return JsonResponse({"error": "User not found"}, status=404)
        
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(user, data=user_data)
        
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data, safe=False, status=200)
        
        errors = user_serializer.errors
        error_messages = {}
        for field, messages in errors.items():
            error_messages[field] = " ".join(messages)
        
        return JsonResponse({"error": error_messages}, safe=False, status=400)
    
    elif request.method == 'DELETE':
        try:
            user = User.objects.get(pk=pk)
            user.delete()
            return JsonResponse({"message": "User deleted successfully"}, status=204)
        except User.DoesNotExist:
            return JsonResponse({"error": "User not found"}, status=404)

    return JsonResponse({"error": "Invalid request method"}, status=405)
