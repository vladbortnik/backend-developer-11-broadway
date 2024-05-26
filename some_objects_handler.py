# Here is how I understand the original problem:
#  
# Class "SomeObjectsHandler" in PHP was checking the object names and handling them with hard-coded logic.
# This approach violates the OCP because if we want to handle a new type of an object, 
# we need to modify the "handleObjects" method (thus modify class "SomeObjectsHandler").
#
# How do I go about it:
# 
# We can introduce a handler interface and derive its "child-handlers" for each new object types.
# This way, "SomeObjectsHandler" class is open for extension but (somewhat) "closed" for modification (for we don't need to change its code to add new handlers).

from abc import ABC, abstractmethod

class SomeObject:
    def __init__(self, name: str):
        self._name = name

    def get_object_name(self) -> str:
        return self._name

class ObjectHandler(ABC):
    @abstractmethod
    def handle(self, obj: SomeObject) -> str:
        pass

class Object1Handler(ObjectHandler):
    def handle(self, obj: SomeObject) -> str:
        # Check if the object name is 'object_1'
        if obj.get_object_name() == 'object_1':
            return 'handle_object_1'
        return ''

class Object2Handler(ObjectHandler):
    def handle(self, obj: SomeObject) -> str:
        # Check if the object name is 'object_2'
        if obj.get_object_name() == 'object_2':
            return 'handle_object_2'
        return ''

class SomeObjectsHandler:
    def __init__(self, handlers: list[ObjectHandler]):
        self._handlers = handlers

    def handle_objects(self, objects: list[SomeObject]) -> list[str]:
        results = []
        for obj in objects:
            for handler in self._handlers:
                # Call the handle method of each handler to process the object
                result = handler.handle(obj)
                if result:
                    results.append(result)
        return results

objects = [
    SomeObject('object_1'),
    SomeObject('object_2')
]

handlers = [Object1Handler(), Object2Handler()]
soh = SomeObjectsHandler(handlers)
soh.handle_objects(objects)
