import HTMLparser
# you can accuire an html file throw urlopen
file = open('info.php', 'r', encoding='utf-8')

# parser is the url handler
parser = HTMLparser.HTMLparser(file)

# build the dom tree
parser.buildTree()

# from root dom 'html' and print the content of each tag
parser.traverseTree(parser.root)

# traverse the dom tree throw tag name
parser.attrTraverse('div', parser.root)

# find every tag whose attribute is 'class' and the content of attribute is 'banner-content'
parser.findByAttr('class', 'banner-content', parser.root)
