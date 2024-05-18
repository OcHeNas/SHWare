from app.dao.base import BaseDAO
from app.object.work.models import Work


class WorkDAO(BaseDAO):
    model = Work
