from fastapi import APIRouter, Depends


squads_router = APIRouter(
    prefix="/equipes",
    tags=["equipes"],
    # dependencies=[Depends(get_db)],
    responses={404: {"description": "Not found"}},
)

students_router = APIRouter(
    prefix="/estudantes",
    tags=["estudantes"],
    # dependencies=[Depends(get_db)],
    responses={404: {"description": "Not found"}},
)

tests_router = APIRouter(
    prefix="/provas",
    tags=["provas"],
    # dependencies=[Depends(get_db)],
    responses={404: {"description": "Not found"}},
)

from routes.squads import *
from routes.students import *
from routes.tests import *
