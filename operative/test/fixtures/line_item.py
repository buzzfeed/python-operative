import datetime

fb_advertiser = {'id': 'Facebook',
                 'name': 'Facebook'}

tw_advertiser = {'id': 'Twitter',
                 'name': 'Twitter'}

fb_order = {'advertiser': fb_advertiser,
            'id': None,
            'name': '10368_The Charles Koch Institute: Koch Institute totally non-partisan BuzzFeed Brews Event',
            'start_date': datetime.datetime(2013, 5, 6).isoformat(),
            'end_date': datetime.datetime(2013, 5, 27).isoformat()}

tw_order = {'advertiser': tw_advertiser,
            'id': None,
            'name': '10368_The Charles Koch Institute: Koch Institute totally non-partisan BuzzFeed Brews Event',
            'start_date': datetime.datetime(2013, 5, 6).isoformat(),
            'end_date': datetime.datetime(2013, 5, 27).isoformat()}

line_items = [{'order': tw_order,
               'id': 9358,
               'name': '104114-1_Social Content Seeding - Stumble/Twitter/Pinterest',
               'start_date': datetime.datetime(2013, 5, 6, 0, 0).isoformat(),
               'end_date': datetime.datetime(2013, 5, 27, 0, 0).isoformat(),
               'action': 'UPDATE',
               'quantity': 44000,
               'unit_cost': 0.0,
               'cost_type': 'CPC',
               'cost': 0.1},
              {'order': fb_order,
               'id': 9357,
               'name': '104113-1_Social Content Seeding - Facebook',
               'start_date': datetime.datetime(2013, 5, 6, 0, 0).isoformat(),
               'end_date': datetime.datetime(2013, 5, 27, 0, 0).isoformat(),
               'action': 'UPDATE',
               'quantity': 29333,
               'unit_cost': 0.0,
               'cost_type': 'CPC',
               'cost': 0.6}, ]
