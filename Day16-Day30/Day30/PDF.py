# 获取在PDF上的文字（coding: utf-8）


from wand.image import Image
from PIL import Image as PI
import pyocr
import pyocr.builders
import io
import sys


def main():
    tools = pyocr.get_available_tools()
    if len(tools) == 0:
        print("No OCR tool found")
        sys.exit(1)
    tool = tools[0]
    print("Will use tool '%s'" % (tool.get_name()))

    langs = tool.get_available_languages()
    print("Available languages: %s" % ", ".join(langs))
    lang = langs[0]
    print("Will use lang '%s'" % (lang))

    req_image = []
    final_text = []

    image_pdf = Image(filename="./pdf_file/stackoverflow.pdf", resolution=400)
    image_jpeg = image_pdf.convert('jpeg')
    image_jpeg.save(filename='./pdf2img/stackoverflow.jpeg')
    for img in image_jpeg.sequence:
        img_page = Image(image=img)
        req_image.append(img_page.make_blob('jpeg'))
    for img in req_image:
        txt = tool.image_to_string(
            PI.open(io.BytesIO(img)),
            lang=lang,
            builder=pyocr.builders.TextBuilder()
        )
        final_text.append(txt)
    print(final_text)
    # for text in final_text:
    #     print(text)


if __name__ == '__main__':
    main()
