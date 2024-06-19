from django.forms import ModelForm
from main.models import Credit, Payment

# Create the form class.
class CreditForm(ModelForm):
    class Meta:
        model = Credit
        fields = ["start_date", "end_date", "sum"]