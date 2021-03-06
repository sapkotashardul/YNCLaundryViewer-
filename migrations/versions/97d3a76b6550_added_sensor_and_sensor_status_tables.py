"""added sensor and sensor status tables

Revision ID: 97d3a76b6550
Revises: 
Create Date: 2018-08-21 14:44:46.907000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '97d3a76b6550'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sensor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sensorValue', sa.Integer(), nullable=True),
    sa.Column('college', sa.String(), nullable=True),
    sa.Column('machineLabel', sa.String(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_sensor_college'), 'sensor', ['college'], unique=False)
    op.create_index(op.f('ix_sensor_machineLabel'), 'sensor', ['machineLabel'], unique=False)
    op.create_index(op.f('ix_sensor_sensorValue'), 'sensor', ['sensorValue'], unique=False)
    op.create_index(op.f('ix_sensor_timestamp'), 'sensor', ['timestamp'], unique=False)
    op.create_table('sensor_status',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('college', sa.String(), nullable=True),
    sa.Column('machineLabel', sa.String(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_sensor_status_college'), 'sensor_status', ['college'], unique=False)
    op.create_index(op.f('ix_sensor_status_machineLabel'), 'sensor_status', ['machineLabel'], unique=False)
    op.create_index(op.f('ix_sensor_status_status'), 'sensor_status', ['status'], unique=False)
    op.create_index(op.f('ix_sensor_status_timestamp'), 'sensor_status', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_sensor_status_timestamp'), table_name='sensor_status')
    op.drop_index(op.f('ix_sensor_status_status'), table_name='sensor_status')
    op.drop_index(op.f('ix_sensor_status_machineLabel'), table_name='sensor_status')
    op.drop_index(op.f('ix_sensor_status_college'), table_name='sensor_status')
    op.drop_table('sensor_status')
    op.drop_index(op.f('ix_sensor_timestamp'), table_name='sensor')
    op.drop_index(op.f('ix_sensor_sensorValue'), table_name='sensor')
    op.drop_index(op.f('ix_sensor_machineLabel'), table_name='sensor')
    op.drop_index(op.f('ix_sensor_college'), table_name='sensor')
    op.drop_table('sensor')
    # ### end Alembic commands ###
