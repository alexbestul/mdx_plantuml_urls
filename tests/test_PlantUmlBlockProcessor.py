import mock
import pytest
from pytest_mock import mocker
from mdx_plantuml_urls import PlantUmlBlockProcessor
from mdx_plantuml_urls import PlantUmlUrlExtension

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

def test_blockprocessor_is_added_via_createBlockprocessor(mocker):
    # Arrange
    extension = PlantUmlUrlExtension()
    fakeBlockprocessor = mock.Mock()

    mocker.patch.object(extension, 'createBlockprocessor')
    extension.createBlockprocessor.return_value = fakeBlockprocessor

    md = mock.Mock()

    # Act
    extension.extendMarkdown(md, None)

    # Assert
    md.parser.blockprocessors.add.assert_called_with('markdown_plantuml_img', fakeBlockprocessor, '>code')

def test_createBlockprocessordefaultvalues():
    # Arrange
    planturl = 'my_custom_planturl'
    extension = PlantUmlUrlExtension()
    md = mock.Mock()

    # Act
    blockprocessor = extension.createBlockprocessor(md)

    # Assert
    assert blockprocessor.planturl == ''
    assert blockprocessor.skinparam == ''

def test_whenplanturlissuppliedtoextension_planturlissetonblockprocessor():
    # Arrange
    planturl = 'my_custom_planturl'
    extension = PlantUmlUrlExtension(planturl=planturl)
    md = mock.Mock()

    # Act
    blockprocessor = extension.createBlockprocessor(md)

    # Assert
    assert blockprocessor.planturl == planturl

def test_whenskinparamissuppliedtoextension_skinparamissetonblockprocessor():
    # Arrange
    skinparam = 'my_custom_skinparam'
    extension = PlantUmlUrlExtension(default_skinparam=skinparam)
    md = mock.Mock()

    # Act
    blockprocessor = extension.createBlockprocessor(md)

    # Assert
    assert blockprocessor.skinparam == skinparam
