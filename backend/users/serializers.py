from rest_framework import serializers
from users.models import UserAccount

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['id', 'email', 'display_name', 'username']

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['display_name', 'username', 'email', 'password']
        extra_kwargs = {
            'password': {
                'style': {
                    'input_type': 'password',
                },

                'write_only': True
            }
        }
    
    def save(self, request):
        user = UserAccount(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            display_name=self.validated_data['display_name'],
        )

        password = self.validated_data['password']

        user.set_password(password)
        user.save()
        return user