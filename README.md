light_ray
==========
### Аналіз касових чеків та ведення домашньої бухгалтерії

Одразу після клонування рекомендуємо налаштувати git push. Для перейдіть в каталог з проектом та виконайте `nano .git/config`. Додайте
```code
[push]
    default=current
```
внизу файла. Збережіть зміни.

Тепер налаштуйте користувача:

`git config user.name <ваше ім’я>`

`git config user.email <email>`

`git config --global color.ui auto` - за бажанням :)

Наступний крок: створюємо новий virtualenv
```code
virtualenv env --no-site-packages
```
Після того, як процес завершиться, активуємо його командою

`source env/bin/activate`

Тепер, коли нове "віртуальне оточення" створено та активовано можна поставити усі необхідні пакети командою:
`pip install -r req.txt`
