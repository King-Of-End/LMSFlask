import sqlalchemy
from sqlalchemy.orm import relationship

from data.db_session import SqlAlchemyBase


class Jobs(SqlAlchemyBase):
    __tablename__ = 'jobs'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    team_leader = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
    job = sqlalchemy.Column(sqlalchemy.String)
    work_size = sqlalchemy.Column(sqlalchemy.Integer)
    collaborators = sqlalchemy.Column(sqlalchemy.String)
    start_date = sqlalchemy.Column(sqlalchemy.DateTime)
    end_date = sqlalchemy.Column(sqlalchemy.DateTime)
    is_finished = sqlalchemy.Column(sqlalchemy.Boolean)

    team_leader_obj = relationship('User', foreign_keys=[team_leader])

    def to_dict(self):
        return {
            'id': self.id,
            'job': self.job,
            'work_size': self.work_size,
            'collaborators': self.collaborators,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'is_finished': self.is_finished,
            'team_leader': self.team_leader_obj.name + ', ' + self.team_leader_obj.surname
        }