#!/usr/bin/python
#
# Implementation of Inferring Genotype from a Pedigree problem
# http://rosalind.info/problems/mend/
#
# Install:
# ETE http://pythonhosted.org/ete2/install/index.html
#
# Usage:
# python rosalind_mend.py dataset_file_in_newick_format
#
# Sample Dataset file:
# ((((Aa,aa),(Aa,Aa)),((aa,aa),(aa,AA))),Aa);
# Sample Output:
# 0.156 0.5 0.344
#

from ete2 import Tree
import sys



def compute_node(n1,n2):
    return [n1[0] * n2[0] + n1[1] * n2[1] / 4 + n1[0] * n2[1] / 2 + n1[1] * n2[0] / 2,
    n1[0] * n2[2] + n1[2] * n2[0] + n1[1] * n2[1] / 2 + n1[0] * n2[1] / 2 + n1[1] * n2[0] / 2 + n1[2] * n2[1] / 2 + n1[1] * n2[2] / 2,
    n1[2] * n2[2] + n1[1] * n2[1] / 4 + n1[2] * n2[1] / 2 + n1[1] * n2[2] / 2]

if __name__ == '__main__':

# http://pythonhosted.org/ete2/tutorial/tutorial_trees.html#reading-newick-trees

    t = Tree(sys.argv[-1])

# http://pythonhosted.org/ete2/tutorial/tutorial_trees.html#traversing-browsing-trees

    for node in t.traverse("postorder"):
        if node.is_leaf():
            if node.name in ('AA','Aa','aa'):
	        if node.name == 'AA':  
                    node.add_feature("data",[1.0, 0.0, 0.0])
                elif node.name == 'Aa':
                    node.add_feature("data",[0.0, 1.0, 0.0])
                elif node.name == 'aa':
                    node.add_feature("data",[0.0, 0.0, 1.0])
            else:
                raise Exception("Wrong node name, not AA,Aa,aa", node)
        else:
            node.data=compute_node(node.children[0].data,node.children[1].data)
# result at root node
            if node.is_root():
                print round(node.data[0],3),round(node.data[1],3),round(node.data[2],3)


