get_all_spec = {
    "responses": {
        "200": {
            "description": "Lista de motos retornada com sucesso",
            "schema": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer"},
                        "marca": {"type": "string"},
                        "modelo": {"type": "string"},
                        "cilindrada": {"type": "integer"},
                        "cor": {"type": "string"},
                        "ano": {"type": "integer"},
                        "preco": {"type": "number", "format": "float"}
                    }
                }
            }
        }
    }
}

get_by_id_spec = {
    "parameters": [
        {
            "name": "moto_id",
            "in": "path",
            "type": "integer",
            "required": True,
            "description": "ID da moto a consultar"
        }
    ],
    "responses": {
        "200": {
            "description": "Moto encontrada com sucesso",
            "schema": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "marca": {"type": "string"},
                    "modelo": {"type": "string"},
                    "cilindrada": {"type": "integer"},
                    "cor": {"type": "string"},
                    "ano": {"type": "integer"},
                    "preco": {"type": "number", "format": "float"}
                }
            }
        },
        "404": {"description": "Moto não encontrada"}
    }
}

insert_spec = {
    "parameters": [
        {
            "name": "body",
            "in": "body",
            "required": True,
            "schema": {
                "type": "object",
                "properties": {
                    "marca": {"type": "string"},
                    "modelo": {"type": "string"},
                    "cilindrada": {"type": "integer"},
                    "cor": {"type": "string"},
                    "ano": {"type": "integer"},
                    "preco": {"type": "number", "format": "float"}
                },
                "required": ["marca", "modelo", "cilindrada", "cor", "ano", "preco"]
            }
        }
    ],
    "responses": {
        "201": {"description": "Moto cadastrada com sucesso"}
    }
}

update_spec = {
    "parameters": [
        {
            "name": "moto_id",
            "in": "path",
            "type": "integer",
            "required": True,
            "description": "ID da moto"
        },
        {
            "name": "body",
            "in": "body",
            "required": True,
            "schema": {
                "type": "object",
                "properties": {
                    "marca": {"type": "string"},
                    "modelo": {"type": "string"},
                    "cilindrada": {"type": "integer"},
                    "cor": {"type": "string"},
                    "ano": {"type": "integer"},
                    "preco": {"type": "number", "format": "float"}
                }
            }
        }
    ],
    "responses": {
        "200": {"description": "Moto atualizada com sucesso"},
        "404": {"description": "Moto não encontrada"}
    }
}

delete_spec = {
    "parameters": [
        {
            "name": "moto_id",
            "in": "path",
            "type": "integer",
            "required": True,
            "description": "ID da moto"
        }
    ],
    "responses": {
        "200": {"description": "Moto removida com sucesso"},
        "404": {"description": "Moto não encontrada"}
    }
}