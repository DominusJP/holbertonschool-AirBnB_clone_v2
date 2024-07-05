#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}


    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is not None:
            class_dict = {}
            for key, value in FileStorage.__objects.items():
                if type(value) is cls:
                    class_dict[key] = value

            return class_dict
        else:
            return FileStorage.__objects

    def delete(self, obj=None):
        """ Public instance method that deletes given object"""
        try:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            del FileStorage.__objects[key]
        except Exception:
            pass

    def new(self, obj):
        """Adds new object to storage dictionary"""
	@@ -39,7 +29,7 @@ def save(self):
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
	@@ -65,6 +55,15 @@ def reload(self):
        except FileNotFoundError:
            pass

    def close(self):
        """Seyyarin can sagligi"""
        self.reload()
