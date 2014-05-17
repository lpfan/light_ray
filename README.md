light_ray
==========
### Аналіз касових чеків та ведення домашньої бухгалтерії


### З чого почати ?

#### Додаткові залежності для linux
Для роботи із зображеннями в форматі jpeg в ubuntu потрібно встановити наступні пакети:
```code
sudo apt-get install libjpeg-dev libfreetype6 libfreetype6-dev zlib1g-dev libpng12-dev
```

А для встановлення системи розпізнавання потрібно виконати:
```code
sudo apt-get install tesseract-ocr
```

 Наступним кроком буде встановлення словників для розпізнавання. Для цього з сайту проекта https://www.code.google.com/p/tesseract-ocr 

 скачуємо 2 файли:

- https://code.google.com/p/tesseract-ocr/downloads/detail?name=tesseract-ocr-3.02.ukr.tar.gz&can=2&q=

- https://code.google.com/p/tesseract-ocr/downloads/detail?name=tesseract-ocr-3.02.rus.tar.gz&can=2&q=

 Розархівовуємо їхній вміст у 
`
  /usr/share/tesseract-ocr/tessdata
`

#### Розгортання репозиторію
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

