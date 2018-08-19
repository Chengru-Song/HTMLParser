import TreeNode
import re
specialNames = ['br', 'hr', 'area', 'base', 'img',
                'input', 'link', 'meta', 'basefont',
                'param', 'col', 'frame', 'embed', 'keygen', 'source']

class HTMLparser(object):
    def __init__(self, html):
        '''html is input html doc'''
        self.html = html
        self.root = TreeNode.Node()
        self.curr = self.root
        self.tagPattern = re.compile(r'(?!<!)</?[^>]+>')
        self.attrPattern = re.compile(r'\w+=\".*\"')
        self.attrListPattern = re.compile(r'(?<=\")\s')
        self.attrNamePattern = re.compile(r'\w+(?=\=\")')
        self.attrContentPattern = re.compile(r'(?<=\=)\".*\"')
        self.contentPattern = re.compile(r'(?<=>).*(?=</)')
        self.startPattern = re.compile(r'<\w+')
        self.closePattern = re.compile(r'</\w+')
        self.namePattern = re.compile(r'(?<=<)\w+')
        self.closeNamePattern = re.compile(r'(?<=</)\w+')

    def addContentToAllParent(self, line, node):
        while node.parent != self.root:
            node = node.parent
            node.appendContent(line)


    def isSpecialNames(self, name):
        for n in specialNames:
            if name == n:
                return True
        return False

    def findStartTag(self, name):
        node = self.curr

        while name != node.name:
            node = node.parent
        return node
    def getAttr(self, tag):
        result = []
        attr = re.findall(self.attrPattern, tag)
        if attr:
            attrlist = re.split(self.attrListPattern, attr[0])
            for e in attrlist:
                attrname = re.findall(self.attrNamePattern, e)
                attrcontent = re.findall(self.attrContentPattern, e)
                length = len(attrname)
                for i in range(0, length):
                    result.append(attrname[i])
                    result.append(attrcontent[i])

        return result


    def buildTree(self):
        '''Build Dom Tree'''
        for eachLine in self.html:
            tags = re.findall(self.tagPattern, eachLine)
            if tags:
                for tag in tags:
                    # if tag:
                    #     print(tag)
                    start = re.match(self.startPattern, tag)
                    close = re.match(self.closePattern, tag)
                    if start:
                        # fill the content of the node
                        names = re.findall(self.namePattern, eachLine)
                        for name in names:
                            node = TreeNode.Node()
                            attr = self.getAttr(tag)
                            node.appendAttrList(attr)
                            node.name = name
                            node.appendAttrList(attr)
                            # judge if the tag is a special node, if the answer is yes
                            # ignore content part and the tag must be a child node
                            # if the tag is not a special node, change the node to curr node
                            if self.isSpecialNames(name):
                                node.parent = self.curr
                                self.curr.appendChild(node)
                                self.addContentToAllParent(eachLine, node)


                            else:
                                content = re.findall(self.contentPattern, eachLine)
                                if content:
                                    node.appendContent(content[0])
                                node.parent = self.curr
                                self.curr.appendChild(node)
                                self.curr = node

                    #   if the node is a close node, search all the way to top
                    # to find its start tag and close it all
                    if close:

                        names = re.findall(self.closeNamePattern, eachLine)
                        for name in names:
                            self.curr = self.findStartTag(name).parent
                            self.curr.appendContent(eachLine)


    def traverseTree(self, node):
        print(node.content)
        if node.child:
            for child in node.child:
                self.traverseTree(child)

    def nameTraverse(self, name, node):
        if name == node.name:
            print(node.content)
        if node.child:
            for child in node.child:
                self.nameTraverse(name, child)

    def attrTraverse(self, name, node):
        if name == node.name:
            print(node.attr)
        if node.child:
            for child in node.child:
                self.attrTraverse(name, child)

    def findByAttr(self, attrname, attrcontent, node):
        if attrname in node.attr:
            if attrcontent == node.attr[attrname]:
                print(node.content)
        if node.child:
            for child in node.child:
                self.findByAttr(attrname, attrcontent, child)