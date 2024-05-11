from schemas import Squad
from routes import squads_router


@squads_router.get("/", response_model=list[Squad], response_model_exclude_none=True)
async def get_squads():
    return {"message": "Read squads"}


@squads_router.post("/", response_model=Squad, response_model_exclude_none=True)
async def create_squad(squad: Squad):
    return squad
