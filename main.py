#!/usr/bin/env python
import sys

DEBUG = False      # set to True to see the debugging outputs
def debug(obj):
  if DEBUG:
    strings = "{}".format(obj).split("\n")
    for string in strings:
      print "DEBUG: "+ string

## verify the input
try:
  string = open(sys.argv[1]).read()
except:
  print "Cannot open the file!"
  print "Usage: %s filename" % sys.argv[0]
  sys.exit(1)

""" A derived class of the builtin data structure set
Supporting validation on values before adding to the set and
fetching by node label in O(n)"""
class Nodeset(set):
  def add(self, node):
    if node != None:
      return super(Nodeset, self).add(node)
  def __getitem__(self, label):
    for node in self:
      if node.label == label:
        return node
    return None
  def __setitem__(self, label, node):
    return super(Nodeset, self).add(node)
  def __eq__(self, other):
    if(len(self) == len(other)):
      for node in self:
        if other[node.label] == None:
          return False
      return True
    return False

""" Node class is essentially a doubly linked list. Keeps track of the current value,
nodes pointed at the current node, as well as nodes pointing to """
class Node:
  def __init__(self, label):
    self.label = label
    self.leave = Nodeset()
    self.enter = Nodeset()

  def debug(self):
    output = "Node {} ".format(self.label)
    output +=   "links to {}".format(map(lambda x: x.label, self.leave)) if len(self.leave) else ""
    output += " and " if len(self.enter) and len(self.leave)                                else ""
    output += "links from {}".format(map(lambda x: x.label, self.enter)) if len(self.enter) else ""
    output += "\n"
    return output

  def is_bridge(self):
    """ This is a bridge node if it has exactly one node entering and one node leaving """
    return len(self.leave) == 1 and len(self.enter) == 1
 
  def link(self, node):
    """ Creating an edge relationship between two nodes """
    self.enter.add(node)
    node.leave.add(self)

""" Graph class keeps track of all the nodes that exists. Its main function is to handle the
relationships between nodes. """
class Graph:
  def __init__(self):
    self.nodes = {}
    self.nodeset = Nodeset()

  def add_edge(self, src, dst):
    """ Given two nodes, create an edge. If either do not exist in the graph, create them """
    src_node = self.nodeset[src] or Node(src)
    dst_node = self.nodeset[dst] or Node(dst)

    src_node.link(dst_node)

    self.nodeset[src] = src_node
    self.nodeset[dst] = dst_node

  def reduce(self):
    """ Remove nodes that have exactly one input and output edge. Bridge nodes are nodes that
    bridge between nodes that are intersections """
    prev_nodeset = self.nodeset.copy()
    while True:
      nodes_to_remove = set()
      for node in self.nodeset:
        if node.is_bridge():
          # it's like a doubly linked list. Remove the middle node and point
          # enter and leave to each other. And since there's only one element in the
          # nodesets, we can safely assume that's the one we want
          leave = node.leave.pop()
          enter = node.enter.pop()
          leave = None if leave == node else leave  # make sure we're not making a circular loop
          enter = None if enter == node else enter
          if leave != None and leave != enter:
            leave.enter.add(enter)                  # relinking the doubly linked list
            leave.enter.remove(node)                # removing reference to the bridge node we're removing
          if enter != None and leave != enter:
            enter.leave.add(leave)
            enter.leave.remove(node)
          nodes_to_remove.add(node)                 # delegate bridge node removal later, to not affect the for loop
      self.nodeset -= nodes_to_remove
      debug("Deleted nodes: {}".format(map(lambda x: x.label, nodes_to_remove)))
      debug(self)
      if prev_nodeset == self.nodeset:
        break
      prev_nodeset = self.nodeset

  def __str__(self):
    output = ""
    for node in self.nodeset:
      output += node.debug()
    return output.strip()

  def output(self):
    output = ""
    for node in self.nodeset:
      for leave in node.leave:
        output += "{}\t{}\n".format(leave.label, node.label)
    return output.strip()


def main():
  graph = Graph()
  for line in string.split("\n"):
    if len(line.strip()) == 0:
      continue
    (src,dst) = line.split("\t");
    graph.add_edge(src, dst)
  debug("===========")
  debug("Initial graph representation:")
  debug(graph)
  debug("===========")
  debug("After bridging nodes")
  graph.reduce()
  debug("===========")
  debug("Output:")
  print graph.output()

if __name__ == "__main__":
  main()
