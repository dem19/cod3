import sqlite3

BD = "boletimEscolar.db"


# matricular Aluno no banco de dados
def matricular(matricula, nome):
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    sql = ("INSERT INTO aluno (matricula,nome) VALUES ('%d', '%s','%s', '%s', '%s' )"
           % (matricula, nome))
    cursor.execute(sql)
    if cursor.rowcount == 1:
        conexao.commit()
        print('Aluno ', nome, 'matricula de  N°: ', matricula)
    else:
        conexao.rollback()
        print('Não foi possível matricular Aluno!')
    cursor.close()
    conexao.close()

# listar todos os alunos
def listar_aluno():
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    sql = "SELECT * FROM aluno  "
    cursor.execute(sql)
    alunos = cursor.fetchall()
    if alunos:
        for aluno in alunos:
            print('-matricula: ', aluno[0], ' - nome: ', aluno[1],'- aprovado:',aluno[2],' - recuperacao:',aluno[3],'reprovado:',aluno[4])
    else:
        print('Nenhum Aluno Matriculado!')
    cursor.close()
    conexao.close()

def listar_aluno_aprovado():
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    sql = " SELECT * FROM Aluno WHERE aprovado = 'True' "
    cursor.execute(sql)
    alunos = cursor.fetchall()
    if alunos:
        for aluno in alunos:
            print('-matricula: ', aluno[0], ' - nome: ', aluno[1],
                  ' - aprovado: ', aluno[4])
    else:
        print('Nenhum Aluno aprovado!')
    cursor.close()
    conexao.close()

def listar_aluno_recuperacao():
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    sql = " SELECT * FROM Aluno WHERE recuperacao = 'True' "
    cursor.execute(sql)
    alunos = cursor.fetchall()
    if alunos:
        for aluno in alunos:
            print('-matricula: ', aluno[0], ' - nome: ', aluno[1],
                  ' - recuperação: ', aluno[4])
    else:
        print('Nenhum Aluno de recuperação!')
    cursor.close()
    conexao.close()

# listar alunos reprovados
def listar_aluno_reprovado():
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    sql = " SELECT * FROM Aluno WHERE reprovado = 'True' "
    cursor.execute(sql)
    alunos = cursor.fetchall()
    if alunos:
        for aluno in alunos:
            print('-matricula: ', aluno[0], ' - nome: ', aluno[1],
                  ' - reprovado: ', aluno[4])
    else:
        print('Nenhum Aluno reprovado!')
    cursor.close()
    conexao.close()

#buscar aluno por matricula

def buscar_por_matricula(matricula):
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    sql = "SELECT * FROM aluno WHERE matricula LIKE '%d'" % matricula
    cursor.execute(sql)
    aluno = cursor.fetchall()
    if aluno:
        for aluno in aluno:
            print('-matricula: ', aluno[0], ' - nome: ', aluno[1],
                  ' - aprovado: ', aluno[2], ' - recuperacao: ', aluno[3],
                  ' - reprovado: ', aluno[4], )
        return True
    else:
        print('Nenhum aluno com essa matricula está matriculado!')
        return False
    cursor.close()
    conexao.close()


# excluir aluno por matricular
def excluir_aluno(matricula):
    if buscar_por_matricula(matricula):
        resposta = input('Deseja realmente exlcuir este aluno ?').lower()
        if resposta == 's':
            conexao = sqlite3.connect(BD)
            cursor = conexao.cursor()
            sql = "DELETE FROM aluno WHERE matricula ='%d'" % matricula
            cursor.execute(sql)
            if cursor.rowcount == 1:
                conexao.commit()
                print('Aluno excluido!')
            else:
                conexao.rollback()
                print('Não foi possível exclui aluno')


#def listar_medias():
#    conexao = sqlite3.connect(BD)
#    cursor = conexao.cursor()
#    sql = "SELECT media FROM notas  "
#    cursor.execute(sql)
#    media = cursor.fetchall()
#    if media:
#        for media in media:
#            return media
#    else:
#        print('Nenhum media Matriculado!')
#    cursor.close()
#   conexao.close()
#
#
#def verificar_situacao_aluno(matricula):
#    conexao = sqlite3.connect(BD)
#    cursor = conexao.cursor()
#    sql = " SELECT * FROM Aluno where matricula == '%d" % matricula
#    cursor.execute(sql)
#    alunos = cursor.fetchall()
#    if alunos:
#        for aluno in alunos:
#            verificar_media(media, recuperacao, reprovado, aprovado)
#            print('-matricula: ', aluno[0], ' - nome: ', aluno[1],
#                  ' - aprovado: ', aluno[2],' - Recuperação:',aluno[3],' - Reprovado:',aluno[4])
#    else:
#        print('Nenhum Aluno aprovado!')
#    cursor.close()
#    conexao.close()
#
#
#def atualizar_matricula(aprovado,recuperacao,reprovado):
#    media = listar_medias()
#    verificar_media(media, recuperacao, reprovado, aprovado)
#    conexao = sqlite3.connect(BD)
#    cursor = conexao.cursor()
#    sql = "UPDATE aluno SET aprovado = '%s' , recuperacao = '%s', reprovado = '%s' WHERE matricula = '%d'" % (aprovado,recuperacao,reprovado,matricula)
#    cursor.execute(sql)
#    if cursor.rowcount == 1:
#        conexao.commit()
#        print('Matriculas atualizadas.')
#    else:
#        conexao.rollback()
#        print('Não foi possível atualizar matricula dos Alunos!')
#    cursor.close()
#    conexao.close()
#
#
## alunos de recuperação
#
#def verificar_media(media,aprovado,recuperacao,reprovado):
#    conexao = sqlite3.connect(BD)
#    cursor = conexao.cursor()
#    sql = " SELECT media FROM notas"
#    cursor.execute(sql)
#    media = media[0]
#    verificacao = cursor.fetchall()
#    if verificacao:
#        if media < 4:
#            aprovado, recuperacao = False, False
#            reprovado = True
#        elif media > 4 and media < 7:
#            recuperacao = True
#            aprovado,reprovado = False, False
#        else:
#            aprovado = True
#            reprovado,recuperacao = False, False
#
#    else:
#        print('Nenhum Aluno de recuperação!')
#    cursor.close()
#    conexao.close()





def Lancar_notas(matricula_aluno, nota1, nota2, media):
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    sql = ("INSERT INTO notas (matricula_aluno, nota1, nota2, media) VALUES ('%d', '%f', '%f','%f')"
           % (matricula_aluno, nota1, nota2,media))
    cursor.execute(sql)
    if cursor.rowcount == 1:
        conexao.commit()
        print(' Notas do Aluno de matricula: ', matricula_aluno, 'foram lançadas com sucesso!')
    else:
        conexao.rollback()
        print('Não foi possivel lançar notas !')
    cursor.close()
    conexao.close()


def listar_notas():
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    sql = "SELECT * FROM notas  "
    cursor.execute(sql)
    notas = cursor.fetchall()
    if notas:
        for nota in notas:
            print('- matricula: ', nota[0], ' - nota1: ', nota[1], ' - nota2: ', nota[2], ' - media: ', nota[3])
    else:
        print('Não tem Notas de Alunos Lançadas !')
    cursor.close()
    conexao.close()


def excluir_notas(matricula_aluno):
    # if matricula_aluno(matricula_aluno):
    resposta = input('Deseja realmente exlcuir este aluno ?').lower()
    if resposta == 's':
        conexao = sqlite3.connect(BD)
        cursor = conexao.cursor()
        sql = "DELETE FROM notas WHERE matricula_aluno = %d " % matricula_aluno
        cursor.execute(sql)
        if cursor.rowcount == 1:
            conexao.commit()
            print('Aluno excluido!')
        else:
            conexao.rollback()
            print('Não foi possível exclui aluno')