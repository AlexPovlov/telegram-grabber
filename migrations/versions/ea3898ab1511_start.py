"""Start

Revision ID: ea3898ab1511
Revises:
Create Date: 2023-06-25 20:01:25.998261

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea3898ab1511'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'accounts',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=True),
        sa.Column('phone', sa.String(), nullable=True),
        sa.Column('phone_hash', sa.String(), nullable=True),
        sa.Column('auth', sa.Boolean(), nullable=True),
        sa.Column('state', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    op.drop_table('accounts')
