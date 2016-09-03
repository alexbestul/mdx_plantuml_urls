import pytest
from markdown_plantuml_img import PlantUmlUrlExtension
import markdown

def test_load_extension_as_object():
    markdown.markdown('', extensions=[PlantUmlUrlExtension()])

def test_load_extension_using_string():
    markdown.markdown('', extensions=['markdown_plantuml_img'])
