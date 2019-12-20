from elasticsearch import Elasticsearch

es = Elasticsearch()


# se buscan todos lo que coincida
res = es.search(index="test-index", body={"query": {"match_all":{}}})
#print(res)
print("Got %d Hits:" % res['hits']['total']['value'])
for hit in res['hits']['hits']:
    print("%(timestamp)s %(autor)s: %(text)s" % hit["_source"])

print("----------------------------------------------------------------------")
# buscamos lo que contenga pelota
res_pelota = es.search(index="test-index",body={ "query": { "bool":{ "must": [ {"match":{ "autor": "pelota" }}]}}})
#print(res_pelota)
for pelota in res_pelota['hits']['hits']:
    print("%(timestamp)s %(autor)s: %(text)s" % pelota["_source"])

print("----------------------------------------------------------------------")
# buscamos lo que contenga cuadrado
res_cuadrado = es.search(index="test-index",body={ "query": { "bool":{ "must": [ {"match":{ "autor": "cuadrado" }}]}}})
#print(cuadrado)
for cuadrado in res_cuadrado['hits']['hits']:
    print("%(timestamp)s %(autor)s: %(text)s" % cuadrado["_source"])

print("----------------------------------------------------------------------")
word1 = "cadena"
# filtramos la palabra cadena del campo text
res_cadena = es.search(index="test-index",body={ "query": { "bool":{ "should": { "term": { "text": word1}}}}})
if res_cadena["hits"]["total"]["value"] == 0:
    print("no hay datos buscando la palabra", word1)
else:
    for cadena in res_cadena['hits']['hits']:
        print("%(timestamp)s %(autor)s: %(text)s" % cadena["_source"])

print("----------------------------------------------------------------------")
word = "elasticsearch"
# filtramos la palabra probando del campo text
res_probando = es.search(index="test-index",body={ "query": { "bool":{ "filter": { "term": { "text": word}}}}})
if res_probando["hits"]["total"]["value"] == 0:
    print("no hay datos buscando la palabra", word)
else:    
    for probando in res_probando['hits']['hits']:
        print("%(timestamp)s %(autor)s: %(text)s" % probando["_source"])

print("----------------------------------------------------------------------")
word3 = "cadena"
# filtramos la palabra probando del campo text
res_combina = es.search(index="test-index",body={ "query": { "bool":{ "must": { "match_all": {}}, "filter": { "term": { "autor": "pelota"}}}}})
if res_combina["hits"]["total"]["value"] == 0:
    print("no hay datos buscando la palabra", word3)
else:    
    for combina in res_combina['hits']['hits']:
        print("%(timestamp)s %(autor)s: %(text)s" % combina["_source"])

print("-----------------------------------------------------------------------")
# buscamos datos para trearnos el maximo registro de un grupo del mismo
#res_maximo = es.search(index="test-index",body={ "query": { "dis_max": { "tie_breaker": 0.7 ,"boots": 1.2,"queries": [ { "term": {"year" : 20 }, { "term": { "year": 30}}}]}})
#if res_maximo["hist"]["total"]["value"] == 0:
