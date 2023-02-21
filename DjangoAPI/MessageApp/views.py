from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view

from MessageApp.models import Messages,Profiles
from MessageApp.serializers import MessageSerializers,ProfileSerializers

# Create your views here.pip install django==<versionnumber>
@csrf_exempt
def messageApi(request):
    if request.method=='GET':
        messages=Messages.objects.all()
        messages_serializer=MessageSerializers(messages,many=True)
        return JsonResponse(messages_serializer.data,safe=False)
    
    elif request.method=='POST':
        message_data=JSONParser().parse(request)
        messages_serializer=MessageSerializers(data=message_data)
        if messages_serializer.is_valid():
            messages_serializer.save()
            return JsonResponse(messages_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(messages_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
           
    
    elif request.method=='PUT':
        message_data=JSONParser().parse(request)
        message=Messages.objects.get(MessageId=message_data['MessageId'])
        messages_serializer=MessageSerializers(message,data=message_data)
        if messages_serializer.is_valid():
            messages_serializer.save()
            return JsonResponse("Updated successfully",safe=False)
        return JsonResponse("Failed to Update")

    elif request.method=='DELETE':
        count=Messages.objects.all().delete()
        return JsonResponse({'message': '{} Messages were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

#elif request.method=='DELETE':
        #message=Messages.objects.get(MessageId=id)
        #message.delete()
        #return JsonResponse("Deleted Successfully",safe=False)

@api_view(['GET', 'PUT', 'DELETE'])
def message_detail(request, pk):
    try: 
        m = Messages.objects.get(pk=pk) 
    except Messages.DoesNotExist: 
        return JsonResponse({'message': 'The message does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        message_serializer = MessageSerializers(m) 
        return JsonResponse(message_serializer.data) 
 
    elif request.method == 'PUT': 
        message_data = JSONParser().parse(request) 
        message_serializer = MessageSerializers(m, data=message_data) 
        if message_serializer.is_valid(): 
            message_serializer.save() 
            return JsonResponse(message_serializer.data) 
        return JsonResponse(message_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        m.delete() 
        return JsonResponse({'message': 'Messagewas deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
# @api_view(['GET'])
# def tutorial_list_published(request):
#     tutorials = Tutorial.objects.filter(published=True)
        
#     if request.method == 'GET': 
#         tutorials_serializer = TutorialSerializer(tutorials, many=True)
#         return JsonResponse(tutorials_serializer.data, safe=False)

    
        