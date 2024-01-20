def construct_forest(list):
    # tree fonksiyonları
    def datum(tree):
        return tree[0]
    #node oluşturma
    def makenode(datum,operator, left=[], right=[]):
        return [datum, operator, [left], [right]]
    # boşlukları kaldırma
    def remove_spaces(lst):
        return [item.replace(' ', '') for item in lst]
    # fonksiyon ismini alma
    def get_func_name(string):
        parts = string.split("=")
        return parts[0]
    def tree_fonksiyon_ismi(string):
        parts = string.split("(x)")
        return parts[0]
    # parametre
    def get_parameters(string):
        equal_index = string.find("=")
        if "^" in string:
         operator_index = string.find("^", equal_index)
        if "+" in string:
         operator_index = string.find("+", equal_index)
        if "*" in string:
         operator_index = string.find("*", equal_index)
        if "-" in string:
         operator_index = string.find("-", equal_index)
        part1 = string[equal_index + 1:operator_index]
        part2 = string[operator_index + 1:]
        if "(x)" in string[operator_index+1:] and "(x)" not in string[equal_index+1:operator_index]:
            start_of_func=string[operator_index+1:].split("(x)")
            return part1, start_of_func[0]
        if "(x)" not in string[operator_index+1:] and "(x)" in string[equal_index+1:operator_index]:
            start_of_func=string[equal_index+1:operator_index].split("(x)")
            return start_of_func[0], part2
        if "(x)" in string[operator_index+1:] and "(x)" in string[equal_index+1:operator_index]:
            start_of_func=string[operator_index+1:].split("(x)")
            start_of_func2=string[equal_index+1:operator_index].split("(x)")
            return start_of_func2[0], start_of_func[0]
        return part1, part2
    # fonksiyon ismini ağaçlar içinde arama
    def func_searching(name,agaç):
        i = 0
        while i < len(agaç):
            if name == datum(agaç[i]):
                return agaç[i]
            else:
                i += 1
    # ilk tree
    no_space = remove_spaces(list)
    tree1 = []
    i=0
    # ziyaret edilenler
    visited = []
    while i < len(no_space):
        func_name = get_func_name(no_space[i])
        tree_fonksiyon=tree_fonksiyon_ismi(no_space[i])
        parameter1, parameter2 = get_parameters(no_space[i])
        if "^" in no_space[i]:
            operator="^"
        if "+" in no_space[i]:
            operator="+"
        if "*" in no_space[i]:
            operator="*"
        if "-" in no_space[i]:
            operator="-"
        if func_name not in visited:
            visited.append(tree_fonksiyon)
        a = makenode(tree_fonksiyon, operator, parameter1, parameter2)
        tree1.append(a)
        i += 1
        # sonradan dal kaldırma
        def delete_node(agac, silinecek):
            i = 0
            if len(silinecek) == 0: return agac
            while 0 != len(silinecek) and i < len(agac):
                if datum(agac[i]) == silinecek[0]:
                    del agac[i]
                    return delete_node(agac, silinecek[1:])
                if datum(agac[i]) != silinecek[0]:
                    i += 1
            return agac
    # ikinci tree
    def replacing_right_places(tree,delete_later):
     if type(tree[0])== str and type(tree[1]) == str and len(tree)==4 :
         if  tree[2][0] not in visited and tree[3][0] not in visited:
             return [tree,tree]
         if tree[2][0] in visited and tree[3][0] in visited:
             if tree[3][0] not in delete_later:
              delete_later.append(tree[3][0])
             if tree[2][0] not in delete_later:
              delete_later.append(tree[2][0])
             tree[2] = replacing_right_places(func_searching(tree[2][0],tree1),delete_later)[0]
             tree[3] = replacing_right_places(func_searching(tree[3][0],tree1),delete_later)[0]
         if tree[2][0] in visited and tree[3][0] not in visited:
             if tree[2][0] not in delete_later:
              delete_later.append(tree[2][0])
             tree[2]= replacing_right_places(func_searching(tree[2][0],tree1),delete_later)[0]
         if tree[3][0] in visited and tree[2][0] not in visited:
             if tree[3][0] not in delete_later:
              delete_later.append(tree[3][0])
             tree[3]= replacing_right_places(func_searching(tree[3][0],tree1),delete_later)[0]
     else:
      i=0
      while i < len(tree) :
        left_char = tree[i][2][0]
        right_char = tree[i][3][0]
        if left_char in visited and right_char in visited:
            if right_char not in delete_later:
             delete_later.append(right_char)
            if left_char not in delete_later:
             delete_later.append(left_char)
            tree[i][2]= replacing_right_places(func_searching(left_char,tree1),delete_later)[0]
            tree[i][3] = replacing_right_places(func_searching(right_char,tree1),delete_later)[0]
        if left_char in visited and right_char not in visited:
            if left_char not in delete_later:
             delete_later.append(left_char)
            tree[i][2]= replacing_right_places(func_searching(left_char,tree1),delete_later)[0]
        if right_char in visited and left_char not in visited:
            if right_char not in delete_later:
             delete_later.append(right_char)
            tree[i][3] = replacing_right_places(func_searching(right_char,tree1),delete_later)[0]
        i+=1
     return [tree,delete_later]
    [silmeden_önce, delete_late ]=replacing_right_places(tree1,[])
    return delete_node(silmeden_önce,delete_late)
