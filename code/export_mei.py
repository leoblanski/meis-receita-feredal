import pandas as pd
import psycopg2

conn = psycopg2.connect(
    dbname="Dados_RFB",
    user="rfb_user",
    password="rfb_password",
    host="localhost",
    port="5432"
)

query = """
SELECT 
  e.cnpj_basico || est.cnpj_ordem || est.cnpj_dv AS cnpj_completo,
  e.razao_social,
  est.nome_fantasia,
  est.uf,
  est.municipio,
  est.logradouro,
  est.numero,
  est.bairro,
  est.cep,
  est.correio_eletronico AS email,
  est.ddd_1 || est.telefone_1 AS telefone_1,
  est.ddd_2 || est.telefone_2 AS telefone_2,
  TO_DATE(est.data_inicio_atividade::text, 'YYYYMMDD') AS data_inicio_atividade,
  cnae.codigo AS cnae_codigo,
  cnae.descricao AS cnae_descricao,
  natju.descricao AS natureza_juridica

FROM empresa e
JOIN estabelecimento est ON e.cnpj_basico = est.cnpj_basico
JOIN simples s ON e.cnpj_basico = s.cnpj_basico
JOIN cnae ON est.cnae_fiscal_principal = cnae.codigo::integer
JOIN natju ON e.natureza_juridica = natju.codigo

WHERE 
  s.opcao_mei = 'S'
  AND est.data_inicio_atividade::text LIKE '2025%'
  AND natju.descricao = 'Empresário (Individual)'
  AND LOWER(cnae.descricao) SIMILAR TO 
      '%(loja|roupa|moda|calçado|confecção|cosmético|mercearia|ambulante|vendedor|itinerante|sinal|feira|artesanato|bijuteria|revenda|venda domiciliar|varejo)%'

ORDER BY e.razao_social
"""

df = pd.read_sql_query(query, conn)
df.to_csv("mei_vendas_2025.csv", index=False, encoding="utf-8")
conn.close()

print("Export completed: mei_vendas_2025.csv")