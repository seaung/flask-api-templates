from contextlib import contextmanager
from flask_sqlalchemy import SQLAlchemy as _SQLALchemy, BaseQuery


class SQLAlchemy(_SQLALchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e


class Query(BaseQuery):
    ...


db = SQLAlchemy(query_class=Query)
