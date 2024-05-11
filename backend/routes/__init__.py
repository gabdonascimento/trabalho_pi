from fastapi import APIRouter, Depends


squads_router = APIRouter(
    prefix="/squads",
    tags=["squads"],
    # dependencies=[Depends(get_db)],
    responses={404: {"description": "Not found"}},
)

students_router = APIRouter(
    prefix="/students",
    tags=["students"],
    # dependencies=[Depends(get_db)],
    responses={404: {"description": "Not found"}},
)

tests_router = APIRouter(
    prefix="/tests",
    tags=["tests"],
    # dependencies=[Depends(get_db)],
    responses={404: {"description": "Not found"}},
)
