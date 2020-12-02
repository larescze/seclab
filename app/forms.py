from django import forms


class SearchForm(forms.Form):
    # Search input
    query = forms.CharField(label="", required=False)

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            # CSS class
            visible.field.widget.attrs['class'] = 'form-check-input'
        # Search input place holder attribute
        self.fields['query'].widget.attrs['placeholder'] = 'Search for the Internet of Things (IoT)'
        # Search input class attribute
        self.fields['query'].widget.attrs['class'] = 'form-control'
