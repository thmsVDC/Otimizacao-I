def dict_to_list(dict):
  list = []
  for key, value in dict.items():
      list.append(value)
  return list

def restrictions_dict_to_list(restrictions_dict, num_restrictions):
    restrictions_list = [[] for _ in range(num_restrictions)]
    for key, value in restrictions_dict.items():
        _, restriction_idx, var_idx = key.split('_')
        restriction_idx = int(restriction_idx)
        restrictions_list[restriction_idx].append(float(value))
    return restrictions_list

def invert_restriction_signs(operators, restrictions, restrictions_right):
    for i, (key, value) in enumerate(operators.items()):
        if value == '>=':
            restrictions[i] = [-value for value in restrictions[i]]
            restrictions_right[i] = -restrictions_right[i]
    return restrictions, restrictions_right
