from flask import Flask ,jsonify ,request
from flask_cors import CORS
import os 
import json
from jsondata import save_json,load_data,save_data,gen_id,find_age,Id_NOT_Found
app = Flask(__name__)
CORS(app)


@app.route("/")
@app.route("/users")
def user(): 
    data=load_data()
    return jsonify(data) 



@app.route("/get/<int:id>",methods=['GET'])
def userpost(id): 
    id_recored=find_age(id)
    if not id_recored:
        return jsonify({"error":"data not found"}) , 404
    return jsonify(id_recored) ,200



@app.route("/new_user",methods=["POST","GET"])
def save(): 
    
    new_data=request.json 
    new_data["id"]=gen_id()
    if not new_data: 
        return jsonify({"message":"data is not preent"}),405
    save_json(new_data)
    data=load_data()[len(load_data())-1]
    return jsonify({"message":f"{ data} data is saved" }),200


@app.route("/delete_user/<int:id>",methods=["POST","GET"])
def delete_user(id): 
    if  Id_NOT_Found(id): 
        return jsonify({"message":f"{id} id invalid !"}),404
    new_record=[]
    data=load_data()
    index=1
    for i in data: 
       if(i["id"]>id):
           i["id"]=index
           index+=1
           new_record.append(i)
       elif(i["id"]<id) :
           i["id"]=index 
           index+=1
           new_record.append(i) 
                  
    save_data(new_record) 
    return jsonify({"message":f"{id} is deleted"})      



@app.route("/update/<int:id>",methods=["POST","GET"])
def update(id): 

    if Id_NOT_Found(id) :
        return jsonify({"error":"id is not found "}) , 404
    data=load_data()
    new_rec= request.json 
    for i in data: 
        if(i["id"]==id): 
            i["id"]= id 
            i["name"]=new_rec["name"]
            i["age"]=new_rec["age"]
            i["marks"]=new_rec["marks"]   
    save_data(data)
    print(new_rec)
    return jsonify({"save":"data is saved"}) , 200

if __name__ == "__main__": 
    app.run(debug=True)