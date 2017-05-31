import view_finder

__author__ = 'Roderik'


def apply_constraint(parent, id_list):

    views = []
    for id in id_list:
        views.extend(view_finder.find_views_with_id(id, parent))

    for i in range(10):
        parent.measure()
        parent.post_measure(640, 480)

        max_width = 0
        for view in views:
            if view.width > max_width:
                # print ('new max width:', view, view.width)
                max_width = view.width

        # print (max_width)

        for view in views:
            view.width = max_width