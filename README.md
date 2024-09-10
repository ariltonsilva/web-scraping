# Web Scraping de Notícias com Selenium - Deadpool

## Visão Geral
Este repositório contém um script em Python que utiliza o Selenium para automatizar a navegação no site Omelete e realizar a busca por notícias relacionadas ao personagem Deadpool. O script captura os títulos e as datas das notícias e armazena os resultados em um arquivo `.txt`.

## Funcionalidades
- Automatiza a pesquisa de notícias no site do Omelete.
- Captura títulos e datas de notícias.
- Armazena os resultados em um arquivo de texto.

## Requisitos
Antes de rodar o script, certifique-se de que você tem os seguintes componentes instalados:

- Python 3.x
- Selenium
- WebDriver do Chrome (compatível com a versão do Chrome instalada)

Você pode instalar as dependências usando o seguinte comando:

```bash
pip install selenium
```

Além disso, baixe o Chrome WebDriver compatível com a versão do seu navegador [aqui](https://sites.google.com/a/chromium.org/chromedriver/downloads) e adicione-o ao seu PATH, ou mantenha o arquivo no mesmo diretório do script.

## Configuração

1. Clone o repositório:
   ```bash
   git clone https://github.com/ariltonsilva/web-scraping.git
   cd web-scraping
   ```

2. Instale as dependências:
   ```bash
   pip install selenium
   ```

3. Certifique-se de que o `chromedriver` está instalado e configurado corretamente no PATH ou no diretório do projeto.

## Uso

Para rodar o script:

```bash
python deadpool.py
```

O script executa as seguintes etapas:

1. Abre o navegador Chrome usando o Selenium.
2. Acessa o site [Omelete](https://www.omelete.com.br/).
3. Clica no ícone de pesquisa e realiza uma busca por "Deadpool".
4. Captura os títulos e datas das notícias exibidas nos resultados.
5. Armazena as informações no arquivo `noticias_deadpool.txt`.

## Exemplo de Saída

Após a execução, o arquivo `noticias_deadpool.txt` conterá resultados semelhantes a este:

```
10/09/2024 - Deadpool 3: Novo trailer revela mais detalhes do filme
05/08/2024 - Ryan Reynolds comenta sobre o futuro de Deadpool no MCU
...
```

## Observações

- O script utiliza uma espera explícita para garantir que o campo de busca esteja interativo antes de inserir o termo de pesquisa.
- Em caso de falha na interação com o campo de busca (por exemplo, por lentidão na página), uma mensagem de erro será exibida.

## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias e correções.

## Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
