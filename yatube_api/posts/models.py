from django.contrib.auth import get_user_model
from django.db import models
from django.conf import settings


User = get_user_model()


CLS_NAME_LEN: int = settings.CLS_NAME_LEN


class Group(models.Model):
    title = models.CharField(
        verbose_name='Группа',
        help_text='Задайте название группы',
        max_length=200)
    slug = models.SlugField(
        verbose_name='Slug идентификатор группы',
        help_text='Задайте slug группы',
        unique=True)
    description = models.TextField(
        verbose_name='Описание',
        help_text='Укажите описание группы')

    class Meta:
        ordering = ('title',)
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self) -> str:
        return self.title


class Post(models.Model):
    text = models.TextField(
        verbose_name='Текст поста',
        help_text='Введите текст поста')
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True,
        db_index=True)
    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE,
        related_name='posts')
    image = models.ImageField(
        verbose_name='Картинка',
        help_text='Загрузите картинку',
        upload_to='posts/',
        null=True,
        blank=True)
    group = models.ForeignKey(
        Group,
        verbose_name='Группа',
        help_text='Выберите группу или оставьте пустым',
        on_delete=models.SET_NULL,
        related_name='posts',
        blank=True,
        null=True)

    class Meta:
        ordering = ('pub_date',)
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self) -> str:
        return self.text[:CLS_NAME_LEN]


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        verbose_name='Автор комментария',
        on_delete=models.CASCADE,
        related_name='comments')
    post = models.ForeignKey(
        Post,
        verbose_name='Комментируемый пост',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='comments')
    text = models.TextField(
        verbose_name='Текст комментария',
        help_text='Прокомментируйте пост')
    created = models.DateTimeField(
        verbose_name='Дата добавления',
        auto_now_add=True,
        db_index=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self) -> str:
        return self.text[:CLS_NAME_LEN]


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name='Подписчик',
        on_delete=models.CASCADE,
        related_name='follower')
    following = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE,
        related_name='following')

    class Meta:
        ordering = ('-user',)
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'

    def __str__(self):
        return f'{self.user} подписан на {self.author}'
