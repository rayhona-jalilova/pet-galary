from common.services import CRUDService

from accounts.models import Contact


class ContactModelService(CRUDService):
    class Meta:
        model = Contact
