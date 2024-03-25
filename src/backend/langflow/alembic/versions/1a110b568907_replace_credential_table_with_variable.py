"""Replace Credential table with Variable

Revision ID: 1a110b568907
Revises: 63b9c451fd30
Create Date: 2024-03-25 09:40:02.743453

"""
from typing import Sequence, Union

import sqlalchemy as sa
import sqlmodel
from alembic import op
from sqlalchemy.engine.reflection import Inspector

# revision identifiers, used by Alembic.
revision: str = '1a110b568907'
down_revision: Union[str, None] = '63b9c451fd30'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    conn = op.get_bind()
    inspector = Inspector.from_engine(conn)  # type: ignore
    table_names = inspector.get_table_names()
    # ### commands auto generated by Alembic - please adjust! ###
    if "variable" not in table_names:
        op.create_table('variable',
        sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column('value', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column('type', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column('id', sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.Column('user_id', sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='fk_variable_user_id'),
        sa.PrimaryKeyConstraint('id')
        )
    if "credential" in table_names:
        op.drop_table('credential')
    # ### end Alembic commands ###


def downgrade() -> None:
    conn = op.get_bind()
    inspector = Inspector.from_engine(conn)  # type: ignore
    table_names = inspector.get_table_names()
    # ### commands auto generated by Alembic - please adjust! ###
    if "credential" not in table_names:
        op.create_table('credential',
        sa.Column('name', sa.VARCHAR(), nullable=True),
        sa.Column('value', sa.VARCHAR(), nullable=True),
        sa.Column('provider', sa.VARCHAR(), nullable=True),
        sa.Column('user_id', sa.CHAR(length=32), nullable=False),
        sa.Column('id', sa.CHAR(length=32), nullable=False),
        sa.Column('created_at', sa.DATETIME(), nullable=False),
        sa.Column('updated_at', sa.DATETIME(), nullable=True),
        sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='fk_credential_user_id'),
        sa.PrimaryKeyConstraint('id')
        )
    if "variable" in table_names:
        op.drop_table('variable')
    # ### end Alembic commands ###
