from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Category)
 
class Catadmin(admin.ModelAdmin):
    list_display=['name'] 
    
    
class AnswerInlineModel(admin.TabularInline):
    model = models.Answer 
    fields = [
        'answer_text',
        'is_right',
    ]    
# This class is used to create a form for adding and editing answers in the admin site
class QuestionInlineModel(admin.TabularInline):
    model = models.Questions 
    fields = [
        'title',
        'technique',
        'difficulty',
        'is_active',
    ]

@admin.register(models.Quizzes)

class QuizAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
    ]

    inlines = [ QuestionInlineModel,]
    
    
# A decorator that registers the QuestionAdmin class with the admin site.    
@admin.register(models.Questions)

class QuestionAdmin(admin.ModelAdmin):

    fields = [
        'title',
        'quiz',
        'technique',
        'difficulty',
        'is_active',
        
       
    ]
    list_display = [
        'title',
        'quiz',
        'technique',
        'difficulty',
        'is_active',
        'date_created',
    ]
    inlines = [ AnswerInlineModel, ]    

@admin.register(models.Answer)
# This class is a subclass of the admin.ModelAdmin class, and it's going to customize the way the
# Answer model is displayed in the admin.
class AnswerAdmin(admin.ModelAdmin):
    list_display = [
        'answer_text',
        'is_right',
        'question',

    ]