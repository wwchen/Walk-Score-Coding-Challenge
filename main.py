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

class Node:
  def __init__(self, label):
    self.label = label
    self.goin = []
    self.goout = []

  def __str__(self):
    output = "Node {} ".format(self.label)
    output +=    "links from {} ".format(map(lambda x: x.label, self.goin))  if len(self.goin)  > 0 else ""
    output += "and links to {}\n".format(map(lambda x: x.label, self.goout)) if len(self.goout) > 0 else ""
    return output

  def __repr__(self):
    return self.__str__()

  def link(self, node):
    self.goin.append(node)
    node.goout.append(self)

class Edge:
  def __init__(self, src, dst):
    print "yes"
    



class Graph:
  def __init__(self):
    self.nodes = {}

  def add_edge(self, src, dst):
    src_node = self.nodes[src] if src in self.nodes else Node(src)
    dst_node = self.nodes[dst] if dst in self.nodes else Node(dst)

    src_node.link(dst_node)

    self.nodes[src] = src_node
    self.nodes[dst] = dst_node

  def __str__(self):
    output = ""
    for node in self.nodes:
      output += str(self.nodes[node])
    return output


graph = Graph()
for line in string.split("\n"):
  if len(line.strip()) == 0:
    continue
  (src,dst) = line.split("\t");
  graph.add_edge(src, dst)
print graph
