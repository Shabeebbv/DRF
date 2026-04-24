from django.shortcuts import render

# Create your views here.

# from .models import Student
# from django.http import JsonResponse
# import json
# from django.views.decorators.csrf import csrf_exempt


# @csrf_exempt
# def student_list(request):
#     if request.method=='GET':
#         students=Student.objects.all().values()

#         return JsonResponse (list(students),safe=False)
    
#     if request.method=='POST':
        
#         data=json.loads(request.body)

#         Student.objects.create(name=data.get('name'),
#                                age=data.get('age'),
#                                email=data.get('email')
#                                )
#         return JsonResponse({'message':'Student Added'})


# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from django.shortcuts import get_object_or_404

# @api_view(['GET','POST'])
# def student_list(request):
#     if request.method=='GET':
#         students=Student.objects.all().values()
#         return Response(students)
#     elif request.method=='POST':
        
#         data=request.data

#         Student.objects.create(
#             name=data.get('name'),
#             age=data.get('age'),
#             email=data.get('email')
#         )

#         return Response({'message':'Student Added'})
    

# @api_view(['GET','PUT','PATCH'])
# def student_detail(request,id):

#     student=get_object_or_404(Student,id=id)

#     if request.method=='GET':
#         data={
#             'id':student.id,
#             'name':student.name,
#             "age": student.age,
#             "email": student.email
#         }
#         return Response(data)


# from django.http import JsonResponse
# import json

# def student_list(request):
#     if request.method=='GET':
#         students=Student.objects.all().values()
#         return JsonResponse(list(students),safe=True)
    
#     elif request.method=='POST':
#         data=json.loads(request.body)

#         Student.objects.create(name=data.get('name'),
#                                age=data.get('age'),
#                                email=data.get('email'))
        
#         return JsonResponse({'message':'student added'})



# from rest_framework.decorators import api_view
# from rest_framework.response import Response

# @api_view(['GET','POST'])
# def stdlist(request):
#     if request.method=='GET':
#         students=Student.objects.all().values()
#         return Response(students)
#     elif request.method=='POST':
#         data=request.data
#         Student.objects.create(name=data.get('name'),
#                                age=data.get('age'),
#                                email=data.get('email'))
#         return Response({'message':'student added'})



# from rest_framework.views import APIView
# from rest_framework.response import Response
# from .serializer import StdSerializer
# from django.shortcuts import get_object_or_404
# from rest_framework.mixins import ListModelMixin

# class StudentApiView(APIView):
#     def get(self,request):

#         students=Student.objects.all()
#         serializer=StdSerializer(students,many=True)

#         return Response(serializer.data)
        # students=Student.objects.all()
        # data=[]
        # for i in students:
        #     data.append({
        #         'name':i.name,
        #         'age':i.age,
        #         'email':i.email
        #     })

        # return Response(data)

    # def post(self,request):
    #     serializer=StdSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'message':'user is created',
    #                          'data':serializer.data})
    #     return Response(serializer.errors)
        
    
    # def  put(self,request,pk):
    #     students=get_object_or_404(Student,pk=pk)
    #     serializer=StdSerializer(students,data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'message':'updated',
    #                      'data':serializer.data})
    #     return Response(serializer.errors)
    
    # def patch(self,request,pk):
    #     students=get_object_or_404(Student,pk=pk)
    #     serializer=StdSerializer(students,data=request.data,partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'message':'updated',
    #                         'data':serializer.data})
        
    # def delete(self,request,pk):
    #     students=get_object_or_404(Student,pk=pk)
    #     students.delete()

    #     return Response({'message':'Student deleted'})


# from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
# from .serializer import StdSerializer
# from rest_framework.generics import GenericAPIView

# class StudentList(GenericAPIView,ListModelMixin,CreateModelMixin):
#     queryset=Student.objects.all()
#     serializer_class=StdSerializer

#     def get(self,request):
#         return self.list(request)
#     def post(self,request):
#         return self.create(request)
    
# class StudentDtail(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
#     queryset=Student.objects.all()
#     serializer_class=StdSerializer
#     lookup_field='pk'

#     def delete(self,request,pk):
#         return self.delete(request,pk=pk)


# from rest_framework.views import APIView
# from .models import Student
# from rest_framework.response import Response
# from .serializer import StudentSerializer
# from rest_framework import status
# from django.shortcuts import get_object_or_404

# class StudentsView(APIView):
#     def get(self,requset):
#         students=Student.objects.all()
#         serializer=StudentSerializer(students,many=True)
#         return Response(serializer.data)
    
#     def post(self,request):
#         serializer=StudentSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)
    
# class StudentView(APIView):
#     def get(self,request,pk):
#         students=get_object_or_404(Student,pk=pk)
#         serializer=StudentSerializer(students)
#         return Response(serializer.data)
    
#     def put(self,request,pk):
#         student=get_object_or_404(Student,pk=pk)
#         serializer=StudentSerializer(student,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self,request,pk):
#         student=get_object_or_404(Student,pk=pk)
#         student.delete()
#         return Response({'message':'Delete'})


#     def patch(self,request,pk):
#         students=get_object_or_404(Student,pk=pk)
#         serializer=StudentSerializer(students,data=request.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
    
