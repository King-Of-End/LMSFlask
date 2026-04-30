from data.db_session import global_init, create_session
from models import User, Jobs

from sqlalchemy import select

global_init(input())
sess = create_session()
resp = sess.execute(select(Jobs)).scalars()
k = max(len(x.collaborators.split(', ')) for x in resp)
for i in resp:
    if len(i.collaborators.split(', ')) == k:
        print(i.team_leader_obj)