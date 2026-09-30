from flask import jsonify
from models.moto import MotoModel

class MotoController:
    @staticmethod
    def mostrar_tudo():
        motos = MotoModel.get_all()
        return jsonify(motos)

    @staticmethod
    def mostrar_por_id(moto_id):
        moto = MotoModel.get_by_id(moto_id)
        if moto:
            return jsonify(moto)
        return jsonify({"erro": "Moto não encontrada", "código": "404"}), 404

    @staticmethod
    def cadastrar(dados):
        novo_id = MotoModel.insert(dados)
        return jsonify({"mensagem": "Moto cadastrada com sucesso", "id": novo_id}), 201

    @staticmethod
    def atualizar(moto_id, dados):
        sucesso = MotoModel.update(moto_id, dados)
        if sucesso:
            return jsonify({"mensagem": "Moto atualizada com sucesso"})
        return jsonify({"erro": "Moto não encontrada", "código": "404"}), 404

    @staticmethod
    def excluir(moto_id):
        sucesso = MotoModel.delete(moto_id)
        if sucesso:
            return jsonify({"mensagem": "Moto excluída com sucesso"})
        return jsonify({"erro": "Moto não encontrada", "código": "404"}), 404