from djoser.serializers import UserCreateSerializer as BaseUserSerializer, UserSerializer as BaseUserSerializer


class UserCreateSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'username', 'password',
                  'email', 'first_name', 'last_name']


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
