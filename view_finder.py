__author__ = 'Roderik'


def find_views_with_id(id, parent):
    found_views = []
    return recurse_find_views_with_id(id, parent, found_views)


def recurse_find_views_with_id(id, parent, found_views):
    if parent.id == id:
        found_views.append(parent)

    if parent.childs:
        for child in parent.childs:
            recurse_find_views_with_id(id, child, found_views)
    return found_views