def register_routes(app, root="api"):
    from app.members import register_routes as attach_users
    from app.plans import register_routes as attach_plans
    from app.subscribe import register_routes as attach_subscribe

    attach_users(app)
    attach_plans(app)
    attach_subscribe(app)