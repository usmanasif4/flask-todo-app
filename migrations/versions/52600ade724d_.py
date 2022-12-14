"""empty message

Revision ID: 52600ade724d
Revises: 
Create Date: 2022-08-03 09:46:34.719868

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '52600ade724d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('todo', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('todo_comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('comment', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('todo_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['todo_id'], ['todos.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('todo_comments')
    op.drop_table('todos')
    # ### end Alembic commands ###
