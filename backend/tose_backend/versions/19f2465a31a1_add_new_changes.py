"""Add new changes

Revision ID: 19f2465a31a1
Revises: a4b91399fca7
Create Date: 2024-01-29 19:26:54.818743

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '19f2465a31a1'
down_revision: Union[str, None] = 'a4b91399fca7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('kündigungsanfrage', sa.Column('neuer_tarif_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'kündigungsanfrage', 'tarif', ['neuer_tarif_id'], ['tarif_id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'kündigungsanfrage', type_='foreignkey')
    op.drop_column('kündigungsanfrage', 'neuer_tarif_id')
    # ### end Alembic commands ###