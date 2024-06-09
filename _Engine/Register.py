class Registry:
    def __init__(self):
        self._registry = {}

    def register(self, name, obj):
        """
        Register an object with a given name.

        Args:
            name (str): The name to register the object under.
            obj (any): The object to register.
        """
        if name in self._registry:
            raise ValueError(f"An object with the name '{name}' is already registered.")
        self._registry[name] = obj
        return self

    def get(self, name):
        """
        Retrieve an object by its registered name.

        Args:
            name (str): The name of the registered object.

        Returns:
            any: The registered object.
        """
        return self._registry.get(name)

    def unregister(self, name):
        """
        Unregister an object by its name.

        Args:
            name (str): The name of the object to unregister.
        """
        if name in self._registry:
            del self._registry[name]
        return self

    def all(self):
        """
        Retrieve all registered objects.

        Returns:
            dict: A dictionary of all registered objects.
        """
        return self._registry
