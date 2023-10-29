# def data_types(input_value):
#     try:
#         float_value = float(input_value)
#         if float_value.is_integer():
#             return float_value * 2
#         else:
#             return f'{float_value * 1.5:.2f}'
#     except ValueError:
#         return f'${input_value}$'
#
# a = input()
# print(data_types(a))



def data_types(input_type, input_value):
    if input_type == "int":
        return int(input_value) * 2
    elif input_type == "real":
        return f'{float(input_value) * 1.5:.2f}'
    else:
        return f'${input_value}$'

input_type_one = input()
input_value_one = input()

print(data_types(input_type_one, input_value_one))
