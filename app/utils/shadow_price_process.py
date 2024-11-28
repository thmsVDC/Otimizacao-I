from scipy.optimize import linprog


def calculate_shadow_price(result, variables_list, restrictions_list, restrictions_right_list):
    sol_original = result.fun
    shadow_prices = []
    restrictions_right_modified = []
    for i in range(len(restrictions_right_list)):
        restrictions_right_modified = restrictions_right_list.copy()
        restrictions_right_modified[i] -= 1
        result_modified = linprog(variables_list, A_ub=restrictions_list, b_ub=restrictions_right_modified,
                                  bounds=[(0, None)] * len(variables_list), method='simplex')
        
        sol_modified = result_modified.fun
        shadow_price = sol_original - sol_modified
        shadow_prices.append(-shadow_price)
    return shadow_prices
