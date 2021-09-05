"""Changed.

Revision ID: bba3eb53c829
Revises: 
Create Date: 2021-09-05 13:07:13.511721

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bba3eb53c829'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('informations',
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.Column('date', sa.Integer(), nullable=True),
    sa.Column('information', sa.String(length=512), nullable=True),
    sa.Column('url', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('name', 'url'),
    sa.UniqueConstraint('url')
    )
    op.create_index(op.f('ix_informations_date'), 'informations', ['date'], unique=False)
    op.create_index(op.f('ix_informations_information'), 'informations', ['information'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_informations_information'), table_name='informations')
    op.drop_index(op.f('ix_informations_date'), table_name='informations')
    op.drop_table('informations')
    # ### end Alembic commands ###