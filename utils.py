import re
from datetime import datetime

def is_date_valid(date: str) -> bool:
    is_date_correct = None
    try:
        date = datetime.strptime(date, "%Y-%m-%d")
        is_date_correct = True
    except ValueError:
        is_date_correct = False
        
    return is_date_correct

def is_isbn_valid(isbn: str) -> bool:
    isbn = isbn.upper()
    
    if len(isbn) == 10:
        match = re.search(r'^(\d{9})(\d|X)$', isbn)
        
        if not match:
            return False
        
        digits = match.group(1)
        check_digit = 10 if match.group(2) == "X" else int(match.group(2))
        
        res = sum(int(digit) * (index + 1) for (index, digit) in enumerate(digits))
        return (res % 11) == check_digit

    if isbn[:3] not in ["978", "979"]:
        return False                
    
    digits = isbn[:-1]            
    check_digit = int(isbn[-1])
    
    res = sum(int(digit) * (1 if index % 2 == 0 else 3) for (index, digit) in enumerate(digits))
    
    return (res + check_digit) % 10 == 0