from django import forms


class SearchForm(forms.Form):
    query = forms.CharField(label="", required=False)

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-check-input'
        self.fields['query'].widget.attrs['placeholder'] = 'Search for the Internet of Things (IoT)'
        self.fields['query'].widget.attrs['class'] = 'form-control'
