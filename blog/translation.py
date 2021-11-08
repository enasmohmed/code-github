from modeltranslation.translator import TranslationOptions, translator

from blog.models import Category, Post


class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


class PostTranslationOptions(TranslationOptions):
    fields = ('author', 'description_author', 'title', 'description_one', 'description_two',)


translator.register(Post, PostTranslationOptions)

translator.register(Category, CategoryTranslationOptions)




