import settings
from util import view_finder

__author__ = 'Roderik'


def apply_width_constraint(parent, id_list):

    views = []
    for id in id_list:
        views.extend(view_finder.find_views_with_id(id, parent))

    for i in range(10):

        # for view in views:
        #     if view.debug_id == 'container':
        #         print ('begin', view.width)

        parent.measure()
        # for view in views:
        #     if view.debug_id == 'container':
        #         print ('after measure', view.width)

        parent.post_measure(settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)
        # for view in views:
        #     if view.debug_id == 'container':
        #         print ('after post measure', view.width)

        parent.apply_gravity(0, 0, settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)
        # for view in views:
        #     if view.debug_id == 'container':
        #         print ('after apply gravity', view.width)


        max_width = 0
        for view in views:
            if view.width > max_width:
                max_width = view.width

        for view in views:
            # print (view.width, 'set to', max_width)
            view.width = max_width

            # if view.debug_id == 'container':
            #     print (view.width)


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