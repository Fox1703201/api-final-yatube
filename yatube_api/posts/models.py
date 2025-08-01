from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Название группы"
    )
    slug = models.SlugField(
        unique=True,
        verbose_name="Слаг"
    )
    description = models.TextField(
        verbose_name="Описание"
    )

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField(verbose_name="Текст поста")
    pub_date = models.DateTimeField(
        "Дата публикации", auto_now_add=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts",
        verbose_name="Автор"
    )
    image = models.ImageField(
        upload_to="posts/",
        null=True,
        blank=True,
        verbose_name="Изображение"
    )
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="posts",
        verbose_name="Группа"
    )

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def __str__(self):
        return self.text[:30]


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Автор"
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Пост"
    )
    text = models.TextField(verbose_name="Текст комментария")
    created = models.DateTimeField(
        "Дата добавления",
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return self.text[:30]


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        related_name="follower",
        on_delete=models.CASCADE,
        verbose_name="Подписчик"
    )
    following = models.ForeignKey(
        User,
        related_name="following",
        on_delete=models.CASCADE,
        verbose_name="Автор"
    )

    class Meta:
        unique_together = ["user", "following"]
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"

    def __str__(self):
        return f"{self.user} подписан на {self.following}"
