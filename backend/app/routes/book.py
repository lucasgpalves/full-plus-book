from fastapi import APIRouter

print('Loading book router')

router = APIRouter(
    prefix='/books'
)

@router.get('/')
async def ping():
    return {'message': 'Book'}