import sys
import pytest
from pytest_tests import setup_tests
import tide.utils.sys_path_container as PathContainer 
from time import sleep

def test__sys_path_container_count_increases_with_insert():
    sys_path_count = len(sys.path)
    PathContainer.insert('/tmp')
    sys_path_count_after_insert = len(sys.path)
    assert sys_path_count_after_insert == sys_path_count + 1
    PathContainer.remove_all()

def test__sys_path_container_count_increases_with_insert():
    sys_path_count = len(sys.path)
    PathContainer.insert('/tmp')
    PathContainer.insert('/work/non_existent_path')
    sys_path_count_after_insert = len(sys.path)
    assert sys_path_count_after_insert == sys_path_count + 2
    PathContainer.remove_all()

def test__sys_path_container_count_same_with_insert_and_remove():
    sys_path_count = len(sys.path)
    PathContainer.insert('/tmp')
    PathContainer.remove('/tmp')
    assert len(sys.path) == sys_path_count

def test__sys_path_container_count_same_with_insert_and_remove_all():
    sys_path_count = len(sys.path)
    PathContainer.insert('/work/docs')
    PathContainer.remove_all()
    assert len(sys.path) == sys_path_count
