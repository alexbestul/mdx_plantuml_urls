import mock
import pytest
from pytest_mock import mocker
from markdown_plantuml_img import PlantUmlBlockProcessor

def test_whenblockexactlymatchesstartumltoken_testreturnstrue(mocker):
    # Arrange
    bp = PlantUmlBlockProcessor(mock.Mock())

    # Act
    result = bp.test(None, '@startuml')

    # Assert
    assert result == True
