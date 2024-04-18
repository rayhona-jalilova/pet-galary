class ListServiceMixin:
    """
    A mixin class that provides a generic method for retrieving all instances of a specified model.

    Attributes:
        model (class): The Django model class for which the retrieval method is provided.
    """

    model = None

    def all(self):
        """
        Retrieve and return all instances of the specified model.

        Returns:
            QuerySet: A QuerySet containing all instances of the specified model.

        Raises:
            ValueError: If the `model` attribute is not set or is set to `None`.
        """
        if self.model is None:
            raise ValueError(
                "Model class not set. Set the 'model' attribute with the appropriate Django model."
            )

        return self.model.objects.all()
