from tabook.forms.abook import card_form


class TestCardForm(object):
    def test_ignore_emty_addresses(self):
        variable_dict = {
            'addresses-1.id': u'', 'first_name': u'Roman',
            'last_name': u'Dolgiy', 'addresses-1.phone_number': u'',
            'addresses-0.id': u'4', 'addresses-2.id': u'',
            'addresses-2.phone_number': u'', 'addresses-0.address': u'Bla bla',
            'addresses-2.address': u'', 'addresses-2.zip_code': u'',
            'addresses-1.zip_code': u'', 'addresses-0.zip_code': u'12345',
            'addresses-0.phone_number': u'123-123-1234', 'id': u'2',
            'addresses-1.address': u'Test'
        }
        result = card_form._ignore_emty_addresses(variable_dict)
        assert ("addresses-1.address" in result and
                "addresses-2.address" not in result)
