#!/usr/bin/python3

import constants
import os
import re
import json

# Create the output folder if it does not already exist
def generate_output_folder() -> None:
    if not os.path.isdir(constants.OUTPUT_DIR):
        os.mkdir(constants.OUTPUT_DIR)

def generate_image_tag(output, image_paths) -> str:
    print("Generating image tags...")
    for image_path in image_paths:
        re.sub(constants.IMAGE_REPLACE, image_path, output)
    return output

# Main Function
def main() -> None:
    # Generate an SVG badge with summary statistics
    with open(constants.TEMPLATE_DIR+"/template.html", "r") as f:
        output = f.read()

    with open("item-list.json", "r") as j:
        item_list_json = j.read()
    item_list = json.loads(item_list_json)

    generate_output_folder()

    for item in item_list:
        output = re.sub(constants.TITLE_REPLACE, item['title'], output)
        output = re.sub(constants.DESC_REPLACE, item['description'], output)

        output = generate_image_tag(output, item['image_paths'])
        with open(constants.OUTPUT_DIR+"/generated.html", "w") as f:
            f.write(output)

if __name__ == "__main__":
    main()
