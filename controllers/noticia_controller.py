from flask import jsonify
from models.noticia import NoticiaModel

class NoticiaController:
    @staticmethod
    def mostrar_tudo():
        noticias = NoticiaModel.get_all()
        return jsonify(noticias)

    @staticmethod
    def cadastrar(dados):
        novo_id = NoticiaModel.insert(dados)
        return jsonify({"mensagem": "Notícia criada com sucesso", "id": novo_id}), 201

    @staticmethod
    def atualizar(noticia_id, dados):
        sucesso = NoticiaModel.update(noticia_id, dados)
        if sucesso:
            return jsonify({"mensagem": "Notícia atualizada com sucesso"})
        return jsonify({"erro": "Notícia não encontrada", "código": "404"}), 404

    @staticmethod
    def excluir(noticia_id):
        sucesso = NoticiaModel.delete(noticia_id)
        if sucesso:
            return jsonify({"mensagem": "Notícia excluída com sucesso"})
        return jsonify({"erro": "Notícia não encontrada", "código": "404"}), 404