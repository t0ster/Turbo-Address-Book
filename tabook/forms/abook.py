"""
Address Book Forms and Widgets
"""
from tw.api import JSLink
from tw.jquery import jquery_js
from tw.core import WidgetsList
from tw.forms import TableForm, TextField, \
    FormFieldRepeater, ListFieldSet, HiddenField
from tw.forms.validators import Int, NotEmpty, Email, UnicodeString
from formencode.national import USPostalCode as PostalCode, \
                                USStateProvince as StateProvince, \
                                USPhoneNumber as PhoneNumber
from formencode.variabledecode import variable_decode, variable_encode
from sprox.tablebase import TableBase
from sprox.fillerbase import TableFiller

from tabook import model


class ZipField(TextField):
    """
    TextField with javascript zip code validation
    """
    zip_field_js = JSLink(modname=__name__, filename="static/zip_field.js")
    javascript = [jquery_js, zip_field_js]


class AddressFieldset(ListFieldSet):
    """
    Subform for address editing
    """
    class fields(WidgetsList):
        id = HiddenField(validator=Int)
        address = TextField(validator=NotEmpty, size=50)
        zip_code = ZipField(validator=PostalCode(not_empty=True))
        state = TextField(validator=StateProvince(not_empty=True))
        phone_number = TextField(validator=PhoneNumber(not_empty=True))
        lat = TextField(label_text=u"Latitude")
        lng = TextField(label_text=u"Longitude")


class CardForm(TableForm):
    """
    Form for editing person card, includes inline subforms for address editing
    """
    class fields(WidgetsList):
        id = HiddenField(validator=Int)
        first_name = TextField(validator=NotEmpty)
        last_name = TextField(validator=NotEmpty)
        email = TextField(validator=Email(not_empty=True))
        addresses = FormFieldRepeater(widget=AddressFieldset())

    # Ignoring empty addresses subforms so they won't fire up
    # validation errors
    def validate(self, value, state=None, use_request_local=True):
        if value:
            value = self._ignore_emty_addresses(value)
        return super(CardForm, self).validate(value, state, use_request_local)

    def _ignore_emty_addresses(self, value):
        value = variable_decode(value)
        value["addresses"] = [address for address in
                              value["addresses"] if any(address.values())]
        return variable_encode(value)


# Using `sprox` to list address book cards
class CardTable(TableBase):
    __model__ = model.Card
    __omit_fields__ = ["id", "first_name", "last_name", "state"]
    __add_fields__ = {"name": None, "addresses": None}
    __field_order__ = ["name", "email", "addresses"]
    __headers__ = {
        "__actions__": "Actions",
        "name": "Name",
        "email": "Email",
        "addresses": "Addresses",
    }


class CardTableFiller(TableFiller):
    __model__ = model.Card
    __add_fields__ = {"name": None, "addresses": None}

    def name(self, obj):
        return obj.name

    def addresses(self, obj):
        return "\n".join(
            ["<div>%s, %s, %s, %s</div>" %
             (addr.address, addr.state, addr.zip_code, addr.phone_number)
             for addr in obj.addresses]
        )

    def __actions__(self, obj):
        primary_fields = self.__provider__.get_primary_fields(self.__entity__)
        pklist = "/".join(map(lambda x: str(getattr(obj, x)), primary_fields))
        value = ('<div><div><a href="/abook/edit/' + pklist + '/" '
                 'style="text-decoration:none">edit</a>'
                 '</div><div>'
                 '<form method="POST" action="/abook/delete/' + pklist + '/" '
                 'class="button-to">'
                 '<input type="hidden" name="_method" value="DELETE" />'
                 '<input class="delete-button" onclick="return '
                 'confirm(\'Are you sure?\');" value="delete" type="submit" '
                 'style="background-color: transparent; float:left; border:0; '
                 'color: #286571; display: inline; margin: 0; padding: 0;"/>'
                 '</form>'
                 '</div></div>')
        return value


class SearchCardTableFiller(CardTableFiller):
    # Overriding `TableFiller._do_get_provider_count_and_objs` to
    # enable search by phone feature
    def _do_get_provider_count_and_objs(self, **kwargs):
        phone_number = kwargs.get("phone_number")
        query = self.provider_hint.query(model.Card).join(
            model.Address).filter(
            model.Address.phone_number.like("%%%s%%" % phone_number))
        count = query.count()
        self.__count__ = count
        objs = query.all()
        return count, objs


card_form = CardForm("card_form")
card_table = CardTable(model.DBSession)
card_table_filler = CardTableFiller(model.DBSession)
search_card_table_filler = SearchCardTableFiller(model.DBSession)
