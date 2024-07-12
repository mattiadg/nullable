from nullable import Nullable


def test_none():
    assert Nullable(None).get() is None


def test_chain_none_attr():
    assert Nullable(None).x.y.get() is None


def test_chain_none_item():
    assert Nullable(None)["item1"]["item2"].get() is None


def test_good_values():
    elem = Nullable([1, "two", {"three": 3}])
    assert elem.x.get() is None
    assert isinstance(elem[0], Nullable)
    assert elem[0].get() == 1
    assert len(elem[1].get()) == 3
    assert elem[2]["three"].get() == 3
    assert elem[2]["one"].get() is None
