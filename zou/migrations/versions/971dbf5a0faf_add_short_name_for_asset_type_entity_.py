"""Add short_name for Asset Type entity_type

Revision ID: 971dbf5a0faf
Revises: a252a094e977
Create Date: 2024-06-20 19:51:15.758780

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "971dbf5a0faf"
down_revision = "a252a094e977"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "entity_type",
        sa.Column("short_name", sa.String(length=20), nullable=True),
    )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("entity_type", "short_name")
    # ### end Alembic commands ###
