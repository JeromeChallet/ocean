from django import forms
from management.models  import Addaschool
# # # #
# # # #
class AddaschoolForm(forms.ModelForm):
        class Meta:
           model = Addaschool
           fields = "__all__"