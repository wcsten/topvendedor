from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, full_name, email, password=None):
        if not full_name:
            raise ValueError('O campo nome é obrigatório')
        if not email:
            raise ValueError('O campo email é obrigatório')

        user = self.model(
            email=self.normalize_email(email),
            full_name=full_name,
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, full_name, email, password):
        if not full_name:
            raise ValueError('O campo nome é obrigatório')
        if not email:
            raise ValueError('O campo email é obrigatório')
        if not password:
            raise ValueError('O campo senha é obrigatório')

        user = self.create_user(
            full_name=full_name,
            email=self.normalize_email(email),
            password=password
        )

        user.is_admin = True
        user.save(using=self._db)

        return user


class ActiveManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        return super(ActiveManager, self).get_queryset().filter(
            is_active=True)


class InactiveManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        return super(InactiveManager, self).get_queryset().filter(
            is_active=False)
