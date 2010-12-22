# -*- coding: utf-8 -*-

from django import template

register = template.Library()

CZECH_MONTHS = {
    1: u'Lednový',
    2: u'Únorový',
    3: u'Březnový',
    4: u'Dubnový',
    5: u'Květnový',
    6: u'Červnový',
    7: u'Červnencový',
    8: u'Srpnový',
    9: u'Zářiový',
    10: u'Říjnový',
    11: u'Listopadový',
    12: u'Prosincový',

}

@register.simple_tag
def czech_month(photo):
    """
    Vrati spravne vysklonovany mesic, ve kterem byla fotka porizena.
    """
    return CZECH_MONTHS[photo.created.month]
