# api_final
api final


API для социальной Yatube. Позволяет публиковать посты, комментировать, вступать в группы и подписываться на авторов.

Установка 

git clone https://github.com/Fox1703201/api-final-yatube.git
python -m venv venv
source venv/Scripts/activate   
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

Примеры запросов

GET /api/v1/posts/ — список постов
POST /api/v1/posts/ — создать пост
GET /api/v1/posts/{id}/comments/ — комментарии к посту
POST /api/v1/follow/ — подписка на пользователя
