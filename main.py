#!/usr/bin/env python
import sys

def debug(str):
  print str

## verify the input
try:
  string = open(sys.argv[1]).read()
except:
  print "Cannot open the file!"
  print "Usage: %s filename" % sys.argv[0]
  sys.exit(1)

class Nodeset(set):
  def add(self, node):
    if node != self:
      return super(Nodeset, self).add(node)
  def __getitem__(self, label):
    for node in self:
      if node.label == label:
        return node
  def __setitem__(self, label, node):
    return super(Nodeset, self).add(node)


class Node:
  label = ""
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
    return len(self.leave) == 1 and len(self.enter) == 1
 
  def link(self, node):
    self.enter.add(node)
    node.leave.add(self)


class Graph:
  def __init__(self):
    self.nodes = {}

  def add_edge(self, src, dst):
    src_node = self.nodes[src] if src in self.nodes else Node(src)
    dst_node = self.nodes[dst] if dst in self.nodes else Node(dst)

    src_node.link(dst_node)

    self.nodes[src] = src_node
    self.nodes[dst] = dst_node

  def bridge_nodes(self):
    for node in self.nodes.values():
      if node.is_bridge():
        # we can assume there's only one element to pop
        leave = node.leave.pop()
        enter = node.enter.pop()
        enter.leave.add(leave)
        leave.enter.add(enter)
        print "deleted " + node.label
        del self.nodes[node.label]
        del node
    # clean up
    for node in self.nodes.values():
      # delete loops
      if node in node.enter:
        node.enter.remove(node)
      if node in node.leave:
        node.leave.remove(node)



  def __str__(self):
    output = ""
    for node in self.nodes.values():
      output += node.debug()
    #  output += str(self.nodes[node])
    return output


def main():
  graph = Graph()
  for line in string.split("\n"):
    if len(line.strip()) == 0:
      continue
    (src,dst) = line.split("\t");
    graph.add_edge(src, dst)
  print graph
  graph.bridge_nodes()
  print graph

if __name__ == "__main__":
  main()
