import mock
import pytest
from markdown_plantuml_img import PlantUmlBlockProcessor
import textwrap

def test_givensimplepleumlblock_collect_blocks_returnsentireblock():
    # Arrange
    bp = PlantUmlBlockProcessor(mock.Mock())

    text = textwrap.dedent('''\
        @startuml
        @enduml''')

    # Act
    result = bp.collect_blocks(to_blocks(text))

    # Assert
    assert result == text

def test_givenunclosedplantumlblock_collect_blocks_returnsentireblock():
    # Arrange
    bp = PlantUmlBlockProcessor(mock.Mock())

    text = textwrap.dedent('''\
        @startuml''')

    # Act
    result = bp.collect_blocks(to_blocks(text))

    # Assert
    assert result == text

def test_givensplitplantumlblock_collect_blocks_returnsentireblock():
    # Arrange
    bp = PlantUmlBlockProcessor(mock.Mock())

    text = textwrap.dedent('''\
        @startuml

        bob -> alice

        @enduml''')

    # Act
    result = bp.collect_blocks(to_blocks(text))

    # Assert
    assert result == text

def test_giventextafterplantumlblock_collect_blocks_returnsonlyuml():
    # Arrange
    bp = PlantUmlBlockProcessor(mock.Mock())

    full_text = textwrap.dedent('''\
        @startuml
        @enduml

        Some regular markdown text.''')

    plantuml_text = textwrap.dedent('''\
        @startuml
        @enduml''')

    # Act
    result = bp.collect_blocks(to_blocks(full_text))

    # Assert
    assert result == plantuml_text


def to_blocks(text):
    return text.split('\n')
