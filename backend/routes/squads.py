from database.crud import create_squad
from database.schemas import Squad
from routes import squads_router


@squads_router.get("/", response_model=list[Squad], response_model_exclude_none=True)
async def get_squads():
    return {"message": "Read squads"}


@squads_router.get(
    "/{id}", response_model=list[Squad], response_model_exclude_none=True
)
async def get_squads():
    return {"message": "Read squads"}


@squads_router.post("/", response_model=Squad)
async def create_squad_route(squad: Squad):
    return create_squad(squad)
