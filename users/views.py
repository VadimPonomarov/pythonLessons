from rest_framework.views import APIView
from rest_framework.views import Response
from typing import TypedDict
import json


def genId(start: int):
    n = start
    while True:
        n += 1
        yield n


User = TypedDict('User', {'id': int, 'name': str, 'age': int})


class FileServices:

    def __init__(self, file_name: str):
        self.__file_name = file_name
        self.__user_arr: [User] = []
        self.read_file()
        self.__user_id = genId(max(item['id'] for item in self.__user_arr))

    def create(self, user: User):
        try:
            user['id'] = next(self.__user_id)
            self.__user_arr.append(user)
            self.write_file()
            return user
        except Exception as err:
            raise err

    def delete_by_id(self, user_id: int):
        self.read_file()
        try:
            i = 0
            for item in self.__user_arr:
                if item['id'] == user_id:
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
        self.read_file()
        try:
            if not len(self.__user_arr) > 0:
                return '!!! Список пуст'
            else:
                return self.__user_arr
        except Exception as err:
            raise err

    def get_one_by_id(self, id: int):
        self.read_file()
        try:
            for item in self.__user_arr:
                if item['id'] == id:
                    return item
            return '!!! Failure. There is no such an Id in the file.'
        except Exception as err:
            raise err

    def alter_by_id(self, user_id: int, user: User):
        self.read_file()
        user['id'] = user_id
        try:
            i = 0
            for item in self.__user_arr:
                if item['id'] == user_id:
                    self.__user_arr[i] = user
                    self.write_file()
                    return self.__user_arr[i]
                else:
                    i += 1
                    continue
            return '!!! Failure. There is no such an Id in the file.'
        except Exception as err:
            raise err

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
    def get(self, *args, **kwargs):
        try:
            id = kwargs.get('id')
            return Response(file_services.get_one_by_id(id))
        except Exception as err:
            print(err)

    def post(self, *args, **kwargs):
        try:
            user = self.request.data
            response = file_services.create(user)
            return Response(response)
        except Exception as err:
            print(err)

    def delete(self, *args, **kwargs):
        try:
            user_id = kwargs.get('id')
            response = file_services.delete_by_id(int(user_id))
            return Response(response)
        except Exception as err:
            print(err)

    def patch(self, *args, **kwargs):
        try:
            user_id = kwargs.get('id')
            user = self.request.data
            response = file_services.alter_by_id(user_id, user)
            return Response(response)
        except Exception as err:
            print(err)


class UsersView(APIView):
    def get(self, *args, **kwargs):
        try:
            return Response(file_services.get_all())
        except Exception as err:
            print(err)
