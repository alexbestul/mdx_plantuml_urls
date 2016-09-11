import mock
import pytest
from mdx_plantuml_urls import PlantUmlBlockProcessor
import textwrap
import plantuml

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

def test_whenplanturlisnotsupplied_defaultplantumlurlisused():
    # Arrange
    bp = PlantUmlBlockProcessor(mock.Mock())

    # Act
    plant = bp.get_plant_instance()

    # Assert
    assert plant.url == plantuml.SERVER_URL

def test_whenplanturlissupplied_suppliedurlisused():
    # Arrange
    planturl = 'http://my_plant_server.localhost.org/plant/'
    bp = PlantUmlBlockProcessor(mock.Mock())
    bp.planturl = planturl

    # Act
    plant = bp.get_plant_instance()

    # Assert
    assert plant.url == planturl

def test_whendefaultskinparamissupplied_itisinsertedafterthestartumltoken():
    # Arrange
    skinparam = textwrap.dedent('''\
        skinparam monochrome true
        skinparam handwritten true''')

    text = textwrap.dedent('''\
        @startuml

        bob -> alice

        @enduml''')

    expected_output = textwrap.dedent('''\
        @startuml
        skinparam monochrome true
        skinparam handwritten true

        bob -> alice

        @enduml''')

    bp = PlantUmlBlockProcessor(mock.Mock())
    bp.skinparam = skinparam

    # Act
    result = bp.collect_blocks(to_blocks(text))

    # Assert
    assert result == expected_output




def to_blocks(text):
    return text.split('\n')
