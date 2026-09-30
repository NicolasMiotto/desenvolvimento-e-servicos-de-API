from flask import Flask, request
from flasgger import Swagger, swag_from
from controllers.moto_controller import MotoController
from config.swagger import (
    get_all_spec, get_by_id_spec, insert_spec, update_spec, delete_spec
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
    "specs_route": "/motos/swagger"
}

swagger = Swagger(app, config=swagger_config)

# 1. Consultar Tudo
@app.route('/motos', methods=['GET'])
@swag_from(get_all_spec)
def listar_todas():
    return MotoController.mostrar_tudo()

# 2. Consultar por ID
@app.route('/motos/<int:moto_id>', methods=['GET'])
@swag_from(get_by_id_spec)
def obter_por_id(moto_id):
    return MotoController.mostrar_por_id(moto_id)

# 3. Cadastrar
@app.route('/motos', methods=['POST'])
@swag_from(insert_spec)
def criar():
    dados = request.json
    return MotoController.cadastrar(dados)

# 4. Atualizar
@app.route('/motos/<int:moto_id>', methods=['PUT'])
@swag_from(update_spec)
def atualizar(moto_id):
    dados = request.json
    return MotoController.atualizar(moto_id, dados)

# 5. Excluir
@app.route('/motos/<int:moto_id>', methods=['DELETE'])
@swag_from(delete_spec)
def deletar(moto_id):
    return MotoController.excluir(moto_id)

if __name__ == '__main__':
    app.run(debug=True)