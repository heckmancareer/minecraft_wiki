#!/usr/bin/python3

import constants
import os
import re
import json
from bs4 import BeautifulSoup

# Create the output folder if it does not already exist
def create_output_folder() -> None:
    if not os.path.isdir(constants.OUTPUT_DIR):
        os.mkdir(constants.OUTPUT_DIR)

def replace_images(output, image_paths) -> str:
    print("Generating image tags...")
    for image_path in image_paths:
        re.sub(constants.IMAGE_REPLACE, image_path, output)
    return output

def construct_sidebar(item_list_json) -> None:
    with open("../" + constants.TEMPLATE_DIR+"/sidebar.html", "r") as sidebar_file: 
        soup = BeautifulSoup(sidebar_file, 'html.parser')
        item_list = json.loads(item_list_json)
        item_headers = soup.find_all("div", class_="sidebar-header-item")

        for item in item_list:
            print(item['category'])
            for header in item_headers:
                if item['category'] == header.text.strip():
                    newtag = BeautifulSoup('<div class="sidebar-line-item"></div>', 'html.parser')
                    itemlink = BeautifulSoup('<a href="./' + item['title'] + '.html"></a>', 'html.parser')
                    itemlink.a.append(item['title'])
                    newtag.div.append(itemlink)
                    headeritemidentifier = item['category'].lower() + "-header"
                    soup.find("div", {"id": headeritemidentifier}).insert_after(newtag)

        with open("output1.html", "w") as file:
            soup.prettify()
            file.write(str(soup))
    return

# Main Function
def main() -> None:
    with open("../"+constants.TEMPLATE_DIR+"/template.html", "r") as template_file:
        template = template_file.read()
        
        with open("../item-list.json", "r") as json_file:
            item_list_json = json_file.read()
        item_list = json.loads(item_list_json)

        construct_sidebar(item_list_json)
        create_output_folder()

        for item in item_list:
            output = str(template)
            output = re.sub(constants.TITLE_REPLACE, item['title'], output)
            output = re.sub(constants.DESC_REPLACE, item['description'], output)

            output = replace_images(output, item['image_paths'])
            with open(constants.OUTPUT_DIR+"/"+item['title'] + ".html", "w") as output_file:
                output_file.write(output)

if __name__ == "__main__":
    main()
