from rest_framework import serializers

from auth_app.models import User, Contributor
from business_logic.system_users._user import User as UserFacade
from core.mixins.serializer_mixins import ModelSerializer
from .user_serializers import UserSerializer
from business_logic.system_users import Contributor as UserFacade

class CreateContributorSerializer(ModelSerializer):
    email = serializers.EmailField(
        max_length=254, 
        min_length=5,
        required=True,
        write_only=True,
        )
    password = serializers.CharField(
        max_length=254,
        min_length=6,
        required=True,
        write_only=True,
        help_text='Required',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
    data = serializers.DictField(
        required=False,
        read_only=True,
        )

    class Meta:
        model = User
        fields = ['email', 'password']
        #fields = ['email', 'password','data']

    def create(self, validated_data):
        _request = self.context['request']
        request = {'request':_request, 'validated_data':validated_data}
        return UserFacade().register_contributor(request)


class ContributorSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Contributor
        exclude = ['registered_by','lastupdated_by']
        depth = 2


class ContributorLoginSerializer(ModelSerializer):
    email = serializers.EmailField(max_length=254, min_length=5)
    password = serializers.CharField(
        max_length=254,
        min_length=6,
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    class Meta:
        model = User
        fields = ['email', 'password']

    def validate(self, attrs):
        login_data = attrs
        return UserFacade().login(login_data)
