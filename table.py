from tortoise import Tortoise

from models import User


async def add_records():
    # Инициализация базы данных
    await Tortoise.init(
        db_url='sqlite://db.market.db',
        modules={'models': ['models']}  # Укажите правильное имя модуля
    )
    await Tortoise.generate_schemas()

    # Остальной код для добавления записей оставьте без изменений


    # Создание и сохранение записей в таблице User
    user1 = User(UserID=1, UserName='User1', Balance=100.0)
    await user1.save()

    user2 = User(UserID=2, UserName='User2', Balance=200.0)
    await user2.save()

    # Создание и сохранение записей в других таблицах
    # ... (повторите аналогичные шаги для других таблиц)

if __name__ == "__main__":
    import asyncio
    asyncio.run(add_records())
