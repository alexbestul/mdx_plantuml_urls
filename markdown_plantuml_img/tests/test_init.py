import pytest
from markdown_plantuml_img import PlantUmlUrlExtension
import markdown

def test_load_extension_as_object():
    markdown.markdown('', extensions=[PlantUmlUrlExtension()])

def test_load_extension_using_string():
    markdown.markdown('', extensions=['markdown_plantuml_img'])

def test_config_server_url():
    # Arrange
    server_url = 'http://my_plant_server.localhost.com/plantuml/'

    # Act
    extension = PlantUmlUrlExtension(planturl=server_url)

    # Assert
    assert server_url == extension.getConfigs()['planturl']
