import datetime

from peewee import *

db = SqliteDatabase('market.db')


class BaseModel(Model):
    id = PrimaryKeyField(unique=True)

    class Meta:
        database = db


class User(BaseModel):
    class Meta:
        db_table = 'Users'
    UserID = IntegerField()
    UserName = CharField(max_length=255)
    Balance = FloatField()


class Product(BaseModel):
    class Meta:
        db_table = 'Products'

    STATUS_PRODUCT = [
        ('В наличии', 'В наличии'),
        ('Зарезервирован', 'Зарезервирован'),
        ('Продан', 'Продан'),
    ]
    ProductID = IntegerField()
    Type = CharField(max_length=20)
    Format = CharField(max_length=20)
    Country = CharField(max_length=20)
    Price = FloatField()
    StatusProduct = CharField(max_length=20)
    AddTime = DateTimeField(default=datetime.datetime.now)


class Order(BaseModel):

    class Meta:
        db_table = 'Orders'

    STATUS_CHOICES = [
        ('заказ оформлен', 'Заказ оформлен'),
        ('в процессе оплаты', 'В процессе оплаты'),
        ('заказ подтвержден', 'Заказ подтвержден'),
    ]
    UserID = ForeignKeyField(User, to_field='UserID', backref='orders')
    ProductCount = IntegerField()
    TotalPrice = FloatField()
    PaymentMethod = CharField(max_length=50)
    Status = CharField(max_length=20)
    TimeOrderStart = DateTimeField(default=datetime.datetime.now)
    TimeOrderFinish = DateTimeField(null=True)

    def save(self, *args, **kwargs):
        if self.Status == 'заказ подтвержден' and not self.TimeOrderFinish:
            self.TimeOrderFinish = datetime.datetime.now()
        super().save(*args, **kwargs)


class OrderProduct(BaseModel):
    class Meta:
        db_table = 'OrderProducts'
    OrderID = ForeignKeyField(Order, backref='OrderProducts')
    ProductID = ForeignKeyField(Product, to_field='ProductID', backref='OrderProducts')
    UserID = ForeignKeyField(User, to_field='UserID', backref='OrderProducts')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        product = self.ProductID
        if product.StatusProduct == 'В наличии':
            product.StatusProduct = 'Зарезервирован'
            product.save()


class Payment(BaseModel):
    class Meta:
        db_table = 'Payments'
    PaymentMethodName = CharField(max_length=50)
    UserID = ForeignKeyField(User, to_field='UserID', backref='payments')
    PaymentAmount = FloatField()
    TimePayment = DateTimeField(default=datetime.datetime.now)


if __name__ == '__main__':
    db.create_tables([User, Product, Order, OrderProduct, Payment])
