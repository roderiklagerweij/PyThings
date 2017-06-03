import view_finder

__author__ = 'Roderik'


def apply_constraint(parent, id_list):

    views = []
    for id in id_list:
        views.extend(view_finder.find_views_with_id(id, parent))

    for i in range(10):
        # print ('iteration')
        parent.measure()
        parent.post_measure(640, 480)

        max_width = 0
        for view in views:
            if view.get_width() > max_width:
                max_width = view.get_width()
                # print ('new max width:', max_width, 'from view', view)

        for view in views:
            # print ('set', max_width, 'to', view)
            view.set_width(max_width)