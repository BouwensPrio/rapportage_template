from docxtpl import DocxTemplate, InlineImage
from docx.shared import Mm
from basic_structures import get_report
from typing import List, Dict
import sys
import argparse
import logging
import os
import re

def configure_logging():
    pass

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("template_path")
    args = parser.parse_args()
    return args

def extract_version(s: str) -> str | None:
    """
    Search `s` for a version like v2, v2.1, v3.0, v5, etc.
    If found, returns the full match (e.g. 'v2.1'), otherwise None.
    """
    pattern = re.compile(r'\[(v\d+(?:\.\d+)?)\]')
    m = pattern.search(s)
    print(f"found {m} in {s}")
    return m.group(1) if m else None


def get_rendering_source():
    SOURCE = get_report()
    # print(SOURCE)
    return SOURCE

def add_version_to_source(rendering_source: List[dict], args):
    version_string = extract_version(args)
    if version_string:
        for report in rendering_source:
            report.update({'versie':version_string})
                    
    return rendering_source

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
    if args.template_path:
        add_version_to_source(rendering_source, args.template_path)
    fill_template(args.template_path,rendering_source)    
    pass


if __name__ == "__main__":
    main()