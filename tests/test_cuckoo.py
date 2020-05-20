import pytest
from cuckoo_filter import CuckooFilter


@pytest.fixture(scope="module")
def entries():
    return ["hello world", "hey buddy", "cuckoo!", "today"]


@pytest.fixture(scope="module")
def cfilter(entries):
    st = CuckooFilter(table_size=10)
    for i in entries:
        st.insert(i)
    return st


def test_cuckoo(cfilter):
    assert "hello world" in cfilter
    assert "tomorrow" not in cfilter
    assert "cuckoo!" in cfilter


def test_cuckoo_size(cfilter):
    assert cfilter.table_size == 10
