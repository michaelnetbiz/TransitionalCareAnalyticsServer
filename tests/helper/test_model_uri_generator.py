from tcas.db import model_uri_generator


def test_model_uri_generator():
    """Test model uri generator.

    """
    assert len(model_uri_generator()) == 16 and type(model_uri_generator()) == str
