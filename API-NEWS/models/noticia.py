from config.conexao import get_connection
class NoticiaModel:
    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id, titulo, noticia, imagem, categoria, data_postagem, quem_postou FROM noticias")
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def insert(dados):
        conn = get_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO noticias (titulo, noticia, imagem, categoria, data_postagem, quem_postou) VALUES (%s, %s, %s, %s, %s, %s)"
        valores = (dados.get('titulo'), dados.get('noticia'), dados.get('imagem'), dados.get('categoria'), dados.get('data_postagem'), dados.get('quem_postou'))
        cursor.execute(sql, valores)
        conn.commit()
        last_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return last_id

    @staticmethod
    def update(noticia_id, dados):
        conn = get_connection()
        cursor = conn.cursor()
        sql = "UPDATE noticias set titulo=%s, noticia=%s, imagem=%s, categoria=%s, data_postagem=%s, quem_postou=%s WHERE id=%s"
        valores = (dados.get('titulo'), dados.get('noticia'), dados.get('imagem'), dados.get('categoria'), dados.get('data_postagem'), dados.get('quem_postou'), noticia_id)
        cursor.execute(sql, valores)
        conn.commit()
        rowcount = cursor.rowcount
        cursor.close()
        conn.close()
        return rowcount > 0

    @staticmethod
    def delete(noticia_id):
        conn = get_connection()
        cursor = conn.cursor()
        sql = "DELETE FROM noticias WHERE id = %s"
        valores = (noticia_id,)
        cursor.execute(sql, valores)
        conn.commit()
        rowcount = cursor.rowcount
        cursor.close()
        conn.close()
        return rowcount > 0