from tw.core import WidgetsList
from tw.forms import TableForm, TextField, CalendarDatePicker, SingleSelectField, TextArea
from formencode.validators import Int, NotEmpty, DateConverter, DateValidator


class CardForm(TableForm):
    class fields(WidgetsList):
        first_name = TextField(validator=NotEmpty)
        last_name = TextArea(attrs=dict(rows=3, cols=25))
        address = TextArea(attrs=dict(rows=3, cols=25))

card_add_form = CardForm("create_card_form")
