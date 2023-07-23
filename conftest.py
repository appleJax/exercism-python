def pytest_configure(config):
    config.addinivalue_line("markers", "task: A concept exercise task")


def pytest_addoption(parser):
    parser.addoption("--taskno", action="store")


def pytest_collection_modifyitems(config, items):
    filter = config.getoption("--taskno")
    if filter:
        items[:] = (
            item
            for item in items
            if (mark := item.get_closest_marker("task"))
            and mark.kwargs
            and mark.kwargs["taskno"] in map(int, filter.split(','))
        )
