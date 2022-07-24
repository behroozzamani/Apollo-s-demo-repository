def cloud_function(json_input):
    original = json_input["original_str"]
    
    # Processing
    splited_arr=original.strip()
    result= splited_arr
    # return the result
    res = {
        "original_arr": result
    }
    return res
