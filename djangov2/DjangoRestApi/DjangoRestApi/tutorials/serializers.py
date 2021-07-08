from django.db.models.fields import EmailField
from rest_framework import serializers 
#from tutorials.models import Tutorial
from .models import Tutorial
from django.contrib.auth.models import User


from django.contrib.auth import password_validation, authenticate
from rest_framework.authtoken.models import Token
#from .models import User

#to model tutorial 
class TutorialSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Tutorial
        fields = ('id',
                  'title',
                  'description',
                  'published')


#to USer register
class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def create(self, validate_data):
        instance = User()
        instance.username = validate_data.get('username')
        instance.email = validate_data.get('email')
        instance.set_password(validate_data.get('password'))
        instance.save()
        return instance

    def validate_username(self, data):
        users = User.objects.filter(username = data)
        if len(users) != 0:
            raise serializers.ValidationError("this user already exists")
        else:
            return data


class UserModelSerializer(serializers.ModelSerializer):

    class Meta:

        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
        )
"""
class UserLoginSerializer(serializers.Serializer):

    # Campos que vamos a requerir
    #email = serializers.EmailField()
    username = serializers.CharField()
    password = serializers.CharField(min_length=8, max_length=64)

    # Primero validamos los datos
    def validate(self, data):

        # authenticate recibe las credenciales, si son válidas devuelve el objeto del usuario
        #user = authenticate(username=data['email'], password=data['password'])
        user = authenticate(username=data['username'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Las credenciales no son válidas')

        # Guardamos el usuario en el contexto para posteriormente en create recuperar el token
        self.context['username'] = user
        return data

    def create(self, data):
        #Generar o recuperar token.
        token, created = Token.objects.get_or_create(user=self.context['username'])
        return self.context['username'], token.key





"""
class UserLoginSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = User
        fields = ('username',
                  'password')

""""
class UserLoginSerializer2(serializers.Serializer):
    username = serializers.CharField()
    #password = serializers.CharField()

    def validate_username(self, data):
        users = User.objects.filter(username = data)
        if len(users) == 1:
            return users[0]
        else:
            raise serializers.ValidationError("User Invalid")
            
    def validate_password(self, data):
        users = User.objects.filter(password = data)
        if len(users) == 1:
            return data
        else:
            raise serializers.ValidationError("Pass Invalid")
"""
