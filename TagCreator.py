'''
Created on 2017/09/19

@author: Abe
'''

import re
import os
import csv

class Tag:
    def __init__(self, attr = ''):
        self.attr = attr
        self.elems = []

    def add(self, elem):
        if isinstance(elem, Tag):
            self.bra1 += '\n'
            self.bra2 = '\n' + self.bra2
        else:
            self.bra1 = '    ' + self.bra1
            self.bra2 += '\n'
        self.elems.append(elem);
        return self

    def to_string(self):
        result_str = self.bra1.replace('%name%', self.attr)
        for elem in self.elems:
            result_str += elem.to_string()
        result_str += self.bra2
        return re.sub('(\n)+', '\n', result_str)
    
    def __iter__(self):
        return iter(self.elems)
    
class CollectionTag(Tag):
    BRACKET1 = '<Collection name = %name%>'
    BRACKET2= '</Collection>'
    
    def __init__(self, attr):
        super(CollectionTag, self).__init__(attr)
        self.bra1 = CollectionTag.BRACKET1
        self.bra2 = CollectionTag.BRACKET2
    
class StringTag(Tag):
    BRACKET1 = '<String name = %name%>'
    BRACKET2= '</String>'
    
    def __init__(self, attr):
        super(StringTag, self).__init__(attr)
        self.bra1 = StringTag.BRACKET1
        self.bra2 = StringTag.BRACKET2

class Value:
    def __init__(self, val):
        self.val = val

    def to_string(self):
        return str(self.val)
    
#ファイルを格納するディレクトリ
cur_dir = os.path.dirname(os.path.abspath(__file__))
    
def read_csv():
    list = []
    with open(cur_dir + '\\bbb.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            list.append(row)
    return list
#メイン関数
if __name__ == '__main__':
    rows = read_csv()
    num = 100000
    for row in rows:
        num += 1
        root_tag = CollectionTag(str(num))
        tag1 = StringTag(attr = 'id')
        tag1.add(Value(row[0]))
        tag2 = StringTag(attr = '49')
        tag2.add(Value('1'))
        root_tag.add(tag1)
        root_tag.add(tag2)
        print (root_tag.to_string())
    
