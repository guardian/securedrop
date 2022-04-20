"""Updates journalists.otp_secret length from 16 to 32

Revision ID: de00920916bf
Revises: 1ddb81fb88c2
Create Date: 2021-05-21 15:51:39.202368

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'de00920916bf'
down_revision = '1ddb81fb88c2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('journalists', schema=None) as batch_op:
        batch_op.alter_column('otp_secret',
               existing_type=sa.VARCHAR(length=16),
               type_=sa.String(length=32),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('journalists', schema=None) as batch_op:
        batch_op.alter_column('otp_secret',
               existing_type=sa.String(length=32),
               type_=sa.VARCHAR(length=16),
               existing_nullable=True)

    # ### end Alembic commands ###
