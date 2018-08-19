class Node(object):
    def __init__(self):
        '''using child pointers to represent the tree structure'''
        self.child = []
        self.parent = object
        self.attr = {}
        self.content = ''
        self.name = ''

    def buildNode(self, child, parent, attr, content, name):
    #     attr is a list containing all attribute
        self.appendChild(child)
        self.parent = parent
        self.appendAttrList(attr)
        self.appendContent(content)
        self.name = name

    def appendChild(self, anotherNode):
        self.child.append(anotherNode)

    def appendAttr(self, key, attr):
        self.attr[key] = attr

    def appendContent(self, line):
        self.content += line

    def appendAttrList(self, attr):
        attrLength = len(attr)
        for i in range(0, attrLength - 1):
            self.appendAttr(attr[i], attr[i+1])