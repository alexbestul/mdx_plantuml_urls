import plantuml
import markdown
from markdown.extensions import Extension
from markdown.util import etree

def makeExtension(*args, **kwargs):
    return PlantUmlUrlExtension(*args, **kwargs)

class PlantUmlUrlExtension(Extension):

    def __init__(self, *args, **kwargs):
        self.config = {
            'planturl': ['', 'Base URL of the PlantUML server.'],
            'default_skinparam': ['', 'Skinparam to be applied to all diagrams.']
        }

        super(PlantUmlUrlExtension, self).__init__(*args, **kwargs)

    def extendMarkdown(self, md, md_globals):
        blockprocessor = self.createBlockprocessor(md)
        md.parser.blockprocessors.add('markdown_plantuml_img', blockprocessor, '>code')

    def createBlockprocessor(self, md):
        blockprocessor = PlantUmlBlockProcessor(md.parser)
        blockprocessor.planturl = self.getConfig('planturl')
        blockprocessor.skinparam = self.getConfig('default_skinparam')

        return blockprocessor

class PlantUmlBlockProcessor(markdown.blockprocessors.BlockProcessor):

    def __init__(self, *args, **kwargs):
        self.planturl = ''
        self.skinparam = ''
        super(PlantUmlBlockProcessor, self).__init__(*args, **kwargs)

    def test(self, parent, block):
        return block.startswith('@startuml')

    def run(self, parent, blocks):
        text = self.collect_blocks(blocks)

        plant = self.get_plant_instance()
        imageurl = plant.get_url(text)

        etree.SubElement(parent, 'img', src=imageurl)

    def get_plant_instance(self):
        if self.planturl:
            return plantuml.PlantUML(self.planturl)
        else:
            return plantuml.PlantUML()

    def collect_blocks(self, blocks):
        current_block = blocks.pop(0)
        text = current_block

        if (self.skinparam):
            text += '\n' + self.skinparam

        while blocks and not current_block.startswith('@enduml'):
            current_block = blocks.pop(0)
            text += '\n' + current_block

        return text
