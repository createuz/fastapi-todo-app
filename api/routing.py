from fastapi.routing import APIRoute, APIRouter
from fastapi import status, HTTPException

from .models import Todo
from .schemas import TodoPost, TodoPut, TodoGet

router = APIRouter(prefix='/api/v1', tags=['Todos'])


@router.get('/')
async def all_todos():
    return await TodoGet.from_queryset(Todo.all())


@router.post('/')
async def create_todo(body: TodoPost):
    data = body.model_dump(exclude_unset=True)
    todo = await Todo.create(**data)
    return await TodoGet.from_tortoise_orm(todo)


@router.put('/{todo_id}')
async def update_todo(todo_id: str, body: TodoPut):
    todo_exists = await Todo.filter(id=todo_id).exists()
    if not todo_exists:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Todo not found')
    data = body.model_dump(exclude_unset=True)
    await Todo.filter(id=todo_id).update(**data)
    return 'Update Successful'


@router.delete('/{todo_id}')
async def delete_todo(todo_id: str):
    todo_exists = await Todo.filter(id=todo_id).exists()
    if not todo_exists:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Todo not found')
    await Todo.filter(id=todo_id).delete()
    return 'Delete Successful'
