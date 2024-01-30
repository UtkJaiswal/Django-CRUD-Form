from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class CreateForm(APIView):
    def post(self,request):
        result={}
        result['status']="NOK"
        result['valid']=False
        result['result']={"message":"Unauthorized access","data":[]}

        if 'name' in request.data and 'email' in request.data:
            name = request.data['name']
            email = request.data['email']

            
            form_instance = Form.objects.create(name=name, email=email)

            result['status'] = "OK"
            result['valid'] = True
            result['result'] = {"message": "Form submitted successfully", "data": {
                
                'name': form_instance.name,
                'email': form_instance.email,
            }}

            return Response(result, status=status.HTTP_201_CREATED)
        return Response(result,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
class GetForm(APIView):
    def get(self, request):
        result = {}
        result['status'] = "NOK"
        result['valid'] = False
        result['result']={"message":"Unauthorized access","data":[]}

        try:

            data = Form.objects.all().values()
            result['status'] = "OK"
            result['valid'] = True
            result['result']['message'] = "Data fetched successfully"
            result['result']['data'] = data

            return Response(result,status=status.HTTP_200_OK)
        
        except Exception as e:
            result['error'] = str(e)
            return Response(result,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class UpdateForm(APIView):
    def put(self, request,pk):
        result = {}
        result['status'] = "NOK"
        result['valid'] = False
        result['result']={"message":"Unauthorized access","data":[]}

        try:
            form_instance = Form.objects.get(pk=pk)

            name = request.data['name']
            email = request.data['email']

            form_instance.name = name
            form_instance.email = email

            form_instance.save()

            data = {
                'name':name,
                'email':email
            }

            result = {
                'status': 'OK',
                'valid': True,
                'result': {'message': 'Data fetched successfully', 'data': data},
            }
            return Response(result, status=status.HTTP_200_OK)
        
        except Form.DoesNotExist:
            result = {
                'status': 'NOK',
                'valid': False,
                'result': {'message': 'Form not found', 'data': []},
            }
            return Response(result, status=status.HTTP_404_NOT_FOUND)
        
        except Exception as e:
            result = {
                'status': 'NOK',
                'valid': False,
                'result': {'message': str(e), 'data': []},
            }
            return Response(result, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class DeleteForm(APIView):
    def delete(self,request,pk):
        result = {}
        result['status'] = "NOK"
        result['valid'] = False
        result['result']={"message":"Unauthorized access","data":[]}

        try:
            form_instance = Form.objects.get(pk=pk)
            form_instance.delete()

            result = {
                'status': 'OK',
                'valid': True,
                'result': {'message': 'Form deleted successfully', 'data': []},
            }
            return Response(result, status=status.HTTP_204_NO_CONTENT)
        
        except Form.DoesNotExist:
            result = {
                'status': 'NOK',
                'valid': False,
                'result': {'message': 'Form not found', 'data': []},
            }
            return Response(result, status=status.HTTP_404_NOT_FOUND)
        
        except Exception as e:
            result = {
                'status': 'NOK',
                'valid': False,
                'result': {'message': str(e), 'data': []},
            }
            return Response(result, status=status.HTTP_500_INTERNAL_SERVER_ERROR)