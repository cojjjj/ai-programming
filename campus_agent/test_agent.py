
from agent import get_campus_resource_info


def test_library_lookup():
    result = get_campus_resource_info("library")
    assert result["status"] == "success"
    assert result["name"] == "Library"


def test_tutoring_alias():
    result = get_campus_resource_info("tutoring")
    assert result["status"] == "success"
    assert result["name"] == "Tutoring Center"


def test_case_insensitive():
    result = get_campus_resource_info("LIBRARY")
    assert result["status"] == "success"
    assert result["name"] == "Library"


def test_resource_not_found():
    result = get_campus_resource_info("dental office")
    assert result["status"] == "error"
    assert "error_message" in result
    assert "Available resources" in result["error_message"]


def test_list_all_resources():
    result = get_campus_resource_info("all")
    assert result["status"] == "success"
    assert "available_resources" in result
    assert isinstance(result["available_resources"], list)
    assert len(result["available_resources"]) >= 4
