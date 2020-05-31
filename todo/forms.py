from django import forms


from .models import Todo


# class TodoForm(forms.Form):
#     text = forms.CharField(max_length=100, widget=forms.TextInput(
#         attrs={'class': 'todo-input', 'placeholder': 'Enter todo here...'}))


class TodoModelForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['text']
        widgets = {'text': forms.TextInput(
            attrs={'class': 'todo-input', 'placeholder': 'Enter todo here...'})}
