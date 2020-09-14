

def return_result():
    #f = open('bioRE/mtdnn_weight_new/Predict_result/result.txt')
    import json # import json module
    import re

    f = open('dl/User_input/prepro_result/ddi_test.tsv')
    user_input = f.readlines()
    user_result_list = ""
    with open('dl/model_result/ddi_result.json') as json_file:
        with open('dl/User_output/DDI_result.txt',"w") as writer:
            json_data = json.load(json_file)
            model_predict = json_data['predictions']
            for user,result in zip(user_input, model_predict):
                user = user.split('\t')[2]
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
                user_result = str(user)+'\t'+str(result)+'\n'
                user_result_file = user_result
                user_result = re.sub(r"@DRUG\$",r'<span style="background-color:yellow">@DRUG$</span>',user_result)
                user_result_list+= user_result + "\n"
                writer.write(user_result_file)
                #print(user_result_list)
    return user_result_list
