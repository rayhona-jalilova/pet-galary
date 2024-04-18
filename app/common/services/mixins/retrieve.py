class RetrieveServiceMixin:
    """
    A mixin class that provides a generic method for retrieving a single instance of a specified model.

    Attributes:
        model (class): The Django model class for which the retrieval method is provided.
    """

    model = None

    def get(self, **kwargs):
        """
        Retrieve and return a single instance of the specified model based on the provided keyword arguments.

        Args:
            **kwargs: Keyword arguments representing the criteria for retrieving the instance.

        Returns:
            Instance: A single instance of the specified model that satisfies the retrieval criteria.

        Raises:
            ValueError: If the `model` attribute is not set or is set to `None`.
            DoesNotExist: If no matching instance is found based on the provided criteria.
            MultipleObjectsReturned: If multiple instances match the provided criteria.
        """
        if self.model is None:
            raise ValueError(
                "Model class not set. Set the 'model' attribute with the appropriate Django model."
            )

        try:
            return self.model.objects.get(**kwargs)
        except self.model.DoesNotExist:
            raise self.model.DoesNotExist(
                f"No matching {self.model.__name__} instance found."
            ) from None
        except self.model.MultipleObjectsReturned:
            raise self.model.MultipleObjectsReturned(
                f"Multiple instances match the provided criteria."
            ) from None
