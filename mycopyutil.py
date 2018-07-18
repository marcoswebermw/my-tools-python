""" Uma modificação do sutil.copyfileobj() que nem sempre funciona para mim. 
    Por questões de desempenhos em arquivos grandes, o arquivo de origem
    é lido aos poucos e seu conteúdo é guardado no buffer e então escrito
    no arquivo de destino.
"""
def copiaArquivo(origem, destino):
    # Buffer de 16kb. Talvez seja melhor aumentá-lo.
    tamanhoBuffer = 16 * 1024
    with open(origem, 'rb') as arqOrigem:
        with open(destino, 'wb') as arqDestino:
            while True:
                buf = arqOrigem.read(tamanhoBuffer)
                if not buf:
                    break
                destino.write(buf)


def copiaDadosParaArquivo(dados, destino):
    # Buffer de 16kb. Talvez seja melhor aumentá-lo. Exemplo: 64kb (2**16 ou 65536).
    tamanhoBuffer = 16 * 1024
    copiado = 0
    with open(destino, 'wb') as arqDestino:
        while True:
            # Size
            buf = dados.read(tamanhoBuffer)
            if not buf:
                break
            destino.write(buf)
            copiado = copiado + len(buf) # Quantidade copiada
            print(copiado)


def copiaUrlParaArquivo(url, destino):
    # Fazendo a requisição
    import urllib3
    http = urllib3.PoolManager()
    r = http.request('GET', url, preload_content=False)

    # Buffer de 16kb. Talvez seja melhor aumentá-lo. Exemplo: 64kb (2**16 ou 65536).
    tamanhoBuffer = 16 * 1024
    copiado = 0
    with open(destino, 'wb') as arqDestino:
        while True:
            buf = r.read(tamanhoBuffer)
            if not buf:
                break
            arqDestino.write(buf)
            copiado = copiado + len(buf) # Quantidade copiada
    
    r.release_conn()
    quantidadeCopiada = "{}kb".format(copiado/1024)
    return quantidadeCopiada
