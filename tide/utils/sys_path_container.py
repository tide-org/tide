import sys

PATH_LIST = []

def insert(path, insert_at=0):
    global PATH_LIST
    sys.path.insert(insert_at, path)
    PATH_LIST.append(path)

def remove(path):
    global PATH_LIST
    sys.path = list(filter(lambda spath: spath != path, sys.path))
    PATH_LIST = list(filter(lambda spath: spath != path, PATH_LIST))

def remove_all():
    global PATH_LIST
    for path in PATH_LIST:
        sys.path = list(filter(lambda spath: spath != path, sys.path))
    PATH_LIST = []
