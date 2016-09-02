import mock
import pytest
from pytest_mock import mocker
import plantuml
from markdown_plantuml_img import PlantUmlUrlExtension
import markdown
import textwrap

def test_happypath(mocker):
    # Given the simplest possible PlantUML input,
    # show that the URL generator is called, and
    # that the URL it returns is inserted into the
    # resulting document.  With this behavior
    # established, other tests may focus on asserting
    # that PlantUML.get_url is passed the correct text.
    #
    # This test does rely on the default PlantUML server
    # URL, as provided by the plantuml package.  If that
    # default ever changes, the test will fail.

    # Arrange
    #mocker.patch('plantuml.PlantUML.get_url')
    #plantuml.PlantUML.get_url.retur_value = 'xxbarxx'

    text = textwrap.dedent('''\
    @startuml
    @enduml
    ''')

    # Act
    output = markdown.markdown(text, extensions=[PlantUmlUrlExtension()])

    #Assert
    #plantuml.PlantUML.get_url.assert_called_with(text)
    assert output == '<img src="http://www.plantuml.com/plantuml/img/SoWkIImgAStDuN98pKi1qG00" />'
