import logging

from tg import expose, flash, require, url, request, redirect
from pylons.i18n import ugettext as _, lazy_ugettext as l_
from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from repoze.what import predicates

from tabook.lib.base import BaseController, render
from tabook.lib.helpers import html
from tabook.forms.abook import card_add_form

log = logging.getLogger(__name__)


class AbookController(BaseController):

    @expose('tabook.templates.abook.index')
    @require(predicates.has_permission('manage', msg=l_('Only for managers')))
    def index(self):
        return {}

    @expose('tabook.templates.abook.edit')
    @require(predicates.has_permission('manage', msg=l_('Only for managers')))
    def new(self):
        c.form = html.literal(card_add_form)
        return {}

    def edit(self, id):
        return {}

    def save(self):
        pass
