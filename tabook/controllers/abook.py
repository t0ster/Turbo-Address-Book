"""
Address Book Controller
"""
import logging

from tg import expose, flash, require, redirect, validate
from pylons.i18n import lazy_ugettext as l_
from pylons import tmpl_context as c
from repoze.what import predicates

from tabook.lib.base import BaseController
from tabook.lib.helpers import html
from tabook.lib import geocoding
from tabook.forms.abook import card_form, card_table, card_table_filler, \
    search_card_table_filler
from tabook import model

log = logging.getLogger(__name__)


class AbookController(BaseController):
    @expose('tabook.templates.abook.index')
    @require(predicates.has_permission('manage', msg=l_('Only for managers')))
    def index(self, *args, **kwargs):
        phone_number = kwargs.get("phone_number")
        if phone_number is not None:
            value = search_card_table_filler.get_value(
                phone_number=phone_number)
        else:
            value = card_table_filler.get_value()
        c.table = html.literal(card_table(value=value))
        return {}

    @expose('tabook.templates.abook.edit')
    @require(predicates.has_permission('manage', msg=l_('Only for managers')))
    def new(self, **kwargs):
        c.form = html.literal(card_form(value=kwargs, action="post"))
        return {}

    @expose()
    @require(predicates.has_permission('manage', msg=l_('Only for managers')))
    @validate(form=card_form, error_handler=new)
    def post(self, **kwargs):
        self.save_card(kwargs)
        flash("Successfully saved")
        redirect("index")

    @expose('tabook.templates.abook.edit')
    @require(predicates.has_permission('manage', msg=l_('Only for managers')))
    def edit(self, id, **kwargs):
        card = model.DBSession.query(model.Card).get(id)
        c.form = html.literal(card_form(value=card, action="/abook/put"))
        return {}

    @expose()
    @validate(form=card_form, error_handler=edit)
    @require(predicates.has_permission('manage', msg=l_('Only for managers')))
    def put(self, **kwargs):
        self.save_card(kwargs)
        flash("Successfully updated")
        redirect("index")

    def save_card(self, card_dict):
        """
        Saves card to DB

        Arguments:
        - `card_dict`: validated form parameters
        """

        def save_addresses(card_id, addresses):
            for address_dict in addresses:
                if not address_dict["address"]:
                    return
                address_id = address_dict.pop("id")
                if address_id is not None:
                    address = model.DBSession.query(
                        model.Address).get(address_id)
                else:
                    address = model.Address()
                    address.card_id = card_id

                address.lat, address.lng = geocoding.get_lat_lng(
                    "%s, %s, %s" %
                    (address.address, address.state, address.zip_code))
                del address_dict["lat"]
                del address_dict["lng"]

                for _key, _value in address_dict.items():
                    setattr(address, _key, _value)
                model.DBSession.merge(address)

        id = card_dict.pop("id")
        if id is not None:
            card = model.DBSession.query(model.Card).get(id)
        else:
            card = model.Card()

        addresses = card_dict.pop("addresses")

        for key, value in card_dict.items():
            setattr(card, key, value)
        card = model.DBSession.merge(card)
        model.DBSession.flush()

        save_addresses(card.id, addresses)

    @expose()
    @require(predicates.has_permission('manage', msg=l_('Only for managers')))
    def delete(self, id, **kwargs):
        card = model.DBSession.query(model.Card).get(id)
        model.DBSession.delete(card)
        flash("Successfully deleted")
        redirect("/abook")
