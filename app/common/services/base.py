from common.services import mixins


class CRUDService(
    mixins.CreateServiceMixin,
    mixins.UpdateServiceMixin,
    mixins.DeleteServiceMixin,
    mixins.FilterServiceMixin,
    mixins.ListServiceMixin,
    mixins.RetrieveServiceMixin,
):
    """
    Base service class providing CRUD operations.

    This class combines several mixins to offer the following operations:
    - Create a new instance
    - Update an existing instance
    - Delete an instance
    - Filter instances based on criteria
    - List all instances
    - Retrieve a single instance

    To use this class, you must define a 'model' attribute in the Meta class:

    Example:
    ```python
    class MyService(CRUDService):
        class Meta:
            model = MyModel
    ```

    Attributes:
        model (class): The Django model class associated with this service.
    """

    def __init__(self) -> None:
        """
        Initialize the CRUDService.

        Raises:
            NotImplementedError: If 'model' is not defined in the Meta class.
        """
        model = getattr(self.Meta, "model", None)
        if model is None:
            raise NotImplementedError(
                "You must provide 'model' in the Meta class."
            )

        self.model = model
