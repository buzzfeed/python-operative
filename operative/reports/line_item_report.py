from operative.reports import Report
from operative.models import (
    LineItem,
    Order,
    Advertiser
)


class LineItemReport(Report):

    def parse_row(self, row):
        """
        Parses a row of csv data into a LineItem object.
        This function contains information on how to translate column headers into object attributes.
        It is meant to be delegated by the parent Report class.

        :param dict row: A row of csv data

        :rtype LineItem:

        """
        advertiser = Advertiser(**{'id': row['Advertiser ID'],
                                   'name': row['Advertiser Name'], })

        order = Order(**{'id': int(row['Order ID']) if row['Order ID'] else None,
                         'name': row['Order Name'],
                         'start_date': row['Order Start Date'],
                         'end_date': row['Order End Date'],
                         'advertiser': advertiser, })

        line_item = LineItem(**{'id': int(row['Line Item ID']) if row['Line Item ID'] else None,
                                'name': row['Line Item Name'],
                                'start_date': row['Line Item Start Date'],
                                'end_date': row['Line Item End Date'],
                                'action': row['Line Item Action'],
                                'quantity': int(row['Quantity']),
                                'unit_cost': float(row['Unit Cost']),
                                'cost_type': row['Cost Type'],
                                'cost': float(row['Cost']),
                                'order': order, })

        return line_item
