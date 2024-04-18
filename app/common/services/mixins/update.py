class UpdateServiceMixin:
    """
    A mixin class that provides a generic method for updating the fields of an instance.

    Methods:
        update(instance, **kwargs): Update the fields of the specified instance with the provided values.

    Attributes:
        None
    """

    def update(self, instance, **kwargs):
        """
        Update the fields of the specified instance with the provided values.

        Args:
            instance: The instance to be updated.
            **kwargs: Keyword arguments representing the fields and values to be updated.

        Returns:
            Instance: The updated instance with modified fields.

        Note:
            This method modifies the fields of the instance in place.

        Example:
            To update the 'name' and 'age' fields of a 'Person' instance:
            >>> person_instance = Person.objects.get(pk=1)
            >>> updater = UpdateServiceMixin()
            >>> updated_instance = updater.update(person_instance, name='John', age=30)
        """
        for key, value in kwargs.items():
            setattr(instance, key, value)
        return instance
