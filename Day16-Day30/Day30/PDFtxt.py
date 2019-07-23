#PDF文档转TXT文档

from pdfminer.pdfinterp import PDFPageInterpreter,PDFResourceManager
from pdfminer.converter import TextConverter,PDFPageAggregator
from pdfminer.layout import LAParams
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfdevice import PDFDevice
from pdfminer.pdfpage import PDFPage


fp = open('exam.pdf','rb') # 获取pdf文档


parser = PDFParser(fp)# 创建一个与文档相关的解释器

'''pdf文档的对象，与解释器连接起来'''
doc = PDFDocument(parser=parser)
parser.set_document(doc=doc)

'''如果是加密pdf，则输入密码
    doc._initialize_password() '''


resource = PDFResourceManager()# 创建pdf资源管理器


laparam=LAParams()# 参数分析器

device = PDFPageAggregator(resource,laparams=laparam)# 创建一个聚合器

interpreter = PDFPageInterpreter(resource,device)# 创建pdf页面解释器

# 获取页面的集合
for page in PDFPage.get_pages(fp):
    interpreter.process_page(page)# 使用页面解释器来读取
    layout = device.get_result()# 使用聚合器来获取内容
    for out in layout:
        if hasattr(out,'get_text'):
            print(out.get_text())
            
            # 写入txt文件
            fw = open('exam.txt','a')
            fw.write(out.get_text())
