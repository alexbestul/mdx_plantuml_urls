import plantuml
import markdown
from markdown.extensions import Extension
from markdown.util import etree

class PlantUmlUrlExtension(Extension):
    def extendMarkdown(self, md, md_globals):
        blockprocessor = PlantUmlBlockProcessor(md.parser)
        md.parser.blockprocessors.add('markdown_plantuml_img', blockprocessor, '>code')

class PlantUmlBlockProcessor(markdown.blockprocessors.BlockProcessor):

    def test(self, parent, block):
        return block.startswith('@startuml')

    def run(self, parent, blocks):
        text = blocks.pop(0)

        while blocks:
            text += blocks.pop(0)

        plant = plantuml.PlantUML('http://plantuml/planuml/')
        imageurl = plant.get_url(text)

        etree.SubElement(parent, 'img', src=imageurl)
