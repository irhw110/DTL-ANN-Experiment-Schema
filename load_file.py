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
file = open("text_dtl.txt", "r")
load_file_dtl(node, 0 , file)
print(node.children[''].children['>=2.45'].children['>=1.8'].children['<5.95'].attribute)
# print_tree(node.children[''], 0)
file.close()

class Neuron:
    def __init__(self, out=None, w=None, is_used=None, error=None):
        self.out = out
        self.w = []
        self.is_used = is_used
        self.error = 0
        self.deltaW = []
        
    def set_out(self, out):
        self.out = out
        
    def get_out(self):
        return self.out
    
    def add_deltaW(self, value):
        self.deltaW.append(value)
        
    def get_deltaW(self, index):
        return self.deltaW[index]
    
    def get_arrdW(self):
        return self.deltaW
    
    def set_deltaW(self, index, value):
        self.deltaW[index] = value
        
    def add_w(self, value):
        self.w.append(value)
        
    def set_w(self, index, value):
        self.w[index] = value
    
    def get_w(self, index):
        return self.w[index]
    
    def get_arrW(self):
        return self.w
    
    def set_is_used(self, is_used):
        self.is_used = is_used
        
    def get_is_used(self):
        return self.is_used
    
    def set_error(self, error):
        self.error = error
    
    def get_error(self):
        return self.error

def printMatrixMLP(matrix):
    for i in range(len(matrix)):
        temp_matrix_out = []
        for j in range(len(matrix[i])):
            temp_matrix_out.append(matrix[i][j].get_error())
        print(temp_matrix_out)

def load_file_ann(file):
    neurons = file.read().split("\n")[:-1]

    rows = []
    columns = []

    curr_row = 0

    for neuron in neurons:
        neuron_pos = neuron.split('=')[0].split(',')
        if int(neuron_pos[0]) != curr_row:
            rows.append(columns)
            columns = []
            curr_row += 1

        new_neuron = Neuron()
        neuron_elements = neuron.split('=')[1].rstrip().split('|')
        weights = neuron_elements[0]
        delta_weights = neuron_elements[1]
        out = neuron_elements[2]
        err = neuron_elements[3]

        if len(weights) > 2:
            parsed_weights = weights[1:-1].split(',')
            for weight in parsed_weights:
                new_neuron.add_w(float(weight.strip()))
        
        if len(delta_weights) > 2:
            parsed_delta_weights = delta_weights[1:-1].split(',')
            for delta_weight in parsed_delta_weights:
                new_neuron.add_deltaW(float(delta_weight.strip()))

        new_neuron.set_out(float(out))
        new_neuron.set_error(float(err))

        columns.append(new_neuron)

    max_col_len = max([len(row) for row in rows])
    for row in rows:
        if len(row) < max_col_len:
            for i in range(max_col_len-len(row)):
                row.append(Neuron())

    return rows

file = open("text_ann.txt", "r")
rows = load_file_ann(file)
printMatrixMLP(rows)
file.close()