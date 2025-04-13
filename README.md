[![License](https://img.shields.io/badge/license-MIT-_red.svg)](https://opensource.org/licenses/MIT)
[![Contribuitions Welcome](https://img.shields.io/badge/contribuitions-welcome-brightgreen.svg?style=flat)](https://github.com/bluurw/carbon/issues)

# **Proxy**

## **Descrição**

O projeto Proxy gera uma lista de proxies gratuitas e seguras, testadas e validadas. Ele coleta, filtra e valida dados de fontes diversas para oferecer aos usuários proxies confiáveis para uso em diferentes contextos, incluindo automação, web scraping e navegação anônima.

## **Como Instalar**

Siga os passos abaixo para instalar e executar o projeto:

Clone o repositório
```bash
git clone https://github.com/bluurw/prox-y.git
```

Entre na pasta do projeto
```bash
cd prox-y
```

Crie um ambiente virtual (opcional, mas recomendado)
```bash
python3 -m venv venv
source venv/bin/activate
```

Instale as dependências
```bash
pip install -r requirements.txt
```

Execute o código principal
```bash
python main.py
```

## **TO DO**

Desenvolver o módulo de teste de proxy:
Implementar funcionalidade para testar a conectividade de cada proxy, verificando se estão ativas e operacionais.

Incluir limitações de resultado:
- Quantidade: Permitir limitar o número de proxies retornados.
- Local (país/região): Filtrar proxies por localização geográfica.
- Tipo de protocolo: Selecionar entre HTTP, HTTPS, SOCKS, etc.
- Nível de anonimato: Classificar proxies por níveis (alta, média, baixa).
- Velocidade/tempo de resposta: Incorporar filtros para proxies rápidas e estáveis.
- Data de verificação: Incluir a data/hora da última validação do proxy.
- (Outros filtros poderão ser adicionados conforme a necessidade do projeto.)

## **Compatibilidade**
Linux: OK
Windows: Não testado
Mac: Não testado

## **Licença**

Este projeto é licenciado sob a Licenca do MIT.