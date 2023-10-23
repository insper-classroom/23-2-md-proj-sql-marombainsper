
BASE_ROUTE = "subscriptions"

def register_routes(app, root="api"):
    from .controller import router as user_router

    app.include_router(user_router, prefix=f"/{root}/{BASE_ROUTE}")