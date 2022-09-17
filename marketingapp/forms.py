from django.forms import Form,fields,widgets

class ContactForm(Form):
    name = fields.CharField(max_length=100)
    email = fields.CharField(max_length=100)
    subject = fields.CharField(max_length=100)
    message = fields.CharField(widget=widgets.Textarea)