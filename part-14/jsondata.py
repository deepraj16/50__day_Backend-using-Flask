import json 
import os 

file_name="data.json"

def load_data(): 
    try: 
        with open("data.json") as f :
            data=json.load(f)
            if not isinstance(data,list):
                return [] 
            else: return data    
    except json.JSONDecodeError: 
        return []        
    
def save_data(data): 
    try: 
        with open(file_name,"w") as f: 
            json.dump(data,f,indent=4)
    except FileNotFoundError : 
        print("No file found")        

def save_json(kwargs):
    global file_name 
    
    student={
        "id":kwargs["id"],
        "name":kwargs["name"],
        "age":kwargs["age"], 
        "marks":kwargs["marks"]
    } 

    if os.path.exists(file_name): 
        try : 
            with open(file_name,"r") as f: 
                data=json.load(f) 
                if not isinstance(data,list):
                    data=[]
        except json.JSONDecodeError :
            data=[]
    else : 
        data=[]

    data.append(student) 
    with open(file_name , "w") as f: 
        json.dump(data,f,indent=4)
    print(f"data is saved")                



def all_data(): 
    try: 
        with open("data.json","r") as f : 
            data=json.load(f)
            if not isinstance(data,list): 
                data=[]
    except FileNotFoundError :
        data=[]

    return data   

def gen_id():
    data=load_data()
    if len(data)==0 : return 1
    last_id=data[len(data)-1]["id"]
    return last_id+1


def find_age(id) : 
    data=load_data()
    for i in data: 
        if(i['id']==id): 
            return i
    return None

def Id_NOT_Found(id): 
    data=load_data()
    for i in data:
        if i["id"]==id: 
            return False
    return True    


#save_json(id=2,name="Omkar",age=21,marks=23)


  