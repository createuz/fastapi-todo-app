from pydantic import BaseModel, Field
from typing import Optional

from tortoise.contrib.pydantic import pydantic_model_creator

from api.models import Todo

TodoGet = pydantic_model_creator(Todo, name="TodoGet")


class TodoPost(BaseModel):
    title: str = Field(min_length=3, max_length=100)


class TodoPut(BaseModel):
    title: Optional[str] = Field(None, min_length=3, max_length=100)
    done: Optional[bool] = Field(None)
