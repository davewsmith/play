from typing import Optional

import sqlalchemy as sa
import sqlalchemy.orm as so

from app import db


class Job(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key = True)
    source: so.Mapped[str] = so.mapped_column(sa.String(128))
    output: so.Mapped[Optional[str]] = so.mapped_column(sa.String(128))
