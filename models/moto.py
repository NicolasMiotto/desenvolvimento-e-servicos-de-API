from config.conexao import get_connection

class MotoModel:
    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id, marca, modelo, cilindrada, cor, ano, preco FROM motos")
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_by_id(moto_id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id, marca, modelo, cilindrada, cor, ano, preco FROM motos WHERE id = %s", (moto_id,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def insert(dados):
        conn = get_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO motos (marca, modelo, cilindrada, cor, ano, preco) VALUES (%s, %s, %s, %s, %s, %s)"
        valores = (
            dados.get('marca'),
            dados.get('modelo'),
            dados.get('cilindrada'),
            dados.get('cor'),
            dados.get('ano'),
            dados.get('preco')
        )
        cursor.execute(sql, valores)
        conn.commit()
        last_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return last_id

    @staticmethod
    def update(moto_id, dados):
        conn = get_connection()
        cursor = conn.cursor()
        sql = "UPDATE motos SET marca=%s, modelo=%s, cilindrada=%s, cor=%s, ano=%s, preco=%s WHERE id=%s"
        valores = (
            dados.get('marca'),
            dados.get('modelo'),
            dados.get('cilindrada'),
            dados.get('cor'),
            dados.get('ano'),
            dados.get('preco'),
            moto_id
        )
        cursor.execute(sql, valores)
        conn.commit()
        rowcount = cursor.rowcount
        cursor.close()
        conn.close()
        return rowcount > 0

    @staticmethod
    def delete(moto_id):
        conn = get_connection()
        cursor = conn.cursor()
        sql = "DELETE FROM motos WHERE id = %s"
        valores = (moto_id,)
        cursor.execute(sql, valores)
        conn.commit()
        rowcount = cursor.rowcount
        cursor.close()
        conn.close()
        return rowcount > 0