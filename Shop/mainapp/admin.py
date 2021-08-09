from django.forms import ModelChoiceField, ModelForm, ValidationError

from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *
# Register your models here.

from PIL import Image


class SmartphoneAdminForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if not instance.sd:
            self.fields["sd_volume_max"].widget.attrs.update({
                "readonly": True, "style": "backgrounds: lightgray"
            })


    def clean(self):
        if not self.cleaned_data['sd']:
            self.cleaned_data['sd_volume_max'] = None
        return self.cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["image"].help_text = mark_safe('<span style ="color:red; font-size:14px;"> Load image with minimal allowed resolution {}x{}</span>'.format(*Product.MIN_RESOLUTION))

    def clean_image(self):
        image = self.cleaned_data["image"]
        img = Image.open(image)
        # print(image.width, image.height)
        min_height, min_width = Product.MIN_RESOLUTION
        max_height, max_width = Product.MAX_RESOLUTION
        if img.height < min_height or img.width < min_width:
            raise ValidationError("The loaded image is smaller than acceptable")
        if img.height > max_height or img.width > max_width:
            raise ValidationError("Loaded image is bigger than acceptable")
        return image


class NotebookAdminForm(ModelForm):


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["image"].help_text = mark_safe('<span style ="color:red; font-size:14px;"> Load image with minimal allowed resolution {}x{}</span>'.format(*Product.MIN_RESOLUTION))

    def clean_image(self):
        image = self.cleaned_data["image"]
        img = Image.open(image)
        # print(image.width, image.height)
        min_height, min_width = Product.MIN_RESOLUTION
        max_height, max_width = Product.MAX_RESOLUTION
        if img.height < min_height or img.width < min_width:
            raise ValidationError("The loaded image is smaller than acceptable")
        if img.height > max_height or img.width > max_width:
            raise ValidationError("Loaded image is bigger than acceptable")
        return image


class NotebookAdmin(admin.ModelAdmin):

    change_form_template = "admin.html"
    form = NotebookAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "category":
            return  ModelChoiceField(Category.objects.filter(slag="notebooks"))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class SmartphoneAdmin(admin.ModelAdmin):


    change_form_template = "admin.html"
    #form = SmartphoneAdminForm


    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "category":
            return  ModelChoiceField(Category.objects.filter(slag="smartphones"))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Category)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(Smartphone, SmartphoneAdmin)
admin.site.register(Notebook, NotebookAdmin)
admin.site.register(Order)