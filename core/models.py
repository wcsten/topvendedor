from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from core.managers import UserManager, ActiveManager, InactiveManager


class DateMixin(models.Model):
    date_added = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Data de criação'
    )
    last_changed = models.DateTimeField(
        auto_now=True,
        verbose_name='Ultima modificação'
    )

    class Meta:
        abstract = True


class User(DateMixin, AbstractBaseUser):
    full_name = models.CharField('Nome completo', max_length=100, default='')
    email = models.EmailField(max_length=100, unique=True, default='')

    is_active = models.BooleanField(default=True, verbose_name='É ativo')
    is_admin = models.BooleanField(default=False, verbose_name='É admin')

    objects = UserManager()
    active = ActiveManager()
    inactive = InactiveManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.full_name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    def __str__(self):
        return self.full_name


class Customer(DateMixin, models.Model):
    full_name = models.CharField('Nome completo', max_length=150, default='')
    prefered_name = models.CharField(
        'Apelido',
        max_length=150,
        null=True,
        blank=True,
        default='',
    )
    email = models.EmailField(
        'E-mail',
        max_length=150,
        unique=True,
        default=''
    )
    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    balance = models.DecimalField(
        'Saldo em conta',
        max_digits=11,
        decimal_places=2,
        default=0,
    )

    objects = models.Manager()
    active = ActiveManager()
    inactive = InactiveManager()

    @property
    def update_balance(self, value=0):
        self.balance = self.balance + value
        self.save()

    class Meta:
        verbose_name = 'Jogadore'
        verbose_name_plural = 'Jogadores'

    def __str__(self):
        return self.full_name


class PlayerSale(DateMixin, models.Model):
    TRANSACTION_TYPE = (
        ('C', 'Crédito'),
        ('D', 'Débito'),
    )
    customer = models.ForeignKey(
        Customer,
        verbose_name='Jogadores',
        related_name='player_list',
    )
    kind = models.CharField(
        'Tipo de transação',
        choices=TRANSACTION_TYPE,
        max_length=1,
        default='C',
    )
    value = models.DecimalField(
        'Valor',
        max_digits=11,
        decimal_places=2
    )

    class Meta:
        verbose_name = 'Extrato'
        verbose_name_plural = 'Extratos'

    def __str__(self):
        return '{}'.format(self.value)
