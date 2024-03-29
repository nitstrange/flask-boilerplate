"""Initial migration.

Revision ID: 706ee81abc66
Revises: 
Create Date: 2020-04-14 02:42:37.222583

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '706ee81abc66'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_index('ix_person_lname', table_name='person')
    op.drop_table('person')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('person',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.Column('lname', sa.VARCHAR(length=32), nullable=True),
    sa.Column('fname', sa.VARCHAR(length=32), nullable=True),
    sa.Column('cell', sa.VARCHAR(length=13), nullable=True),
    sa.Column('occupation', sa.VARCHAR(length=32), nullable=True),
    sa.Column('location', sa.VARCHAR(length=32), nullable=True),
    sa.Column('email', sa.VARCHAR(length=32), nullable=True),
    sa.Column('timestamp', sa.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_person_lname', 'person', ['lname'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('username', sa.VARCHAR(length=32), nullable=True),
    sa.Column('password', sa.VARCHAR(length=32), nullable=True),
    sa.Column('timestamp', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
