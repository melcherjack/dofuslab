"""empty message

Revision ID: 6d5e10e2995e
Revises: d4f262a8d2bf
Create Date: 2020-03-10 22:12:27.228323

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6d5e10e2995e'
down_revision = 'd4f262a8d2bf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_custom_set_name'), 'custom_set', ['name'], unique=False)
    op.create_unique_constraint(op.f('uq_equipped_item_exo_equipped_item_id'), 'equipped_item_exo', ['equipped_item_id', 'stat'])
    op.drop_index('ix_equipped_item_exo_num_items', table_name='equipped_item_exo')
    op.drop_column('equipped_item_exo', 'num_items')
    op.create_index(op.f('ix_item_stat_stat'), 'item_stat', ['stat'], unique=False)
    op.create_index(op.f('ix_item_translation_item_id'), 'item_translation', ['item_id'], unique=False)
    op.create_index(op.f('ix_item_translation_locale'), 'item_translation', ['locale'], unique=False)
    op.create_index(op.f('ix_item_translation_name'), 'item_translation', ['name'], unique=False)
    op.create_index(op.f('ix_set_bonus_stat'), 'set_bonus', ['stat'], unique=False)
    op.create_index(op.f('ix_set_translation_locale'), 'set_translation', ['locale'], unique=False)
    op.create_index(op.f('ix_set_translation_name'), 'set_translation', ['name'], unique=False)
    op.create_index(op.f('ix_set_translation_set_id'), 'set_translation', ['set_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_set_translation_set_id'), table_name='set_translation')
    op.drop_index(op.f('ix_set_translation_name'), table_name='set_translation')
    op.drop_index(op.f('ix_set_translation_locale'), table_name='set_translation')
    op.drop_index(op.f('ix_set_bonus_stat'), table_name='set_bonus')
    op.drop_index(op.f('ix_item_translation_name'), table_name='item_translation')
    op.drop_index(op.f('ix_item_translation_locale'), table_name='item_translation')
    op.drop_index(op.f('ix_item_translation_item_id'), table_name='item_translation')
    op.drop_index(op.f('ix_item_stat_stat'), table_name='item_stat')
    op.add_column('equipped_item_exo', sa.Column('num_items', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_index('ix_equipped_item_exo_num_items', 'equipped_item_exo', ['num_items'], unique=False)
    op.drop_constraint(op.f('uq_equipped_item_exo_equipped_item_id'), 'equipped_item_exo', type_='unique')
    op.drop_index(op.f('ix_custom_set_name'), table_name='custom_set')
    # ### end Alembic commands ###
