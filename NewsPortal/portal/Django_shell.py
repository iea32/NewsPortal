from portal.models import *
from django.contrib.auth.models import User

# Создать двух пользователей (с помощью метода User.objects.create_user('username')).
# Создать два объекта модели Author, связанные с пользователями.

slava_user = User.objects.create_user('slava')
misha_user = User.objects.create_user('misha')

slava = Author.objects.create(user=slava_user)
misha = Author.objects.create(user=misha_user)

# Добавить 4 категории в модель Category.

cat_sport = Category.objects.create(name='Спорт')
cat_kino = Category.objects.create(name='Кино')
cat_music = Category.objects.create(name='Музыка')
cat_game = Category.objects.create(name='Игры')

# Добавить 2 статьи и 1 новость.

text1 = "Статья про спорт и кино"
text2 = "Статья про музыку"
text3 = "Новости про игры"

a1 = Post.objects.create(author=slava,post_type=Post.article,title="Статья1",text=text1)
a2 = Post.objects.create(author=slava,post_type=Post.article,title="Статья2",text=text2)
a3 = Post.objects.create(author=misha,post_type=Post.news,title="Новости",text=text3)

# Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий).

PostCategory.objects.create(post = a1, category = cat_sport)
PostCategory.objects.create(post = a1, category = cat_kino)
PostCategory.objects.create(post = a2, category = cat_music)
PostCategory.objects.create(post = a3, category = cat_game)

# Создать как минимум 4 комментария к разным объектам модели Post (в каждом объекте должен быть как минимум один комментарий).

comment1 = Comment.objects.create(post = a1, user = slava.user, text = "Комментарий1")
comment2 = Comment.objects.create(post = a2, user = slava.user, text = "Комментарий2")
comment3 = Comment.objects.create(post = a3, user = misha.user, text = "Комментарий3")
comment4 = Comment.objects.create(post = a1, user = misha.user, text = "Комментарий4")

