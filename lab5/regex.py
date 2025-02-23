import re
#task1
def match_a_b(text):
    return re.fullmatch(r'ab*',text) is not None
print(match_a_b("ac")) 

#task2
def match_a_3b(text):
    return re.fullmatch(r'ab{2,3}', text) is not None
print(match_a_3b("abb"))

#task3
def find_snake_case(text):
    return re.findall(r'\b[a-z]+_[a-z]+\b', text)
print(find_snake_case("hello_world test_case")) 

#task4
def upper_lower(text):
    return re.findall(r'[A-Z][a-z]+', text)
print(upper_lower("HelloWorld Example anotherWords hi"))  

#task5
def match_a_anything_b(text):
    return re.fullmatch(r'a.*b', text) is not None
print(match_a_anything_b("acvb"))

#task6
def replace(text):
    return re.sub(r'[ ,.]', ':', text)
print(replace("My name is John. This is a test."))

#task7
def snake_to_camel(text):
    return re.sub(r'_([a-z])', lambda x: x.group(1).upper(), text)
print(snake_to_camel("hello_world"))

#task8
def split_upper(text):
    return re.findall(r'[A-Z][a-z]*', text)
print(split_upper("SplitAtUpperCase")) 

#task9
def insert_spaces(text):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', text)
print(insert_spaces("InsertSpacesBetweenWords")) 

#task10
def camel_to_snake(text):
    return re.sub(r'([a-z])([A-Z])', r'\1_\2', text).lower()
print(camel_to_snake("CamelCaseExample")) 
 
