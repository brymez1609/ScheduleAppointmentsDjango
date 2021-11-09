from django.shortcuts import redirect, render
from rest_framework.serializers import Serializer
from list_appointments.models import CustomSettings, RolesUser
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .serializers import CustomSettingsSerializer, HelloSerializer
from rest_framework.response import Response
# Create your views here.   

@login_required
def index(request):   
    return render(request, 'index.html',{})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)    
        if user:
            login(request, user)       
            return redirect('index')
        else:
            return render(request, 'login.html',{'error':'Username or password incorrect.'})
    return render(request, 'login.html',{})        

#@login_required
def list_patients(request):
    users = User.objects.all()
    roles_users  = RolesUser.objects.all()
    return render(request, 'list_appointments/list.html',{
            'roles_users':roles_users,
            'sections':CustomSettings.SECTIONS
        })
   

class ListUsersApiView(APIView):    

    def post(self, request):
        data = request.data
        data["id_provider"] = 1        
        serializer = CustomSettingsSerializer(data=data)
        if serializer.is_valid():            
            serializer.save()
        else:
            print(serializer.errors)                        
        return Response({'oket':'okey'})    