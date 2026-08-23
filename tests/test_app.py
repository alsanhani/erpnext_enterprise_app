def test_app_version():
    import my_custom_app
    assert my_custom_app.__version__ == "1.0.0"
