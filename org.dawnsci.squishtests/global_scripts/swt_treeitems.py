# adapted from http://kb.froglogic.com/display/KB/Example+-+Getting+TreeItem+of+SWT+Tree+via+path+(Java)

import re
source(findFile("scripts", "namedtuple.py"))

def get_swt_tree_sub_item(tree_or_item, path, column, verbose=True):
    """Get sub item in an SWT tree, where the sub item is the
       com.froglofic.squish.swt.TreeSubItem virtual wrapper around
       an item's specified column.
       
       tree_or_item and path are passed directly to get_swt_tree_item,
       see documentation thre for details.
       
       column in the 0-index column number to extract the sub item for.
       The fields of iterest if a TreeSubItem are:
       - item, the TreeItem (row) that this sub item is part of
       - text, the displayed text
       The object returned can be used as any other object can, for
       instance as the target of mouseClick()
    """
    item = get_swt_tree_item(tree_or_item, path, verbose=verbose)
    test.verify(item is not None, "Found object for path " + str(path))
    subitems = object.children(item)
    if verbose:
        test.log("Tree item had " + str(len(subitems)) + " columns")
    return subitems[column]


def get_swt_tree_item(tree_or_item, path, sub_path=None, verbose=True):
    """Get item in an SWT tree.
    path is a list of TreeItem texts, denoting the path of
    the desired item. For example:
 
        Node1
            Sub-Node1
        Node2
 
        path = ["Node1", "Sub-Node1"]
 
    In addition each element of path can also be a tuple
    of (TreeItem_text, occurrence), where occurrence
    specifies which TreeItem to use in case of duplicates
    under the same parent TreeItem. For example:
 
        Node0
            Sub-Node1
            Sub-Node1
 
        path = ["Node0", ("Sub-Node1", 2)]"""
 
    if sub_path is None:
        sub_path = path
    n = tree_or_item.getItemCount()
    occurrence = None
    for i in range(n):
        item = tree_or_item.getItem(i)
        item_text = item.getText()
 
        if occurrence is None:
            path_element = sub_path[0]
            if not isinstance(path_element, tuple):
                path_element = (path_element, 1)
            occurrence = path_element[1]
            path_element = path_element[0]
        if item_text == path_element:
            if occurrence > 1:
                if verbose:
                    test.log("Ignoring: " + item_text + ", occurrence: " + str(occurrence))
                occurrence -= 1
                continue
 
            occurrence = None
            if verbose:
                test.log("Found " + item_text)
 
            if len(sub_path) == 1:
                if verbose:
                    test.log("Reached end of path")
                return item
            else:
                return get_swt_tree_item(item, path, sub_path[1:], verbose)
 
    if verbose:
        test.log("Error: Path element not found: " + str(sub_path[0]) + " (Complete path: " + str(path) + ")")
    return None


_swt_tree_node = namedtuple('_swt_tree_node', ["children", "column", "object"])
def get_swt_tree_texts(tree_or_item, columns_tuple_type=None, verbose=False):
    '''
    Get all the items in thew tree as they are displayed to the user.
    

    node = ([children-nodes], (column_texts), tree_item_object) 
    '''
    if columns_tuple_type is None:
        column_count = tree_or_item.getColumnCount()
    else:
        column_count = len(columns_tuple_type._fields)
    if column_count == 0:
        column_count = 1
    if columns_tuple_type is None:
        # Try and populate the names from the actual column names
        column_names = []
        for n in range(column_count):
            column_name = tree_or_item.getColumn(n).getText()
            column_name = re.sub('[^0-9a-zA-Z_]', '_', column_name)
            if column_name in column_names:
                column_name += "_"
            column_names.append(column_name)
        columns_tuple_type = namedtuple('columns_tuple_type', column_names)
    if columns_tuple_type is None:
        columns_tuple_type = namedtuple('columns_tuple_type', ["Column" + str(i) for i in range(10)])
    
    n = tree_or_item.getItemCount()
    if verbose:
        test.log(str(tree_or_item) + " getItemCount: " + str(n))
    children = []
    for i in range(n):
        item = tree_or_item.getItem(i)
        children.append(get_swt_tree_texts(item, columns_tuple_type=columns_tuple_type, verbose=verbose))

    item_texts = []
    try:
        if column_count == 1:
            item_text.append(tree_or_item.getText())
        else:
            for column in range(column_count):
                item_texts.append(tree_or_item.getText(column))
    except AttributeError:
        pass
    
    item_texts += [None] * (column_count - len(item_texts))
    if verbose:
        test.log(str(tree_or_item) + ".getTexts: " + str(item_texts))
    return _swt_tree_node(children, columns_tuple_type._make(item_texts), tree_or_item)
    
