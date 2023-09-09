import datetime
from tortoise import Tortoise, fields
from tortoise.models import Model
from tortoise.fields import ForeignKeyField


class User(Model):
    UserID = fields.IntField()
    UserName = fields.CharField(max_length=255)
    Balance = fields.FloatField()


class Product(Model):
    ProductID = fields.IntField()
    Type = fields.CharField(max_length=20)
    Format = fields.CharField(max_length=20)
    Country = fields.CharField(max_length=20)
    Price = fields.FloatField()
    StatusProduct = fields.CharField(max_length=20, choices=[('В наличии', 'В наличии'), ('Зарезервирован', 'Зарезервирован'), ('Продан', 'Продан')])
    AddTime = fields.DatetimeField(default=datetime.datetime.now)


class Order(Model):
    UserID = ForeignKeyField('models.User', related_name='orders')
    ProductCount = fields.IntField()
    TotalPrice = fields.FloatField()
    PaymentMethod = fields.CharField(max_length=50)
    Status = fields.CharField(max_length=20, choices=[('заказ оформлен', 'Заказ оформлен'), ('в процессе оплаты', 'В процессе оплаты'), ('заказ подтвержден', 'Заказ подтвержден')])
    TimeOrderStart = fields.DatetimeField(default=datetime.datetime.now)
    TimeOrderFinish = fields.DatetimeField(null=True)

    async def save(self, *args, **kwargs):
        if self.Status == 'заказ подтвержден' and not self.TimeOrderFinish:
            self.TimeOrderFinish = datetime.datetime.now()
        await super().save(*args, **kwargs)


class OrderProduct(Model):
    OrderID = ForeignKeyField('models.Order', related_name='OrderProducts')
    ProductID = ForeignKeyField('models.Product', related_name='OrderProducts')
    UserID = ForeignKeyField('models.User', related_name='OrderProducts')

    async def save(self, *args, **kwargs):
        await super().save(*args, **kwargs)
        product = await self.ProductID
        if product.StatusProduct == 'В наличии':
            product.StatusProduct = 'Зарезервирован'
            await product.save()


class Payment(Model):
    PaymentMethodName = fields.CharField(max_length=50)
    UserID = ForeignKeyField('models.User', related_name='payments')
    PaymentAmount = fields.FloatField()
    TimePayment = fields.DatetimeField(default=datetime.datetime.now)


async def init():
    await Tortoise.init(
        db_url='sqlite://market.db',
        modules={'models': ['__main__']},
    )
    await Tortoise.generate_schemas()

if __name__ == '__main__':
    from asyncio import run
    run(init())
