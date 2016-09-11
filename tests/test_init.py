import pytest
from mdx_plantuml_urls import PlantUmlUrlExtension
import markdown

def test_load_extension_as_object():
    markdown.markdown('', extensions=[PlantUmlUrlExtension()])

def test_load_extension_using_string():
    markdown.markdown('', extensions=['plantuml_urls'])

def test_load_extension_using_short_string():
        markdown.markdown('', extensions=['mdx_plantuml_urls'])

def test_config_server_url():
    # Arrange
    server_url = 'http://my_plant_server.localhost.com/plantuml/'

    # Act
    extension = PlantUmlUrlExtension(planturl=server_url)

    # Assert
    assert server_url == extension.getConfigs()['planturl']
