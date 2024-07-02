# def create_char_count_dict(text):
#     char_count = {}
#     for char in text:
#         if char in char_count:
#             char_count[char] += 1
#         else:
#             char_count[char] = 1
#     return char_count

# def merge_dicts(dict1, dict2):
#     merged_dict = dict1.copy()
#     for key, value in dict2.items():
#         if key in merged_dict:
#             merged_dict[key] += value
#         else:
#             merged_dict[key] = value
#     return merged_dict

# text1 = "hello world"
# text2 = "world of code"

# char_count_dict1 = create_char_count_dict(text1)
# char_count_dict2 = create_char_count_dict(text2)

# print("Словник для тексту 1:", char_count_dict1)
# print("Словник для тексту 2:", char_count_dict2)

# merged_dict = merge_dicts(char_count_dict1, char_count_dict2)
# print("Об'єднаний словник:", merged_dict)



# def merge_dicts_with_lists(dict1, dict2):
#     merged_dict = dict1.copy()
#     for key, value in dict2.items():
#         if key in merged_dict:
#             if not isinstance(merged_dict[key], list):
#                 merged_dict[key] = [merged_dict[key]]
#             merged_dict[key].append(value)
#         else:
#             merged_dict[key] = value
#     return merged_dict

# def invert_dict(dict_to_invert):
#     inverted_dict = {}
#     for key, value in dict_to_invert.items():
#         inverted_dict[value] = key
#     return inverted_dict
# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {'b': 4, 'c': 5, 'd': 6}

# merged_dict = merge_dicts_with_lists(dict1, dict2)
# print("Об'єднаний словник:", merged_dict)

# dict_to_invert = {'a': 1, 'b': 2, 'c': 3}
# inverted_dict = invert_dict(dict_to_invert)
# print("Інвертований словник:", inverted_dict)



# def invert_dict(dict_to_invert):
#     inverted_dict = {}
#     for key, value in dict_to_invert.items():
#         inverted_dict[value] = key
#     return inverted_dict
# def sort_dict_by_keys(dict_to_sort):
#     sorted_dict = dict(sorted(dict_to_sort.items()))
#     return sorted_dict
# original_dict = {'a': 3, 'b': 1, 'c': 2}
# inverted_dict = invert_dict(original_dict)
# print("Інвертований словник:", inverted_dict)
# sorted_inverted_dict = sort_dict_by_keys(inverted_dict)
# print("Сортований інвертований словник:", sorted_inverted_dict)



# def sort_dict_by_keys(dict_to_sort, ascending=True):
#     return dict(sorted(dict_to_sort.items(), reverse=not ascending))
# def find_keys_by_partial_value(dict_to_search, partial_value): 
#     return [key for key, value in dict_to_search.items() if partial_value in str(value)]
# original_dict = {'banana': 3, 'apple': 1, 'cherry': 2, 'date': 4}
# sorted_dict_asc = sort_dict_by_keys(original_dict, ascending=True)
# print("Сортований словник за зростанням ключів:", sorted_dict_asc)
# sorted_dict_desc = sort_dict_by_keys(original_dict, ascending=False)
# print("Сортований словник за спаданням ключів:", sorted_dict_desc)
# partial_value = '2'
# keys_with_partial_value = find_keys_by_partial_value(original_dict, partial_value)
# print(f"Ключі, значення яких містять '{partial_value}':", keys_with_partial_value)



# def find_keys_by_partial_value(dict_to_search, partial_value):
#     return [key for key, value in dict_to_search.items() if partial_value in str(value)]
# def convert_tuples_to_dict(tuples_list):
#     return dict(tuples_list)
# original_dict = {'banana': 'yellow fruit', 'apple': 'green fruit', 'cherry': 'red fruit', 'date': 'sweet fruit'}
# partial_value = 'fruit'
# keys_with_partial_value = find_keys_by_partial_value(original_dict, partial_value)
# print(f"Ключі, значення яких містять '{partial_value}':", keys_with_partial_value)
# tuples_list = [('banana', 'yellow'), ('apple', 'green'), ('cherry', 'red'), ('date', 'brown')]
# converted_dict = convert_tuples_to_dict(tuples_list)



# def convert_tuples_to_dict(tuples_list):
#     return dict(tuples_list)
# def group_elements_by_value(tuples_list):
#     grouped_dict = {}
#     for key, value in tuples_list:
#         if value in grouped_dict:
#             grouped_dict[value].append(key)
#         else:
#             grouped_dict[value] = [key]
#     return grouped_dict
# tuples_list = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'a'), (5, 'b'), (6, 'c')]
# converted_dict = convert_tuples_to_dict(tuples_list)
# print("Словник, створений з кортежів:", converted_dict)
# grouped_elements = group_elements_by_value(tuples_list)
# print("Групування елементів за значеннями:", grouped_elements)


# def group_elements_by_first(tuples_list):
#     grouped_dict = {}
#     for key, value in tuples_list:
#         if key in grouped_dict:
#             grouped_dict[key].append(value)
#         else:
#             grouped_dict[key] = [value]
#     return grouped_dict
# def merge_dicts_with_lists(dict1, dict2):
#     merged_dict = dict1.copy()
#     for key, value_list in dict2.items():
#         if key in merged_dict:
#             merged_dict[key].extend(value_list)
#         else:
#             merged_dict[key] = value_list
#     return merged_dict
# tuples_list1 = [(1, 'a'), (2, 'b'), (1, 'c')]
# tuples_list2 = [(2, 'd'), (3, 'e'), (1, 'f')]
# grouped_dict1 = group_elements_by_first(tuples_list1)
# grouped_dict2 = group_elements_by_first(tuples_list2)
# print("Перший згрупований словник:", grouped_dict1)
# print("Другий згрупований словник:", grouped_dict2)
# merged_dict = merge_dicts_with_lists(grouped_dict1, grouped_dict2)
# print("Об'єднаний словник:", merged_dict)



# def merge_dicts_with_lists(dict1, dict2):
#     merged_dict = dict1.copy()
#     for key, value_list in dict2.items():
#         if key in merged_dict:
#             merged_dict[key].extend(value_list)
#         else:
#             merged_dict[key] = value_list
#     return merged_dict
# def find_min_max_in_dict(dict_with_lists):
#     all_values = [item for sublist in dict_with_lists.values() for item in sublist]
#     min_value = min(all_values)
#     max_value = max(all_values)
#     return min_value, max_value
# dict1 = {'a': [1, 2], 'b': [3, 4]}
# dict2 = {'a': [5], 'b': [6, 7]}
# merged_dict = merge_dicts_with_lists(dict1, dict2)
# print("Об'єднаний словник:", merged_dict)
# min_value, max_value = find_min_max_in_dict(merged_dict)
# print("Мінімальне значення у словнику:", min_value)
# print("Максимальне значення у словнику:", max_value)



# def find_extremes_and_sum(dictionary):
#     if not isinstance(dictionary, dict):
#         raise TypeError("Input should be a dictionary.")
#     if not dictionary:
#         raise ValueError("Dictionary should not be empty.")
#     min_key = None
#     max_key = None
#     min_value = float('inf')  
#     max_value = float('-inf')  
#     total_sum = 0
#     for key, value in dictionary.items():
#         if value < min_value:
#             min_value = value
#             min_key = key
#         if value > max_value:
#             max_value = value
#             max_key = key
#         if isinstance(value, dict):
#             total_sum += find_extremes_and_sum(value)
#         else:
#             total_sum += value
#     return (min_key, max_key, total_sum)
# input_dict = {'a': 10,'b': {'x': 5,'y': 20 },'c': 3, 'd': { 'p': 8, 'q': 2}}
# try:
#     min_key, max_key, sum_values = find_extremes_and_sum(input_dict)
#     print(f"Ключ з мінімальним значенням: {min_key}")
#     print(f"Ключ з максимальним значенням: {max_key}")
#     print(f"Сума всіх значень: {sum_values}")
# except Exception as e:
#     print(f"Сталася помилка: {e}")



# def calculate_sum(dictionary):
#     total_sum = 0
#     for value in dictionary.values():
#         if isinstance(value, dict):
#             total_sum += calculate_sum(value)
#         elif isinstance(value, (int, float)):
#             total_sum += value
#     return total_sum
# input_dict = {'a': { 'x': 1,   'y': 2 }, 'b': {'x': 3,'y': 4 }}
# total_sum = calculate_sum(input_dict)
# print(f"Сума всіх числових значень у словнику: {total_sum}")
