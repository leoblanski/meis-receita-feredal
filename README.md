# Extrator de dados Receita Federal

Este projeto reúne uma solução completa para o processamento dos dados públicos de CNPJ disponibilizados pela Receita Federal do Brasil. A ideia é extrair, transformar e carregar (ETL) os dados para um banco de dados PostgreSQL e, a partir daí, gerar arquivos CSV segmentados para facilitar análises e abordagens comerciais (por exemplo, via WhatsApp).

## 📦 Recursos do Projeto

- **Docker e Docker Compose**  
  Ambiente isolado com:
  - **PostgreSQL 14.2**: Banco de dados relacional para armazenar os dados tratados.
  - **Adminer**: Ferramenta web para visualização e gerenciamento do PostgreSQL (semelhante ao phpMyAdmin).

- **Processo ETL**  
  Automatiza:
  - Download dos arquivos da Receita Federal.
  - Extração e transformação dos dados.
  - Inserção dos dados nas tabelas do PostgreSQL.
  - Criação de índices para otimização de consultas.

- **Geração de CSV**  
  Script para filtrar os dados com critérios (ex: MEI, CNAEs pertinentes a comércio/varejo, estabelecimentos com data de início em um determinado ano) e exportar o resultado para um arquivo CSV, pronto para ser importado em ferramentas como o Google Drive.

- **Automação de WhatsApp (opcional)**  
  Script com **Selenium** para disparar mensagens automaticamente via WhatsApp Web. Ideal para testes de abordagem com um lote pequeno (ex: 20 contatos) para validar o interesse de potenciais clientes.

## 📂 Estrutura de Pastas

```plaintext
.
├── docker-compose.yml           # Arquivo para subir os containers do PostgreSQL e Adminer
├── banco_de_dados.sql           # Script de criação das tabelas e índices
├── code/
│   ├── .env_template            # Template com as variáveis de ambiente
│   ├── ETL_coletar_dados_e_gravar_BD.py   # Script para realizar o processo ETL
│   ├── export_mei_vendas_2025.py           # Script para gerar CSV com dados filtrados
│   └── whatsapp_fastcontrol.py             # Script para disparo de mensagens via WhatsApp
├── downloads/                   # Diretório para os arquivos baixados (ZIPs)
├── extracted/                   # Diretório para os arquivos descompactados
└── mei_vendas_2025.csv          # CSV gerado (após execução do script de exportação)
```

## ⚙️ Pré-requisitos

- **Python 3.8+**

- **Docker e Docker Compose**  
  Instale o [Docker](https://docs.docker.com/get-docker/) e o [Docker Compose](https://docs.docker.com/compose/install/).

- **Google Chrome + ChromeDriver**  
  Necessários para a automação do WhatsApp via Selenium.

  - Verifique a versão do seu Google Chrome acessando:  
    `chrome://settings/help`

  - Baixe o ChromeDriver correspondente aqui:  
    [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)

  - Ou instale via Homebrew (macOS):

    ```bash
    brew install chromedriver
    ```

    > Dica: pode ser necessário rodar `xattr -d com.apple.quarantine /path/to/chromedriver` após instalar.

- **Dependências Python**  
  Instale com:

  ```bash
  pip install -r requirements.txt
	•	Instale o ChromeDriver compatível com a versão do seu Google Chrome ou use Homebrew:
