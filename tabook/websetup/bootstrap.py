# -*- coding: utf-8 -*-
"""
Setup the Turbo-Address-Book application
"""

import logging
from tg import config
from tabook import model

import transaction


def bootstrap(command, conf, vars):
    """Place any commands to setup tabook here"""

    # <websetup.bootstrap.before.auth
    from sqlalchemy.exc import IntegrityError
    try:
        # Adding users
        u = model.User()
        u.user_name = u"manager"
        u.display_name = u"Example manager"
        u.email_address = u"manager@somedomain.com"
        u.password = u"managepass"

        model.DBSession.add(u)

        g = model.Group()
        g.group_name = u"managers"
        g.display_name = u"Managers Group"

        g.users.append(u)

        model.DBSession.add(g)

        p = model.Permission()
        p.permission_name = u"manage"
        p.description = (u"This permission give an administrative "
                         "right to the bearer")
        p.groups.append(g)

        model.DBSession.add(p)

        u1 = model.User()
        u1.user_name = u"editor"
        u1.display_name = u"Example editor"
        u1.email_address = u"editor@somedomain.com"
        u1.password = u"editpass"

        model.DBSession.add(u1)
        # ---

        # Adding address book dummy data
        card = model.Card()
        card.first_name = u"Larry"
        card.last_name = u"Smith"
        card.email = u"larry@domain.com"

        address = model.Address()
        address.address = u"1600 Amphitheatre Parkway, Mountain View"
        address.zip_code = u"94043"
        address.state = u"CA"
        address.phone_number = u"650-253-0000"
        address.lat = 37.4213068
        address.lng = -122.08529
        card.addresses.append(address)

        address = model.Address()
        address.address = u"201 S. Division St."
        address.zip_code = u"48104"
        address.state = u"MI"
        address.phone_number = u"734-332-6500"
        address.lat = 42.279901
        address.lng = -83.743825
        card.addresses.append(address)

        address = model.Address()
        address.address = u"2200 Cambridge Place"
        address.zip_code = u"21244"
        address.state = u"MD"
        address.phone_number = u"410-591-0566"
        address.lat = 39.3352109
        address.lng = -76.7490424
        card.addresses.append(address)

        model.DBSession.add(card)

        card = model.Card()
        card.first_name = u"Richard"
        card.last_name = u"Payne"
        card.email = u"richardcpayne@example.com"

        address = model.Address()
        address.address = u"556 Johnstown Road"
        address.zip_code = u"60106"
        address.state = u"IL"
        address.phone_number = u"847-378-5599"
        address.lat = 42.0307639
        address.lng = -88.3519304
        card.addresses.append(address)

        address = model.Address()
        address.address = u"4038 Zimmerman Lane, Los Angeles"
        address.zip_code = u"90014"
        address.state = u"CA"
        address.phone_number = u"213-402-3990"
        address.lat = 34.4605053
        address.lng = -118.488888
        card.addresses.append(address)

        model.DBSession.add(card)

        card = model.Card()
        card.first_name = u"Ann"
        card.last_name = u"Smith"
        card.email = u"annsmith@example.com"

        address = model.Address()
        address.address = u"556 Johnstown Road"
        address.zip_code = u"60106"
        address.state = u"IL"
        address.phone_number = u"147-128-3312"
        address.lat = 42.0307639
        address.lng = -88.3519304
        card.addresses.append(address)

        address = model.Address()
        address.address = u"4038 Zimmerman Lane, Los Angeles"
        address.zip_code = u"90014"
        address.state = u"CA"
        address.phone_number = u"215-412-3590"
        address.lat = 34.4605053
        address.lng = -118.488888
        card.addresses.append(address)

        model.DBSession.add(card)
        # ---

        model.DBSession.flush()
        transaction.commit()
    except IntegrityError:
        print("Warning, there was a problem adding your auth data, "
              "it may have already been added:")
        import traceback
        print traceback.format_exc()
        transaction.abort()
        print "Continuing with bootstrapping..."

    # <websetup.bootstrap.after.auth>
