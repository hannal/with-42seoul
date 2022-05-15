import factory
from django.contrib.auth.models import User as UserModel


default_password = 'password'


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserModel

    username = factory.Sequence(lambda n: f'user_{n}')

    @factory.post_generation
    def password(self, create, extracted, **kwargs):
        if extracted:
            self.set_password(extracted)
        else:
            self.set_password(default_password)
