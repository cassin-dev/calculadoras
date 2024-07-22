from math import pow
peso = float(input('Digite o seu peso em KG: '))
alt = float(input('Digite sua altura em metros: '))
imc = peso/(alt*alt)
print(f'O cálculo do IMC é feito baseado nos dados fornecidos pelo usuário e obtém respostas baseadas na tebla fornecida pela Organização Mundial da Saúde (OMS).')
if imc < 18.5:
    print(f'Pela tabela fornecida pela OMS, você está no grau 0 de obesidade e está com a classificação \033[36;4mMagreza\033m, com o IMC de {imc}), com o IMC de {imc:.4}')
elif imc < 24.9:
    print(f'Pela tabela fornecida pela OMS, você está no grau 0 de obesidade e está com a classificação \033[30;4mNormal\033m, com o IMC de {imc:.4}')
elif imc < 29.9:
    print(f'Pela tabela fornecida pela OMS, você está no grau 1 de obesidade e está com a classificação \033[31;4mSobrepeso\033m, com o IMC de {imc:.4}')
elif imc < 39.9:
    print(f'Pela tabela fornecida pela OMS, você está no grau 2 de obesidade e está com a classificação \033[31;4mObesidade\033m, com o IMC de {imc:.4}')
elif imc > 40:
    print(f'Pela tabela fornecida pela OMS, você está no grau 3 de obesidade e está com a classificação \033[35;4mObesidade Grave\033m, com o IMC de {imc:.4}')
