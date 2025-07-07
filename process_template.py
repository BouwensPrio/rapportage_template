from docxtpl import DocxTemplate, InlineImage
from docx.shared import Mm
from basic_structures import get_report
import sys
import argparse
import logging
import os

def configure_logging():
    pass

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("template_path")
    args = parser.parse_args()
    return args

def get_rendering_source():
    SOURCE = get_report()
    print(SOURCE)
    return SOURCE

def fill_template(template_path,rendering_source):
    for source in rendering_source:
        try:
            with open(template_path,"r") as template:
                pass
        except Exception as e:
            print(f'failed at loading template {e}')
        doc = DocxTemplate(template_path)
        doc.render(source)
        doc.save(os.path.join(os.getcwd(),'Sjablonen',source["bestandsnaam"]))
        pass

def main():
    args = parse_arguments()
    rendering_source = get_rendering_source()
    fill_template(args.template_path,rendering_source)    
    pass


if __name__ == "__main__":
    main()