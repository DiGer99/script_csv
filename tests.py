from utils import where_parse, aggregate_condition

rows = [
    {"name": "iphone 15 pro", "brand": "apple", "price": "999", "rating": "4.9"},
    {"name": "galaxy s23 ultra", "brand": "samsung", "price": "1199", "rating": "4.8"},
    {"name": "iphone 16 pro max", "brand": "apple", "price": "2499", "rating": "5.0"},
    {"name": "redmi note 12", "brand": "xiaomi", "price": "199", "rating": "4.6"},
    {"name": "poco x5 pro", "brand": "xiaomi", "price": "299", "rating": "4.4"},
    {"name": "pixel 8 pro", "brand": "google", "price": "999", "rating": "4.7"},
    {"name": "realme 11 pro", "brand": "realme", "price": "349", "rating": "4.3"},
    {"name": "nokia x20", "brand": "nokia", "price": "399", "rating": "4.1"},
    {"name": "iphone 16", "brand": "apple", "price": "1499", "rating": "5.0"},
    {"name": "motorola edge 40", "brand": "motorola", "price": "599", "rating": "4.5"},
    {"name": "asus zenfone 10", "brand": "asus", "price": "699", "rating": "4.6"},
    {"name": "iphone 16 pro", "brand": "apple", "price": "1999", "rating": "4.9"},
]


def test_where_xiaomi():
    res = where_parse("brand=xiaomi", rows)
    assert all(i["brand"] == "xiaomi" for i in res)
    assert len(res) == 2


def test_where_apple():
    res = where_parse("brand=apple", rows)
    assert all(i["brand"] == "apple" for i in res)
    assert len(res) == 4


def test_where_aggregate_min():
    where_filter = where_parse("brand=apple", rows)
    res = aggregate_condition("price=min", where_filter)
    assert len(res) == 1
    assert res["min"] == [999.0]


def test_where_aggregate_max():
    where_filter = where_parse("brand=apple", rows)
    res = aggregate_condition("rating=max", where_filter)
    assert len(res) == 1
    assert res["max"] == [5.0]


def test_where_aggregate_avg():
    where_filter = where_parse("brand=apple", rows)
    res = aggregate_condition("price=avg", where_filter)

    avg_list = [float(i["price"]) for i in rows if i["brand"] == "apple"]
    avg_res = sum(avg_list) / len(avg_list)

    assert len(res) == 1
    assert res["avg"] == [avg_res]


def test_only_aggregate():
    res = aggregate_condition("price=avg", rows)
    assert len(res) == 1
    assert res["avg"] == [978.17]


def test_only_max():
    res = aggregate_condition("rating=max", rows)
    assert len(res) == 1
    assert res["max"] == [5.0]


def test_only_min():
    res = aggregate_condition("rating=min", rows)
    assert len(res) == 1
    assert res["min"] == [4.1]
