import subprocess

def criar_link_simbolico(destino, origem):
    comando = f'mklink /J "{destino}" "{origem}"'
    try:
        subprocess.call(comando, shell=True)
        return True, "Link simbólico criado com sucesso!"
    except subprocess.CalledProcessError as e:
        return False, f"Ocorreu um erro ao criar o link simbólico: {e}"
