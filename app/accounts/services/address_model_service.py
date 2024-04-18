from common.services import CRUDService

from accounts.models import Address


class AddressModelService(CRUDService):
    class Meta:
        model = Address
