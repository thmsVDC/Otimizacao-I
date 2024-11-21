def variables_dict_to_list(variables_dict):
    variables_list = []
    for key, value in variables_dict.items():
        variables_list.append(value)

    return variables_list


def restrictions_dict_to_list(restrictions_dict, num_restrictions):
    restrictions_list = [[] for _ in range(num_restrictions)]
    for key, value in restrictions_dict.items():
        _, restriction_idx, var_idx = key.split('_')
        restriction_idx = int(restriction_idx)
        restrictions_list[restriction_idx].append(float(value))

    return restrictions_list


def restrictions_right_dict_to_list(restrictions_right_dict):
    restrictions_right_list = []
    for key, value in restrictions_right_dict.items():
        restrictions_right_list.append(value)

    return restrictions_right_list


def invert_restriction_signs(operators, restrictions, restrictions_right):
    for i, (key, value) in enumerate(operators.items()):
        print(f"{key}: {value}")
        if value == '>=':
            restrictions[i] = [-value for value in restrictions[i]]
            restrictions_right[i] = -restrictions_right[i]

    return restrictions, restrictions_right
