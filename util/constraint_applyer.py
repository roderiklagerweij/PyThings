import settings
from util import view_finder

__author__ = 'Roderik'


def apply_width_constraint(parent, id_list):

    views = []
    for id in id_list:
        views.extend(view_finder.find_views_with_id(id, parent))

    for i in range(10):
        # print ('iteration')
        parent.measure()
        parent.post_measure(settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)

        max_width = 0
        for view in views:
            if view.width > max_width:
                max_width = view.width
                # print ('new max width:', max_width, 'from view', view)

        for view in views:
            # print ('set', max_width, 'to', view)
            view.width_with_padding = max_width
            view.width = max_width - (view.padding_left + view.padding_right)


def apply_height_constraint(parent, id_list):

    views = []
    for id in id_list:
        views.extend(view_finder.find_views_with_id(id, parent))

    for i in range(50):
        parent.measure()
        parent.post_measure(settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)
        parent.layout(0, 0, settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)


        max_height = 0
        for view in views:
            if view.height > max_height:
                max_height = view.height

        for view in views:
            view.height_with_padding = max_height
            view.height = max_height - (view.padding_top + view.padding_bottom)