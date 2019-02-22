"""
Given a “flatten” dictionary object, whose keys are dot-separated. For example, { ‘A’: 1, ‘B.A’: 2, ‘B.B’: 3, ‘CC.D.E’: 4, ‘CC.D.F’: 5}.
Implement a function in any language to transform it to a “nested” dictionary object. In the above case, the nested version is like:
{'A':1, {B:{A:2,B:3}}, {'CC':{D:{E:4}}}....}
"""


def flattenToNestedDic(dic):
    def merge_dic(dic1, dic2):
        for k, v in dic2.items():
            if k not in dic1:
                dic1[k] = v
            else:
                if type(v) is dict:
                    v = merge_dic(dic1[k], dic2[k])
                dic1[k] = v
        return dic1

    def helper(key_list, v):
        s = {}
        if len(key_list) > 1:
            s[key_list[0]] = helper(key_list[1:], v)
        else:
            s[key_list[0]] = v
        return s
    dic_lst = []
    new_dic = {}
    for k, v in dic.items():
        # ** helper(k.split('.'), v)
        dic_lst.append(helper(k.split('.'), v))
    # [{'A': 1}, {'B': {'B': 2}}, {'B': {'C': 4}}, {'BA': {'D': 4}}, {'BC': {'A': {'A': 7}}}, {'BC': {'A': {'B': 6}}}]
    for i in dic_lst:
        merge_dic(new_dic, i)

    print(new_dic)
    return new_dic


_d = {'A': 1, 'B.B': 2, 'B.C': 4, 'BA.D': 4, 'BC.A.A':7, 'BC.A.B':6}
flattenToNestedDic(_d)
