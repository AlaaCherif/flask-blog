"""comment rename

Revision ID: d8ea59214afa
Revises: 21ceaf13012d
Create Date: 2023-05-31 20:42:11.934459

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd8ea59214afa'
down_revision = '21ceaf13012d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comment', schema=None) as batch_op:
        batch_op.add_column(sa.Column('comment', sa.String(length=140), nullable=True))
        batch_op.drop_column('body')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comment', schema=None) as batch_op:
        batch_op.add_column(sa.Column('body', sa.VARCHAR(length=140), nullable=True))
        batch_op.drop_column('comment')

    # ### end Alembic commands ###