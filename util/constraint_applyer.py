import settings
from util import view_finder

__author__ = 'Roderik'


def apply_width_constraint(parent, id_list):

    views = []
    for id in id_list:
        views.extend(view_finder.find_views_with_id(id, parent))

    for i in range(10):
        parent.measure()
        parent.post_measure(settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)
        parent.apply_gravity(0, 0, settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)

        max_width = 0
        for view in views:
            if view.width > max_width:
                max_width = view.width

        for view in views:
            view.width = max_width

def apply_height_constraint(parent, id_list):

    views = []
    for id in id_list:
        views.extend(view_finder.find_views_with_id(id, parent))

    for i in range(10):
        parent.measure()
        parent.post_measure(settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)
        parent.apply_gravity(0, 0, settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)

        max_height = 0
        for view in views:
            if view.height > max_height:
                max_height = view.height

        for view in views:
            view.height = max_height