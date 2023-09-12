def construct_forest(defs):

    # creating new definitions list without the spaces between them since we dont know how many there will be of it.
    new_defs = []

    for i in defs:
        a = i.replace(" ","")
        new_defs.append(a)

    # creating a dictionary with functions with key as the names and the wanted lists of each function as the values. but these doesnt have explanations of the function if a function is a term itself.
    dict = {}

    for i in new_defs:

        operators = ["+", "-", "*", "^"]
        eq_index = i.index("=")

        for k in operators:
            if k in i:
                operator = k
                op_index = i.index(k)
            
        func_name = i[0] 
        term_1 = i[eq_index+1:op_index]
        term_2 = i[op_index+1:]

        dict[i[:4]] = [func_name, operator, [term_1],[term_2]]    
        # for example {"a(x)": ["a","*",["x"],["20"]]}

    # this helper functions finds out the terms as functions and updates the dictionary with equivalents of functions.
    def value(j,i):
    
        func_name = i[0]
        operator = i[1]
        term_1 = i[2][0]
        term_2 = i[3][0]

        if "(x)" not in term_1 and "(x)" not in term_2:
            dict.update()

        elif "(x)" in term_1 and "(x)" not in term_2 :
            value(term_1,dict.get(term_1))
            a = dict.get(term_1)
            dict.update({j:[func_name,operator,a,[term_2]]})
        
        elif "(x)" in term_2 and "(x)" not in term_1 :    
            value(term_2,dict.get(term_2))
            a = dict.get(term_2)
            dict.update({j:[func_name,operator,[term_1],a]})  

        else: 
            value(term_1,dict.get(term_1))
            value(term_2,dict.get(term_2))
            a = dict.get(term_1)
            b = dict.get(term_2)
            dict.update({j:[func_name,operator,a,b]})

    # now we are going to update the dictionary with the help of this function. 
    for j,i in dict.items():
        value(j,i)    


    # if a function is in another function, we will delete that function and the functions in it if there is any, from the dictionary. 
    # so lets first make a list of functions which will be deleted from dictionary.
    deleted_list= []
    for i in dict.values():
        func_name = i[0]
        operator = i[1]
        term_1 = i[2]
        term_2 = i[3]
        if len(term_1) != 1:
            deleted_list.append(term_1[0])
        if len(term_2) != 1:
            deleted_list.append(term_2[0])
        
    # it is time to delete them from the dictionary
    for i in deleted_list:
        a = i + "(x)"
        if a in dict.keys():
            dict.pop(a)
    
    # now lets make a list of the remaning values and return it
    result_list = []
    for i in dict.values():
        result_list.append(i)

    return result_list
            