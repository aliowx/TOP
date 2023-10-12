"""empty message

Revision ID: 92fab1095a4d
Revises: afa5805eb617
Create Date: 2023-04-10 08:22:13.530704

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "92fab1095a4d"
down_revision = "afa5805eb617"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "requestlog",
        sa.Column("created", sa.DateTime(timezone=True), nullable=True),
        sa.Column("modified", sa.DateTime(timezone=True), nullable=True),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("authorization", sa.String(length=256), nullable=True),
        sa.Column("method", sa.String(length=10), nullable=True),
        sa.Column("service_name", sa.String(length=50), nullable=True),
        sa.Column("ip", sa.String(length=50), nullable=True),
        sa.Column("request", sa.Text(), nullable=True),
        sa.Column("response", sa.Text(), nullable=True),
        sa.Column("trace", sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_requestlog_authorization"),
        "requestlog",
        ["authorization"],
        unique=False,
    )
    op.create_index(
        op.f("ix_requestlog_created"), "requestlog", ["created"], unique=False
    )
    op.create_index(op.f("ix_requestlog_id"), "requestlog", ["id"], unique=False)
    op.create_index(op.f("ix_requestlog_ip"), "requestlog", ["ip"], unique=False)
    op.create_index(
        op.f("ix_requestlog_method"), "requestlog", ["method"], unique=False
    )
    op.create_index(
        op.f("ix_requestlog_modified"), "requestlog", ["modified"], unique=False
    )
    op.create_index(
        op.f("ix_requestlog_request"), "requestlog", ["request"], unique=False
    )
    op.create_index(
        op.f("ix_requestlog_service_name"), "requestlog", ["service_name"], unique=False
    )
    op.create_index(op.f("ix_requestlog_trace"), "requestlog", ["trace"], unique=False)
    op.create_table(
        "wsrequestlog",
        sa.Column("created", sa.DateTime(timezone=True), nullable=True),
        sa.Column("modified", sa.DateTime(timezone=True), nullable=True),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("authorization", sa.String(length=256), nullable=True),
        sa.Column("method", sa.String(length=10), nullable=True),
        sa.Column("status_code", sa.String(length=10), nullable=True),
        sa.Column("service_name", sa.String(length=100), nullable=True),
        sa.Column("request", sa.Text(), nullable=True),
        sa.Column("response", sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_wsrequestlog_authorization"),
        "wsrequestlog",
        ["authorization"],
        unique=False,
    )
    op.create_index(
        op.f("ix_wsrequestlog_created"), "wsrequestlog", ["created"], unique=False
    )
    op.create_index(op.f("ix_wsrequestlog_id"), "wsrequestlog", ["id"], unique=False)
    op.create_index(
        op.f("ix_wsrequestlog_method"), "wsrequestlog", ["method"], unique=False
    )
    op.create_index(
        op.f("ix_wsrequestlog_modified"), "wsrequestlog", ["modified"], unique=False
    )
    op.create_index(
        op.f("ix_wsrequestlog_request"), "wsrequestlog", ["request"], unique=False
    )
    op.create_index(
        op.f("ix_wsrequestlog_service_name"),
        "wsrequestlog",
        ["service_name"],
        unique=False,
    )
    op.create_index(
        op.f("ix_wsrequestlog_status_code"),
        "wsrequestlog",
        ["status_code"],
        unique=False,
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_wsrequestlog_status_code"), table_name="wsrequestlog")
    op.drop_index(op.f("ix_wsrequestlog_service_name"), table_name="wsrequestlog")
    op.drop_index(op.f("ix_wsrequestlog_request"), table_name="wsrequestlog")
    op.drop_index(op.f("ix_wsrequestlog_modified"), table_name="wsrequestlog")
    op.drop_index(op.f("ix_wsrequestlog_method"), table_name="wsrequestlog")
    op.drop_index(op.f("ix_wsrequestlog_id"), table_name="wsrequestlog")
    op.drop_index(op.f("ix_wsrequestlog_created"), table_name="wsrequestlog")
    op.drop_index(op.f("ix_wsrequestlog_authorization"), table_name="wsrequestlog")
    op.drop_table("wsrequestlog")
    op.drop_index(op.f("ix_requestlog_trace"), table_name="requestlog")
    op.drop_index(op.f("ix_requestlog_service_name"), table_name="requestlog")
    op.drop_index(op.f("ix_requestlog_request"), table_name="requestlog")
    op.drop_index(op.f("ix_requestlog_modified"), table_name="requestlog")
    op.drop_index(op.f("ix_requestlog_method"), table_name="requestlog")
    op.drop_index(op.f("ix_requestlog_ip"), table_name="requestlog")
    op.drop_index(op.f("ix_requestlog_id"), table_name="requestlog")
    op.drop_index(op.f("ix_requestlog_created"), table_name="requestlog")
    op.drop_index(op.f("ix_requestlog_authorization"), table_name="requestlog")
    op.drop_table("requestlog")
    # ### end Alembic commands ###
