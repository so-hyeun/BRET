# coding=utf-8
import json # import json module
import re
def chem_dis_func(f):
    return f+"Chemprot_disease_result_json"

def drug2_func(f):
    return f+"Drug_Drug_result_json"

def gene_dis_func(f):
    return f+"Gene_Disease_result_json"


def return_result_ddi(f, out_file):
    #f = open('bioRE/mtdnn_weight_new/Predict_result/result.txt')
    
    
    f = open(f) #origin user input
    user_input = f.readlines()[1:]
    user_result_list = ""
    with open('dl/model_result/ddi_result.json') as json_file: #model result json
        with open( out_file,"w") as writer:    #output 쓰는 file
            json_data = json.load(json_file)
            model_predict = json_data['predictions']
            for user,result in zip(user_input, model_predict):
                user = user.split('\t')[1]
                if result == 0: 
                    result = 'DDI-mechanism'
                elif result == 1:
                    result = 'DDI-effect'
                elif result == 2:
                    result = 'DDI-advise'
                elif result == 3:
                    result = 'DDI-int'
                else:
                    result = 'DDI-false'
                user_result = str(user)+' '+str(result)+'newline'
                user_result_ = re.sub(r"@DRUG\$",r'<s>@DRUG$</s>',user_result)
                user_result_file = user_result
                user_result_list+= user_result_
                writer.write(user_result_file)
                #print(user_result_list)
    return user_result_list

def return_result_chemprot(f, out_file):
    #f = open('bioRE/mtdnn_weight_new/Predict_result/result.txt')
    
    
    f = open(f)
    user_input = f.readlines()[1:]
    user_result_list = ""
    with open('dl/model_result/chemprot_result.json') as json_file: #model result json
        with open( out_file,"w") as writer:    #output 쓰는 file
            json_data = json.load(json_file)
            model_predict = json_data['predictions']
            for user,result in zip(user_input, model_predict):
                user = user.split('\t')[1]
                if result == 0: 
                    result = 'CPR:3'
                elif result == 1:
                    result = 'CPR:4'
                elif result == 2:
                    result = 'CPR:5'
                elif result == 3:
                    result = 'CPR:6'
                elif result == 4:
                    result = 'CPR:9'
                else:
                    result = 'CPR:false'
                user_result = str(user)+' '+str(result)+'newline'
                user_result_ = re.sub(r"BC6ENT1",r'<s>BC6ENT1</s>',user_result)
                user_result_ = re.sub(r"BC6ENT2",r'<s>BC6ENT2</s>',user_result_)
                user_result_ = re.sub(r"BC6ENTC",r'<s>BC6ENTC</s>',user_result_)
                user_result_ = re.sub(r"BC6ENTG",r'<s>BC6ENTG</s>',user_result_)
                user_result_ = re.sub(r"BC6OTHER",r'<s>BC6OTHER</s>',user_result_)
                
                user_result_file = user_result
                user_result_list+= user_result_
                writer.write(user_result_file)
                #print(user_result_list)
    return user_result_list

def return_result_gad(f, out_file):
    #f = open('bioRE/mtdnn_weight_new/Predict_result/result.txt')
    
    
    f = open(f)
    user_input = f.readlines()[1:]
    user_result_list = ""
    with open('dl/model_result/gad_result.json') as json_file: #model result json
        with open( out_file,"w") as writer:    #output 쓰는 file
            json_data = json.load(json_file)
            model_predict = json_data['predictions']
            for user,result in zip(user_input, model_predict):
                user = user.split('\t')[1]
             
                
                user_result = str(user)+' '+str(result)+'newline'
                user_result_ = re.sub(r"@GENE\$",r'<s>@GENE$</s>',user_result)
                user_result_ = re.sub(r"@DISEASE\$",r'<s>@DISEASE$</s>',user_result_)
                
                user_result_file = user_result
                user_result_list+= user_result_
                writer.write(user_result_file)
                #print(user_result_list)
    return user_result_list