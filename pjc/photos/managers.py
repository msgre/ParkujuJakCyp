# -*- coding: utf-8 -*-

def public(self):
    """
    Vrati pouze verejne zaznamy.
    """
    return self.filter(public=True)
