# Análise de Dados de Absorbância

Este repositório contém um programa Python para realizar a análise de dados de absorbância provenientes de um espectrofotômetro. O programa utiliza a biblioteca Pandas para manipulação de dados, o Matplotlib para visualização gráfica e a biblioteca scikit-learn para implementar uma regressão linear.

## Pré-requisitos

Certifique-se de ter as seguintes bibliotecas instaladas antes de executar o programa:

```bash
pip install pandas numpy matplotlib scikit-learn
```

## Uso
Defina o caminho da pasta no Google Drive que contém os dados espectrofotométricos no código, na variável link.
Especifique as diferentes aliquotas desejadas no vetor aliquotas.
Execute o script Python.

## Funcionalidades
Coleta dados de absorbância máxima de cada arquivo na pasta correspondente à cada aliquota.
Calcula a média aritmética das amostras para cada aliquota.
Realiza uma regressão linear entre a concentração e a absorbância média.
Exibe a equação da reta de regressão no console.
Gera um gráfico da curva de calibração, mostrando a reta de regressão e os pontos de dispersão.
Exemplo de Resultado
A equação da reta de regressão gerada pelos dados de exemplo é:

�
=
0.0636447
�
+
0.3017013
y=0.0636447x+0.3017013

O gráfico resultante é exibido na seção de visualização do código.

Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas (issues) ou enviar solicitações de pull (pull requests) para melhorar este programa.



