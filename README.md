Социальная сеть любителей котов "Kittygram"

Каждый пользователь сайта в своём личном кабинете имеет возможность публиковать фотографии котов, присваивать каждому коту имя, год рождения, цвет, а также любые достижения.

Технологии: Python 3.10, Django 3.2, Django REST framework, React

Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:alexrashkin/kittygram_final.git
```

```
cd kittygram_final
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас Windows

    ```
    source env/scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
Автор: 
- Александр Рашкин  - https://github.com/alexrashkin
