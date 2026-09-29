from flask import Flask, request
from flasgger import Swagger, swag_from
from controllers.noticia_controller import NoticiaController
from config.swagger import (
    get_all_spec, insert_spec, update_spec, delete_spec
)

app = Flask(__name__)

swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'apispec_1',
            "route": '/apispec_1.json',
            "rule_filter": lambda rule: True,
            "model_filter": lambda rule: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/news/swagger"
}

swagger = Swagger(app, config=swagger_config)

@app.route('/news', methods=['GET'])
@swag_from(get_all_spec)
def listar_todas():
    return NoticiaController.mostrar_tudo()

@app.route('/news', methods=['POST'])
@swag_from(insert_spec)
def criar():
    dados = request.json
    return NoticiaController.cadastrar(dados)

@app.route('/news/<int:noticia_id>', methods=['PUT'])
@swag_from(update_spec)
def atualizar(noticia_id):
    dados = request.json
    return NoticiaController.atualizar(noticia_id, dados)

@app.route('/news/<int:serie_id>', methods=['DELETE'])
@swag_from(delete_spec)
def deletar(noticia_id):
    return NoticiaController.excluir(noticia_id)





if __name__ == '__main__':
    app.run(debug=True)