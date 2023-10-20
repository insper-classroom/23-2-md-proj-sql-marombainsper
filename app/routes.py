def register_routes(app, root="api"):
    from app.members import register_routes as attach_users
    from app.plans import register_routes as attach_plans

    attach_users(app)
    attach_plans(app)