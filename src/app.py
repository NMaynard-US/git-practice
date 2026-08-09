def get_environment_message(environment="production"):
    environment = environment.lower()

    if environment == "staging":
        return "Application is running in the staging environment."

    return "Application is running in the production environment."


def get_pipeline_status():
    return {
        "source_control": True,
        "automation": True,
        "build": True,
        "unit_testing": True,
        "security_scanning": True,
        "artifact": True,
        "staging": True,
        "integration_testing": True,
        "manual_approval": True,
        "production": True,
        "monitoring": True,
    }