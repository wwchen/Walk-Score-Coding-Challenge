Welcome to the Walk Score coding challenge!
===========================================

The files in the input directory represent directed graphs.  Each line
contains two tab-separated node IDs, and defines an edge.  We want to
eliminate nodes that have exactly one input and one output edge, by connecting
their neighbors directly.

The output directory contains correct output for the first few graphs, which
may answer some of your questions about *ahem* edge cases.  Your challenge is
to write a program that can produce correct output for the rest!

Quick Start
===========
- Make sure you have Python 2.7.5+, check with `python --version`
- Clone the repo: `git clone git@github.com:wwchen/Walk-Score-Coding-Challenge.git`
- Run the main executable, `./main.py <filename>`, where the filename is the location of the input file
- Alternatively, you can run all the sample input and outputs with `./test.sh`
- Debug output can be turned on. Simply switch `DEBUG` variable to `True` in `main.py`

Credit
======
Python documentation and StackOverflow were referenced quite a bit during the coding. I had a hard time
adjusting from Ruby to Python. A lot of messing up because of similar but different syntax. A lot of code
refactoring went into choosing the right data structure to represent nodes in the graph.

Sample output
=============
    ===================
    Test #0: ./main.py input/0
    A	C
    Expected output:
    A	C
    
    ===================
    Test #1: ./main.py input/1
    A	C
    Expected output:
    A	C
    
    ===================
    Test #2: ./main.py input/2
    
    Expected output:
    
    ===================
    Test #3: ./main.py input/3
    A	B
    B	D
    B	C
    ===================
    Test #4: ./main.py input/4
    A	C
    B	C
    C	D
    ===================
    Test #5: ./main.py input/5
    E	F
    E	G
    G	H
    G	B
    B	E


    ===================
    Test #0: ./main.py input/0
    DEBUG: ===========
    DEBUG: Initial graph representation:
    DEBUG: Node B links to ['A'] and links from ['C']
    DEBUG: Node A links from ['B']
    DEBUG: Node C links to ['B']
    DEBUG: ===========
    DEBUG: After bridging nodes
    DEBUG: Deleted nodes: ['B']
    DEBUG: Node A links from ['C']
    DEBUG: Node C links to ['A']
    DEBUG: ===========
    DEBUG: Output:
    A	C
    Expected output:
    A	C
    
    ===================
    Test #1: ./main.py input/1
    DEBUG: ===========
    DEBUG: Initial graph representation:
    DEBUG: Node B links to ['A'] and links from ['C']
    DEBUG: Node D links to ['A'] and links from ['C']
    DEBUG: Node A links from ['B', 'D']
    DEBUG: Node C links to ['B', 'D']
    DEBUG: ===========
    DEBUG: After bridging nodes
    DEBUG: Deleted nodes: ['B', 'D']
    DEBUG: Node C links to ['A']
    DEBUG: Node A links from ['C']
    DEBUG: ===========
    DEBUG: Output:
    A	C
    Expected output:
    A	C
    
    ===================
    Test #2: ./main.py input/2
    DEBUG: ===========
    DEBUG: Initial graph representation:
    DEBUG: Node B links to ['A'] and links from ['C']
    DEBUG: Node D links to ['C'] and links from ['A']
    DEBUG: Node A links to ['D'] and links from ['B']
    DEBUG: Node C links to ['B'] and links from ['D']
    DEBUG: ===========
    DEBUG: After bridging nodes
    DEBUG: Deleted nodes: ['B', 'D', 'A', 'C']
    DEBUG: 
    DEBUG: ===========
    DEBUG: Output:
    
    Expected output:
    
    ===================
    Test #3: ./main.py input/3
    DEBUG: ===========
    DEBUG: Initial graph representation:
    DEBUG: Node B links to ['A'] and links from ['D', 'C']
    DEBUG: Node D links to ['B']
    DEBUG: Node A links from ['B']
    DEBUG: Node C links to ['B']
    DEBUG: ===========
    DEBUG: After bridging nodes
    DEBUG: Deleted nodes: []
    DEBUG: Node B links to ['A'] and links from ['D', 'C']
    DEBUG: Node D links to ['B']
    DEBUG: Node A links from ['B']
    DEBUG: Node C links to ['B']
    DEBUG: ===========
    DEBUG: Output:
    A	B
    B	D
    B	C
    ===================
    Test #4: ./main.py input/4
    DEBUG: ===========
    DEBUG: Initial graph representation:
    DEBUG: Node C links to ['A', 'B'] and links from ['D']
    DEBUG: Node D links to ['C']
    DEBUG: Node A links from ['C']
    DEBUG: Node B links from ['C']
    DEBUG: ===========
    DEBUG: After bridging nodes
    DEBUG: Deleted nodes: []
    DEBUG: Node C links to ['A', 'B'] and links from ['D']
    DEBUG: Node D links to ['C']
    DEBUG: Node A links from ['C']
    DEBUG: Node B links from ['C']
    DEBUG: ===========
    DEBUG: Output:
    A	C
    B	C
    C	D
    ===================
    Test #5: ./main.py input/5
    DEBUG: ===========
    DEBUG: Initial graph representation:
    DEBUG: Node F links to ['E']
    DEBUG: Node G links to ['E'] and links from ['H', 'A']
    DEBUG: Node A links to ['G'] and links from ['B']
    DEBUG: Node H links to ['G']
    DEBUG: Node B links to ['A'] and links from ['D', 'C']
    DEBUG: Node C links to ['B'] and links from ['D']
    DEBUG: Node D links to ['B', 'C'] and links from ['E']
    DEBUG: Node E links to ['D'] and links from ['G', 'F']
    DEBUG: ===========
    DEBUG: After bridging nodes
    DEBUG: Deleted nodes: ['D', 'A', 'C']
    DEBUG: Node F links to ['E']
    DEBUG: Node G links to ['E'] and links from ['B', 'H']
    DEBUG: Node H links to ['G']
    DEBUG: Node B links to ['G'] and links from ['E']
    DEBUG: Node E links to ['B'] and links from ['G', 'F']
    DEBUG: ===========
    DEBUG: Output:
    E	F
    E	G
    G	H
    G	B
    B	E
