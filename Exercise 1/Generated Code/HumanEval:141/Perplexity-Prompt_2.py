def file_name_check(file_name):
    """
    Returns 'Yes' if the file name is valid, 'No' otherwise.
    """
    # Step 1: Check the file name contains exactly one dot
    if file_name.count('.') != 1:
        return 'No'
    
    # Step 2: Split into name and extension
    name, ext = file_name.split('.')
    
    # Check extension is valid
    if ext not in ['txt', 'exe', 'dll']:
        return 'No'
    
    # Check name before the dot is not empty and starts with a letter
    if not name or not name[0].isalpha():
        return 'No'
    
    # Step 3: Count digits in the file name
    digit_count = sum(1 for c in file_name if c.isdigit())
    if digit_count > 3:
        return 'No'
    
    # Step 4: If all criteria pass, return 'Yes'
    return 'Yes'

print(file_name_check("example.txt"))    # 'Yes'
print(file_name_check("1example.dll"))   # 'No'
print(file_name_check("examp1le2.txt"))  # 'Yes'
print(file_name_check("examp1234.txt"))  # 'No'
print(file_name_check("ex.txt"))         # 'Yes'
print(file_name_check(".txt"))           # 'No'
print(file_name_check("example.tx"))     # 'No'
print(file_name_check("example.txt.txt"))# 'No'
