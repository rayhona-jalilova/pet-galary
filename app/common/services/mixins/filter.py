class FilterServiceMixin:
    """
    A mixin class that provides a generic method for filtering instances of a specified model.

    Attributes:
        model (class): The Django model class for which the filtering method is provided.
    """

    model = None

    def filter(self, **kwargs):
        """
        Filter and return instances of the specified model based on the provided keyword arguments.

        Args:
            **kwargs: Keyword arguments representing the filtering criteria.

        Returns:
            QuerySet: A QuerySet containing instances of the specified model that satisfy the filtering criteria.

        Raises:
            ValueError: If the `model` attribute is not set or is set to `None`.
        """
        if self.model is None:
            raise ValueError(
                "Model class not set. Set the 'model' attribute with the appropriate Django model."
            )

        return self.model.objects.filter(**kwargs)
