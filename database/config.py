DB_CONFIG = {
    "connections": {"default": {"db_url": 'sqlite://db.sqlite3'}
    },

    "apps": {
        "User": {"models": ["models"], "default_connection": "default"},
        "Product": {"models": ["models"], "default_connection": "default"},
        "Order": {"models": ["models"], "default_connection": "default"},
        "OrderProduct": {"models": ["models"], "default_connection": "default"},
        "Payment": {"models": ["models"], "default_connection": "default"}
    }

}
