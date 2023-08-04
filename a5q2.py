# Student Name: Pratham Shah                        Section Number: 01
# NSID: mvr659                                      Course Number: 41442
# Student Number: 11353450                          Instructor: Lauresa Stilling

def subst(tnode, t, r):
    """
    Substitute a target value t with a replacement value r wherever it appears in the given tree.
    :param tnode: The root treenode
    :param t: Target value to replace
    :param r: The replacement value
    :return: None
    """

    if tnode is None:
        return None
    else:
        if tnode.get_data() == t:
            tnode.set_data(r)
        subst(tnode.get_left(), t, r)
        subst(tnode.get_right(), t, r)
