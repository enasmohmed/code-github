from modeltranslation.translator import TranslationOptions, translator

from properties.models import Category, CardEliteHome, CardDoxHome, CardsProgramUnits, CardsFeatures, DetailSection, \
    SubCategory, DetailSubCategory


class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)
    required_languages = {"ar": ("name",), "default": ("name",)}


class SubCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


class DetailSubCategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'message',)


class DetailSectionTranslationOptions(TranslationOptions):
    fields = ('title_section','description_section',)


class CardsFeaturesTranslationOptions(TranslationOptions):
    fields = ('title_card', 'description_card',)


class CardsProgramUnitsTranslationOptions(TranslationOptions):
    fields = ('title_program', 'description_program',)


class CardDoxHomeTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


class CardEliteHomeTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


class PostTranslationOptions(TranslationOptions):
    fields = ('author','description_author','title','tags','description_one','description_two','category',)


translator.register(Category, CategoryTranslationOptions)

translator.register(SubCategory, SubCategoryTranslationOptions)

translator.register(DetailSubCategory, DetailSubCategoryTranslationOptions)

translator.register(DetailSection, DetailSectionTranslationOptions)

translator.register(CardsFeatures, CardsFeaturesTranslationOptions)
translator.register(CardsProgramUnits, CardsProgramUnitsTranslationOptions)

translator.register(CardDoxHome, CardDoxHomeTranslationOptions)
translator.register(CardEliteHome, CardEliteHomeTranslationOptions)

