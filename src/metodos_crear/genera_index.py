from elasticsearch import Elasticsearch

from archivos_json import doc_json

es = Elasticsearch()

print("paso por metodo crear")
#res = es.index(index="test-index",doc_type='tweet',id=1,body=doc_json.doc0)
#print(res['result'])
#res = es.index(index="test-index",doc_type='tweet',id=2,body=doc_json.doc1)
#print(res['result'])
#res = es.index(index="test-index",doc_type='tweet',id=3,body=doc_json.doc2)
#print(res['result'])
#res = es.index(index="test-index",doc_type='tweet',id=4,body=doc_json.doc3)
#print(res['result'])
#res = es.index(index="test-index",doc_type='tweet',id=5,body=doc_json.doc4)
#print(res['result'])
#res = es.index(index="test-index",doc_type='tweet',id=6,body=doc_json.doc5)
#print(res['result'])
#res = es.index(index="test-index",doc_type='tweet',id=7,body=doc_json.doc6)
#print(res['result'])
#res = es.index(index="test-index",doc_type='tweet',id=8,body=doc_json.doc7)
#print(res['result'])


#res = es.get(index="test-index",doc_type='tweet')
#print(res['_source'])

#es.indices.refresh(index="test-index")

# con esto consultamos datos especificos
#v_autor = "cuadrado"
#res = es.search(index="test-index", body={"query": {"bool":{ "must": [{ "match": { "autor": v_autor}}]}}})
#print("Got %d Hits:" % res['hits']['total']['value'])
#for hit in res['hits']['hits']:
#    print("%(timestamp)s %(autor)s: %(text)s" % hit["_source"],hit["_id"])
#    id_es = hit["_id"]
