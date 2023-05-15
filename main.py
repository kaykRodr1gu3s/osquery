import requests
import pandas as pd 
from pandas import DataFrame
import secrets


xsrf_token = secrets.token_hex(16)

# creating live-query

create_live_query = ' '
create_live_query = requests.post('<kibana host>:<port>/api/osquery/live_queries/<id>',
                    headers={"Authorization": "your ApiKey", 'Content-Type': 'application/json', "kbn-xsrf": xsrf_token},
                    json={
                        "your query name": "select * from uptime;",

                        "ecs_mapping": {
                            "host.uptime": {
                            "field": "total_seconds"
                            }
                        },
                        "agent_all": True,
                        })

#creating saved-query

creating_saved_query = ' '
creating_saved_query = requests.post("<kibana host>:<port>/api/osquery/saved_queries",
                   headers={"authorization" : "your ApiKey", "content-type": "application/json", "kbn-xsrf": xsrf_token}, 
                   
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
  }
})

print(creating_saved_query.status_code)



#getting packs
getting_packs = ' '
getting_packs = requests.get("<kibana host>:<port>/api/osquery/packs/<id>", 
                   headers={"authorization": "your ApiKey", "content-type" : "application/json", "kbn-xsrf": xsrf_token}
                   )


# saving the results in a csv file
#you can put any variable that has been created for see the results 

saving = pd.DataFrame(creating_saved_query.json())
saving.to_csv('the file name.csv')