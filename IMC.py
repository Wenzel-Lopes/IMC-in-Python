print('**********************************************')
print('*             CALCULADORA DE IMC             *')
print('**********************************************')

enter = input('Pressione \"ENTER\" para iniciarmos o nosso programa: ')

peso = float(input('Isira o seu peso (kg): '))
altura = float(input('Insira a sua altura (cm): '))

imc = peso / (altura ** 2)

if imc < 16.00:
    print('                                          ')
    print('|   CLASSIFICAÇÃO     |        IMC       |')
    print('| Baixo peso Grau III |  abaixo de 16.00 |')
    print('                                          ')
    print('Seu IMC é: {:.2f}'.format(imc))
elif imc >= 16.00 and imc < 17.00:
    print('                                          ')
    print('|   CLASSIFICAÇÃO     |        IMC       |')
    print('| Baixo peso Grau II  |   16.00 a 16.99  |')
    print('                                          ')
    print('Seu IMC é: {:.2f}'.format(imc))
elif imc >= 17.00 and imc < 18.50:
    print('                                          ')
    print('|   CLASSIFICAÇÃO     |        IMC       |')
    print('| Baixo peso Grau I   |   17.00 a 18.49  |')
    print('                                          ')
    print('Seu IMC é: {:.2f}'.format(imc))
elif imc >= 18.50 and imc < 25.00:
    print('                                          ')
    print('|   CLASSIFICAÇÃO     |        IMC       |')
    print('|     Peso ideal      |   18.50 a 24.99  |')
    print('                                          ')
    print('Seu IMC é: {:.2f}'.format(imc))
elif imc >= 25.00 and imc < 30.00:
    print('                                          ')
    print('|   CLASSIFICAÇÃO     |        IMC       |')
    print('|     Sobrepeso       |   25.00 a 29.99  |')
    print('                                          ')
    print('Seu IMC é: {:.2f}'.format(imc))
elif imc >= 30.00 and imc < 35.00:
    print('                                          ')
    print('|   CLASSIFICAÇÃO     |        IMC       |')
    print('|  Obesidade Grau I   |   30.00 a 34.99  |')
    print('                                          ')
    print('Seu IMC é: {:.2f}'.format(imc))
elif imc >= 35.00 and imc < 40.00:
    print('                                          ')
    print('|   CLASSIFICAÇÃO     |        IMC       |')
    print('|  Obesidade Grau II  |   35.00 a 39.99  |')
    print('                                          ')
    print('Seu IMC é: {:.2f}'.format(imc))
else:
    print('                                          ')
    print('|   CLASSIFICAÇÃO     |        IMC       |')
    print('| Obesidade Grau III  |    40.0 e acima  |')
    print('                                          ')
    print('Seu IMC é: {:.2f}'.format(imc))