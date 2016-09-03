import mock
import pytest
from markdown_plantuml_img import PlantUmlBlockProcessor

def test_whenblockexactlymatchesstartumltoken_testreturnstrue():
    # Arrange
    bp = PlantUmlBlockProcessor(mock.Mock())

    # Act
    result = bp.test(None, '@startuml')

    # Assert
    assert result == True

def test_whenblockdoesnotmatchstartumltoken_testreturnsfalse():
    # Arrange
    bp = PlantUmlBlockProcessor(mock.Mock())

    # Act
    result = bp.test(None, 'not the startuml token')

    # Assert
    assert result == False

def test_whenblockcontainsextratextafterstartumltoken_testreturnstrue():
    # This is considered valid because Plant will still parse it,
    # however, any text that follows the @startuml token on the
    # same line will be ignored by Plant.

    # Arrange
    bp = PlantUmlBlockProcessor(mock.Mock())

    # Act
    result = bp.test(None, '@startuml_plus_some_extra_text')

    # Assert
    assert result == True
