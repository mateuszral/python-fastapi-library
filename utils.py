from datetime import datetime

def is_date_valid(date: str) -> bool:
    is_date_correct = None
    try:
        date = datetime.strptime(date, "%Y-%m-%d")
        is_date_correct = True
    except ValueError:
        is_date_correct = False
        
    return is_date_correct

def is_isbn_valid(isbn: int) -> bool:
    sum = 0
    for index, digit in enumerate(str(isbn)[:-1]):
        if index % 2 == 0:
            sum += int(digit)
        else:
            sum += int(digit) * 3
            
    return (sum + (isbn % 10)) % 10 == 0