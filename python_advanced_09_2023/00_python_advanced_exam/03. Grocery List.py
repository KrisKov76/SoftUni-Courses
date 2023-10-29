def shop_from_grocery_list(*args):
    budget = args[0]
    grocery_lst = list(args[1])
    bought_products = {}

    for product, sum_ in args[2:]:
        if product not in grocery_lst:
            continue
        if budget < sum_:
            break
        if product not in bought_products:
            bought_products[product] = 0
            grocery_lst.remove(product)
        bought_products[product] = sum_
        budget -= sum_

    result = ''

    if len(grocery_lst) == 0: # if not grocery_lst:
        result += f"Shopping is successful. Remaining budget: {budget:.2f}.\n"
    else:
        result += f"You did not buy all the products. Missing products: {', '.join(grocery_lst)}.\n"

    return result