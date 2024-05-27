from django import forms

class SignUpForm(forms.Form):
    usuario = forms.CharField(
        max_length=18,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-input",
                "placeholder": "Username",
                "required": True,
                "max-length": 18,
            }
        ),
    )
    nome = forms.CharField(
        max_length=12,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-input",
                "placeholder": "Name",
                "required": True,
                "max-length": 12,
            }
        ),
    )
    sobrenome = forms.CharField(
        max_length=14,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-input",
                "placeholder": "Last Name",
                "required": True,
                "max-length": 14,
            }
        ),
    )
    email = forms.CharField(
        max_length=150,
        required=False,
        widget=forms.TextInput(
            attrs={"class": "form-input", "placeholder": "Email", "required": True}
        ),
    )
    senha = forms.CharField(
        max_length=190,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-input",
                "placeholder": "Password",
                "required": True,
                "type": "password",
            }
        ),
    )

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields["usuario"].label = False
        self.fields["nome"].label = False
        self.fields["sobrenome"].label = False
        self.fields["email"].label = False
        self.fields["senha"].label = False

class SignInForm(forms.Form):
    usuario = forms.CharField(
        max_length=150,
        required=False,
        widget=forms.TextInput(
            attrs={"class": "form-input", "placeholder": "Username", "required": True}
        ),
    )
    senha = forms.CharField(
        max_length=190,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-input",
                "placeholder": "Password",
                "required": True,
                "type": "password",
            }
        ),
    )

    def __init__(self, *args, **kwargs):
        super(SignInForm, self).__init__(*args, **kwargs)
        self.fields["usuario"].label = False
        self.fields["senha"].label = False
