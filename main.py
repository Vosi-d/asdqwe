from pydantic import BaseModel
from typing import List,Optional, Dict
class Player(BaseModel):
    user:str
    comment:Optional [str]
    likes:int=0
lol=Player(user='kiku', comment='pizdes', likes=99)
print(lol)