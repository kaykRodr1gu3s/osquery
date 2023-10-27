# osquery_API

![GitHub](https://img.shields.io/github/license/kaykRodr1gu3s/osquery_API)
![GitHub language count](https://img.shields.io/github/languages/count/kaykRodr1gu3s/osquery_API)

Este código é usado para fazer a interação com o Elastic SIEM para criar, lista queries com a integração do Osquery.

![images](https://github.com/kaykRodr1gu3s/osquery/assets/110197812/8d72536d-86f2-48ae-8df7-831ff073d3c6)



## Como utilizar 
No campo json passe a sua query ja pronta.

```python
 json={
  "id": "saved_query_id",
  "description": "Saved query description",
  "query": "select * from uptime;",
  "interval": "60",
  "version": "2.8.0",
  "platform": "linux,darwin",
  "ecs_mapping": {
    "host.uptime": {
      "field": "total_seconds"
    }
```

após fazer as alterações, execute o código.
se o code response for 200, as requisições foi ocorrida corretamente 


## como contribuir

Clone o repositório, efetue as mudanças , efetue o Pull Request
