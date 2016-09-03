import pytest
from markdown_plantuml_img import PlantUmlUrlExtension
import markdown
import textwrap

def test_happypath():
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
    text = textwrap.dedent('''\
        @startuml
        @enduml
    ''')

    # Act
    output = markdown.markdown(text, extensions=[PlantUmlUrlExtension()])

    #Assert
    assert output == '<img src="http://www.plantuml.com/plantuml/img/SoWkIImgAStDuN98pKi1qLm0" />'
