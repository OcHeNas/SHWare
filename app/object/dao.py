from app.dao.base import BaseDAO
from app.object.models import Object


class ObjectDAO(BaseDAO):
    model = Object