from _Engine.LogManager import Log

try:
    class Event(object):
        """
        Base class for the event-driven system
        """

        _events = []

        def __init__(self, name: str) -> None:
            """
            Initialise event system
            """
            self._event_handler = []
            self._name = name
            Event._events.append(self)

        def subscribe(self, fn):
            """
            Add an event subscription

            Args:
                fn (function): The function to subscribe
            """
            self._event_handler.append(fn)
            return self

        def unsubscribe(self, fn):
            """
            Delete event subscription fn

            Args:
                fn (function): The function to unsubscribe
            """
            self._event_handler.remove(fn)
            return self

        def __iadd__(self, fn):
            """
            Add event subscription fn

            Args:
                fn (function): The function to subscribe
            """
            self._event_handler.append(fn)
            return self

        def __isub__(self, fn):
            """
            Delete event subscription fn

            Args:
                fn (function): The function to unsubscribe
            """
            self._event_handler.remove(fn)
            return self

        def __call__(self, *args, **keywargs):
            """
            Calls all event subscription functions
            """
            for eventhandler in self._event_handler:
                eventhandler(*args, **keywargs)

        @classmethod
        def get_all_events(cls):
            """
            Get all registered events

            Returns:
                list: List of all Event instances
            """
            return cls._events
except Exception as e:
    Log.getModule().error(f"Error loading Event Module: '{e}'")