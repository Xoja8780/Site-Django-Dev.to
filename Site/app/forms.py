# Импортируем модуль forms из Django для создания HTML форм
from django import forms

# Создаём класс SearchForm, который наследуется от forms.Form
# Этот класс определяет структуру и валидацию формы поиска
class SearchForm(forms.Form):
    # Поле для ввода текста поиска
    # - max_length=100: ограничивает максимальную длину ввода до 100 символов
    # - required=False: поле не обязательно к заполнению (пользователь может отправить пустую форму)
    q = forms.CharField(
        max_length=100,
        required=False
    )