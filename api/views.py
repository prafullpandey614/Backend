# from datetime import datetime
import datetime
# from random import random
import random
from django.forms import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
import pytz
from api.models import NewUserOTP
from .serializers import UserSerializer
from .validators import validate_email_mobile
class Register(generics.CreateAPIView):
    serializer_class = UserSerializer
    
    def post(self,request,*args, **kwargs):
        
        
        if request.path=="/generateotp":
            #validating User Email Address
            try:
                validate_email_mobile(request.data['email_mobile'])
            except ValidationError as e:
                return Response(e,status=status.HTTP_400_BAD_REQUEST)
            #checking if Otp Exists
            try:
                NewUserOTP.objects.get(email_mobile = request.data['email_mobile']).delete()
            except:
                pass
            # otp = random.random.randint(1001,9999)
            otp = random.randint(1001,9999)
            NewUserOTP.objects.create(email_mobile = request.data['email_mobile'],otp = otp)
            return Response(otp,status = status.HTTP_201_CREATED)
        
        if request.path == '/register':
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                new_user_otp = get_object_or_404(NewUserOTP,email_mobile = request.data['email_mobile'])
                utc_curr = datetime.datetime.utcnow()
                utc_curr = utc_curr.replace(tzinfo=pytz.utc)
                if new_user_otp.created_on < utc_curr-datetime.timedelta(seconds=120):
                    new_user_otp.delete()
                    return Response({'error':'Otp Expired'},status = status.HTTP_400_BAD_REQUEST)
                if str(new_user_otp.otp)==request.data['otp']:
                    pass