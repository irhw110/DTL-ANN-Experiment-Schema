class Node:
    def __init__(self, attribute=None, label=None, vertex=None):
        self.attribute = attribute
        self.label = label
        self.vertex = vertex
        self.children = {}
        self.most_common_label = None
    
    def set_most_common_label(self, most_common_label):
        self.most_common_label = most_common_label
        
    def get_most_common_label(self):
        return self.most_common_label
        
    def setAttribute(self, attribute):
        self.attribute = attribute

    def setLabel(self, label):
        self.label = label
        
    def setVertex(self, vertex):
        self.vertex = vertex
  
    def addChildren(self, attributeValue, node):
        self.children[attributeValue] = node
    
    def getChildren(self):
        return self.children
    
    def getLabel(self):
        return self.label
    
    def getVertex(self):
        return self.vertex

def print_tree(node,depth):
    if node.label is not None: 
        print("    "*(depth+1) +str(node.label))
    else:
        print("    "*depth + "["+ node.attribute +"]")
        for i in node.children:
            print("----"*(depth+1) +str(i))
            print_tree(node.children[i],depth+1)   

def load_file_dtl(parent, depth, file):
    line = file.readline().rstrip()

    while line:
        tabs = line.count('----')

        if tabs < depth:
            break
        else :
            node = Node()
            parsed_line = ''
            vertex = ''

            if depth == 0:
                line = line[1:-1]
                parent.setAttribute(line)

            else:
                if (line[-1] == ']'):
                    parsed_line = line.replace('----', '').split('[')
                    vertex = parsed_line[0].rstrip()
                    attribute = parsed_line[1].strip()[:-1]
                    node.setAttribute(attribute)
                    node.setVertex(vertex)
                    
                else:
                    parsed_line = line.replace('----', '').split(' ' * (depth+1))
                    vertex = parsed_line[0].rstrip()
                    label = parsed_line[1].strip()
                    node.setVertex(vertex)
                    node.setLabel(label)

            parent.children[vertex] = node
            
            line = load_file_dtl(node, depth + 1, file)
    
    return line         

node = Node()
file = open("dtl.txt", "r")
load_file_dtl(node, 0 , file)
print(node.children[''].children['>=2.45'].children['>=1.8'].children['<5.95'].attribute)
# print_tree(node.children[''], 0)
file.close()

# line = "------------<5.95    2"
# print(line.replace('----', '').split(' '*4)[1])