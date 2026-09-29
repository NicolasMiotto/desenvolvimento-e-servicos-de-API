get_all_spec = {
    "responses": {
        "200": {
            "description": "Lista de séries retornada com sucesso",
            "schema": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer"},
                        "titulo": {"type": "string"},
                        "noticia": {"type": "string"},
                        "imagem": {"type": "string"},
                        "categoria": {"type": "string"},
                        "data_postagem": {"type": "string"},
                        "quem_postou": {"type": "string"}
                    }
                }
            }
        }
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
                    "id": {"type": "integer"},
                    "titulo": {"type": "string"},
                    "noticia": {"type": "string"},
                    "imagem": {"type": "string"},
                    "categoria": {"type": "string"},
                    "data_postagem": {"type": "string"},
                    "quem_postou": {"type": "string"}
                }
            }
        }
    ],
    "responses": {
        "201": {"description": "Notícia cadastrada com sucesso"}
    }
}

update_spec = {
    "parameters": [
        {
            "name": "noticia_id",
            "in": "path",
            "type": "integer",
            "required": True,
            "description": "ID da notícia"
        },
        {
            "name": "body",
            "in": "body",
            "required": True,
            "schema": {
                "type": "object",
                "properties": {
                    "titulo": {"type": "string"},
                    "noticia": {"type": "string"},
                    "imagem": {"type": "string"},
                    "categoria": {"type": "string"},
                    "data_postagem": {"type": "string"},
                    "quem_postou": {"type": "string"}
                }
            }
        }
    ],
    "responses": {
        "200": {"description": "Notícia atualizada com sucesso"},
        "404": {"description": "Notícia não encontrada"}
    }
}

delete_spec = {
    "parameters": [
        {
            "name": "noticia_id",
            "in": "path",
            "type": "integer",
            "required": True,
            "description": "ID da Notícia"
        }
    ],
    "responses": {
        "200": {"description": "Notícia removida com sucesso"},
        "404": {"description": "Notícia não encontrada"}
    }
}