from rest_framework.views import APIView
from rest_framework.views import Response
from typing import TypedDict
import json


def genId():
    n = 0
    while True:
        n += 1
        yield n


userId = genId()
User = TypedDict('User', {'id': int, 'name': str, 'age': int})


class FileServices:

    def __init__(self, file_name: str):
        self.__file_name = file_name
        self.__user_arr: [User] = []
        self.read_file()

    def create(self, user: User):
        try:
            self.__user_arr.append(user)
            self.write_file()
            return user
        except Exception as err:
            raise err

    def delete_by_id(self, id: int):
        try:
            i = 0
            for item in self.__user_arr:
                if item['id'] == id:
                    del self.__user_arr[i]
                    self.write_file()
                    return item
                else:
                    i += 1
                    continue
            return '!!! Failure. There is no such an Id in the file.'
        except Exception as err:
            raise err

    def get_all(self):
        try:
            if not len(self.__user_arr) > 0:
                return '!!! Список пуст'
            else:
                return self.__user_arr
        except Exception as err:
            raise err

    def get_one_by_id(self, id: int):
        try:
            for item in self.__user_arr:
                if item['id'] == id:
                    return item
            return '!!! Failure. There is no such an Id in the file.'
        except Exception as err:
            raise err

    def alter_by_id(self, user: User):
        i = 0
        for item in self.__user_arr:
            if item['id'] == user['id']:
                self.__user_arr[i] = user
                self.write_file()
                return self.__user_arr[i]
            else:
                i += 1
                continue
        return '!!! Failure. There is no such an Id in the file.'

    def read_file(self):
        try:
            with open(self.__file_name, 'r') as file:
                self.__user_arr = json.load(file)
        except Exception as err:
            raise err

    def write_file(self):
        try:
            with open(self.__file_name, 'w') as file:
                json.dump(self.__user_arr, file)
        except Exception as err:
            raise err


file_services = FileServices('MyFile')


class UserView(APIView):
    @staticmethod
    def get(*args, **kwargs):
        try:
            return Response(file_services.get_one_by_id(kwargs.get('id')))
        except Exception as err:
            return Response(err)

    def post(self, *args, **kwargs):
        try:
            user: User = self.request.data
            user['id'] = (next(userId))
            return Response(file_services.create(user))
        except Exception as err:
            return Response(err)

    def patch(self, *args, **kwargs):
        try:
            user: User = self.request.data
            user['id'] = kwargs.get('id')
            return Response(file_services.alter_by_id(user))
        except Exception as err:
            return Response(err)

    @staticmethod
    def delete(*args, **kwargs):
        try:
            return Response(file_services.delete_by_id(kwargs.get('id')))
        except Exception as err:
            return Response(err)


class UsersView(APIView):
    @staticmethod
    def get(*args, **kwargs):
        return Response(file_services.get_all())
