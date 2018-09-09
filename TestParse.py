# 
import os
import xml.etree.ElementTree as et

from processor import converter as cvt

base_path = os.path.dirname(os.path.realpath(__file__))
xml_file = os.path.join(base_path,"res/OneChhaPage.xml")

tree = et.parse(xml_file)
root = tree.getroot()


ns = {'office':'urn:oasis:names:tc:opendocument:xmlns:office:1.0',
      'draw':'urn:oasis:names:tc:opendocument:xmlns:drawing:1.0',
      'text':'urn:oasis:names:tc:opendocument:xmlns:text:1.0',
      'table':'urn:oasis:names:tc:opendocument:xmlns:table:1.0',
      'style':'urn:oasis:names:tc:opendocument:xmlns:style:1.0'}


lw = []
for body in root.findall('office:body',ns):
    for drawing in body.findall('office:drawing',ns):
        for page in drawing.findall('draw:page',ns):
            for frame in page.findall('draw:frame',ns):
                for text_box in frame.findall('draw:text-box',ns):
                    for p in text_box.findall('text:p',ns):
                        for span in p.findall('text:span',ns):
                            for s in span.findall('text:s',ns):

                            atrb = span.attrib
                            nst = '{'+ns['text']+'}style-name'
                            style = atrb[nst]
                            #print(atrb)
                            tp = (style,span.text)
                            #print(style, ' ',span.text,end='\n')
                            lw.append(tp)




def mord(wrd):
    wr = ' '
    if wrd != None:
        wr = '{}'.format(ord(wrd[0]))
    return wr



def show_info():
    for ft,word in lw:
        #ft = lw[i][0]
        #word = lw[i][1]
        cvcl = cvt.Converter()
        c_word = word
        if ft != 'T8':
            c_word = cvcl.convert_word(word)

        print('{} :: {}  || {} || {}'.format(ft,word,c_word,mord(word)))

def write_file():
    with open('res/Grest.txt','w') as ofl:
        for i in range(len(lw)):
            ft = lw[i][0]
            word = lw[i][1]
            cvcl = cvt.Converter()
            c_word = word
            if ft != 'T8':
                c_word = cvcl.convert_word(word)


            # T5 147 is chandrabindu
            # T5 151 is -

            if ft == 'T5':
                if len(word) == 1:
                    if ord(word) == 151:
                        ofl.write('\n')
                        print('\n')

            print('{}'.format(c_word),end='')
            ofl.write('{}'.format(c_word))


show_info()
