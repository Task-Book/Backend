"""initial migration

Revision ID: a9faff0e73b4
Revises: 
Create Date: 2022-12-26 17:12:21.678240

"""
import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = "a9faff0e73b4"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "categories",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=120), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    op.create_table(
        "profiles",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(length=120), nullable=True),
        sa.Column("password", sa.String(length=120), nullable=True),
        sa.Column("name", sa.String(length=120), nullable=True),
        sa.Column("photo", sa.String(length=120), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )
    op.create_table(
        "tasks",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.Column("description", sa.String(length=120), nullable=False),
        sa.Column("category_id", sa.Integer(), nullable=True),
        sa.Column(
            "status",
            sa.Enum("CREATED", "DONE", "DELETED", name="status"),
            nullable=True,
        ),
        sa.Column(
            "priority",
            sa.Enum("URGENT", "HIGH", "MEDIUM", "LOW", name="priority"),
            nullable=True,
        ),
        sa.Column("end_date", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(
            ["category_id"], ["categories.id"], ondelete="CASCADE"
        ),
        sa.ForeignKeyConstraint(
            ["user_id"], ["profiles.id"], ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade():
    op.drop_table("tasks")
    op.drop_table("profiles")
    op.drop_table("categories")
