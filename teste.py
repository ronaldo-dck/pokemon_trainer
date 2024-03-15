import subprocess

def main():
    for numero in range(1, 1026):
        # Chamando o subprograma e capturando o retorno
        retorno = subprocess.run(['python3', './testeIntegra.py', str(numero)], capture_output=True, text=True)
        if retorno.returncode != 0:
            print(f"FAIL: {numero}")
        else:
            print(f'pass: {numero}')

if __name__ == "__main__":
    main()
