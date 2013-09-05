from datetime import datetime
from tinymodel import TinyModel, FieldDef


class Advertiser(TinyModel):

    """
    Represents an Operative Advertiser.
    """

    FIELD_DEFS = [
        FieldDef(title='id', allowed_types=[unicode, str, long, int, type(None)]),
        FieldDef(title='name', allowed_types=[unicode, str]),
    ]


class Order(TinyModel):

    """
    Represents an Operative order.
    """

    FIELD_DEFS = [
        FieldDef(title='advertiser', allowed_types=['operative.models.Advertiser'], relationship='has_one'),
        FieldDef(title='id', allowed_types=[long, int, type(None)]),
        FieldDef(title='name', allowed_types=[unicode, str]),
        FieldDef(title='start_date', allowed_types=[datetime]),
        FieldDef(title='end_date', allowed_types=[datetime]),
    ]


class LineItem(TinyModel):

    """
    Represents an Operative Line Item.
    """

    FIELD_DEFS = [
        FieldDef(title='order', allowed_types=['operative.models.Order'], relationship='has_one'),
        FieldDef(title='id', allowed_types=[long, int, type(None)]),
        FieldDef(title='name', allowed_types=[unicode, str]),
        FieldDef(title='start_date', allowed_types=[datetime]),
        FieldDef(title='end_date', allowed_types=[datetime]),
        FieldDef(title='action', allowed_types=[long, int, type(None)]),
        FieldDef(title='quantity', allowed_types=[long, int, type(None)]),
        FieldDef(title='unit_cost', allowed_types=[long, int, type(None)]),
        FieldDef(title='cost_type', allowed_types=[unicode, str]),
        FieldDef(title='cost', allowed_types=[float]),
    ]
