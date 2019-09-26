from django import forms

from applications.blog_app.models import blog_post


class CreateBlogForm(forms.ModelForm):
    class Meta:
        model = blog_post
        fields = (
            "blog_title",
            "blog_img",
            "blog_description"
        )