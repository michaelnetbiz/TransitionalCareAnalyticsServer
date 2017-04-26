from tcas.admin.helper import upload_extension_validator


def test_upload_extension_validator():
    assert upload_extension_validator('piz.zip') is True
    assert upload_extension_validator('zip.piz') is False
