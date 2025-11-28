from src.processing import dictionaries_list, filter_by_state, sort_by_date


def test_filter_by_state() -> None:
    """Тест проверяет сортировку по параметру 'state' реализованную в модуле 'processing'"""
    result = filter_by_state(dictionaries_list, state="EXECUTED")
    expected_result = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    assert result == expected_result


def test_sort_by_date() -> None:
    """Тест проверяет сортировку по параметру 'date' реализованную в модуле 'processing'"""
    result = sort_by_date(dictionaries_list)
    expected_result = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    assert result == expected_result
