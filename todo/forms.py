from django import forms


class TodoForm(forms.Form):
    text = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'todo-input', 'placeholder': 'Enter todo here...'}))
