from .models import Team, Employee
from django.contrib.auth import get_user_model


def populate():
    User = get_user_model()

    # for data in books_data:
    #     book = Book(**data)
    #     book.save()
    #     print(f'Добавлена предмет: {item}')


# Вызываем функцию для заполнения модели данными
# populate()
