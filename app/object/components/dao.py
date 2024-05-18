from app.dao.base import BaseDAO
from app.object.components.models import Components


class ComponentsDAO(BaseDAO):
    model = Components