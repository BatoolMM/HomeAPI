###########
# GENERAL #
###########

app_title = "HomeAPI"
app_description = "HomeAPI by Koen02. It connects local machines & smart devices to the internet"
app_version = "0.1.0"

# Categories Descriptions
tags_metadata = [
    {
        "name": "machines",
        "description": "Manage HomeAPI enabled machines",
    },
    {
        "name": "lights",
        "description": "Manage Lights",
    },
    {
        "name": "auth",
        "description": "Authentication",
    }
]

############
# DATABASE #
############

database_url = "sqlite:///./app/database/homeapi.db"

########
# AUTH #
########

token_expires_in_minutes = 60
jwt_algorithm = "HS256"
