def file_name_check(file_name):
    """
    Returns 'Yes' if the file name is valid, 'No' otherwise.
    """
    # Step 1: Check for exactly one dot
    if file_name.count('.') != 1:
        return 'No'
    
    # Step 2: Split at the dot
    name, ext = file_name.split('.')
    
    # Step 3: Validate extension
    if ext not in ['txt', 'exe', 'dll']:
        return 'No'
    
    # Step 4: Check that the part before the dot is not empty and starts with a letter
    if not name or not name[0].isalpha():
        return 'No'
    
    # Step 5: Count digits in the whole file name
    digit_count = sum(c.isdigit() for c in file_name)
    if digit_count > 3:
        return 'No'
    
    return 'Yes'

print(file_name_check("example.txt"))    # 'Yes'
print(file_name_check("1example.dll"))   # 'No'
print(file_name_check("examp1le2.txt"))  # 'Yes'
print(file_name_check("examp1234.txt"))  # 'No'
print(file_name_check("ex.txt"))         # 'Yes'
print(file_name_check(".txt"))           # 'No'
print(file_name_check("example.tx"))     # 'No'
print(file_name_check("example.txt.txt"))# 'No'

