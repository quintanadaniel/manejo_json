from elasticsearch import Elasticsearch

es = Elasticsearch()

def delete_all_datos_es():
    res_delete_all = es.count(index="test-index",doc_type="tweet")
    res_del_all = res_delete_all["count"]
    #print(res_del_all," ",len(range(res_del_all)))
    i= 1
    if i <= len(range(res_del_all)):
        while i <= len(range(res_del_all)):
            print("antes de delete_es_all")
            delete_es_all = es.delete(index="test-index",doc_type="tweet",id=len(range(res_del_all)))
            print("despues de delete_es_all")
            if i <= len(range(res_del_all)):
                print("cantidad: ",res_delete_all," borrando registro ",delete_es_all)
            else:
                print("No existe el id, procedemos a buscarlo y borrarlo")
    elif i > len(range(res_del_all)):
        print("No existen id creados para borrar masivamente")
    
    es.indices.refresh(index="test-index")
    

def delete_id_datos_es(v_id):        
    vl_id = int(v_id)
    delete_es_id = es.delete(index="test-index",doc_type="tweet",id=vl_id)
    return print("se borra el id: ",delete_es_id)
    



