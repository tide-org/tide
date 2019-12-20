import sys


class SysPathContainer(object):

    def __init__(self):
        self.__added_list = []

    def insert(self, path, insert_at=0):
       sys.path.insert(insert_at, path)
       self.__added_list.append(path)

    def remove(self, path):
        sys.path.remove(path)
        self.__added_list.remove(path)

    def remove_all(self):
        list_copy = self.__added_list[:]
        for path in list_copy:
            self.remove(path)
