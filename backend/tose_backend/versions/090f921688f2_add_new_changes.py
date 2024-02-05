"""Add new changes

Revision ID: 090f921688f2
Revises: c51ca99baf27
Create Date: 2024-01-21 10:50:27.377424

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '090f921688f2'
down_revision: Union[str, None] = 'c51ca99baf27'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('rechnungen', 'rechnungsbetrag',
               existing_type=sa.DOUBLE_PRECISION(precision=53),
               type_=sa.Numeric(precision=10, scale=2),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('rechnungen', 'rechnungsbetrag',
               existing_type=sa.Numeric(precision=10, scale=2),
               type_=sa.DOUBLE_PRECISION(precision=53),
               existing_nullable=True)
    # ### end Alembic commands ###