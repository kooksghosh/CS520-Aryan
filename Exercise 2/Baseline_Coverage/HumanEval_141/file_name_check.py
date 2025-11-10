def file_name_check(file_name: str) -> str:
    """
    Return 'Yes' if the file name is valid, else 'No'.
    Rules:
      - At most three digits total in the name.
      - Exactly one dot '.'.
      - Before the dot: non-empty and starts with a latin letter.
      - After the dot: one of {'txt','exe','dll'}.
    """
    # Exactly one dot
    if file_name.count(".") != 1:
        return "No"

    before, after = file_name.split(".")

    # Before-dot checks
    if not before or not before[0].isalpha():
        return "No"

    # Extension check
    if after not in {"txt", "exe", "dll"}:
        return "No"

    # Digit count across the whole name
    if sum(ch.isdigit() for ch in file_name) > 3:
        return "No"

    return "Yes"

