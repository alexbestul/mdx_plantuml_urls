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
        text = self.collect_blocks(blocks)

        plant = plantuml.PlantUML()
        imageurl = plant.get_url(text)

        etree.SubElement(parent, 'img', src=imageurl)

    def collect_blocks(self, blocks):
        current_block = blocks.pop(0)
        text = current_block

        while blocks and not current_block.startswith('@enduml'):
            current_block = blocks.pop(0)
            text += '\n' + current_block

        return text
