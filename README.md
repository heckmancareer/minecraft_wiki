# Minecraft Wiki

## generate-html.py
This script loads the html file found at `template/template.html` and the json file `item-list.json`, goes through the html file and replaces keywords with their json counterpart ex. `{{minecraft_title}}` -> `Stable Ender Pearl`

Then it writes the new, filled html file into the `generated-html` folder to be committed back into the repo.
