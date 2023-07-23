valid_email = "mak.st0@ya.ru"
valid_pass = "Qwe123rty567"

invalid_email = 'mak@ya.ru'
invalid_pass = 'Aa1234'

name = 'Иван'
surname = 'Иванов'
region = 'Москва г'
email = 'mak.st0@ya.ru'
password = 'Qwe123rty567'

false_email = '123456'
false_mobile_max = '891234567890'
false_mobile_mini = '9123456789'
false_name_mini = 'А'
name_two_letters = "Як"
thirty_letters = 'Оченьдлинноеимямоеатакжефамили'
thirty_one_letters = 'Оченьдлинноеимямоеатакжефамилия'

class TestData:
    BASE_URL = 'https://b2c.passport.rt.ru/'

    #Заголовки названий элементов
    FORM_AUTH_MAIL = 'Почта'
    AUTH = 'Авторизация'
    RECOVERY = 'Восстановление пароля'
    CHECK = 'Регистрация'
    VERIFICATION_EMAIL = 'Подтверждение email'
    VERIFICATION_INVALID_EMAIL = 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'
    VERIFICATION_INVALID_NAME = 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
    ENTRY_VK = 'Войти'
    OK = 'Одноклассники'
    CHOICE_ACCOUNT = 'Вход'
    MM = 'Войти и разрешить'
