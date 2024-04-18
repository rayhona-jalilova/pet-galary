class DeleteServiceMixin:
    """
    A mixin class that provides a generic method for deleting an instance of a model.

    Note:
        This mixin assumes that the model has a `delete` method to perform the deletion.

    Methods:
        delete(instance): Delete the specified instance.

    Attributes:
        None
    """

    def delete(self, instance):
        """
        Delete the specified instance.

        Args:
            instance: The instance of the model to be deleted.

        Raises:
            AttributeError: If the specified instance does not have a 'delete' method.
        """
        try:
            instance.delete()
        except AttributeError as e:
            raise AttributeError(
                "The specified instance does not have a 'delete' method."
            ) from e
