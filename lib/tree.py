# Initialize an empty output list 
# Initialize a list of nodes to visit and add the root node to it 
# While there are nodes in the nodes to visit list 
  # Remove the first node from the nodes to visit list 
  # Add it's value to the output list 
  # Add its children (if any) to the end of the nodes to visit list
# Return the output list 


class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    nodes_to_visit = [self.root]

    while len(nodes_to_visit) > 0:
      node = nodes_to_visit.pop(0)
      if node['id'] == id:
        #result.append(node['id'])
        return node 
      nodes_to_visit = nodes_to_visit + node['children']

    return None 

  
"""
class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    nodes_to_visit = [self.root]

    while len(nodes_to_visit) > 0:
      node = nodes_to_visit.pop(0)
      if node['id'] == id:
        return node
      nodes_to_visit = node['children'] + nodes_to_visit

    return None
"""