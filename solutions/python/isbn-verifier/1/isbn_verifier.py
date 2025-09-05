def is_valid(isbn):
    
# (d₁ * 10 + d₂ * 9 + d₃ * 8 + d₄ * 7 + d₅ * 6 + d₆ * 5 + d₇ * 4 + d₈ * 3 + d₉ * 2 + d₁₀ * 1) mod 11 == 0
    
    isbn_list = []        
    isbn = isbn.replace("-", "")
    
    # Case 1: empty string
    if not isbn:
        return False

    # Case 2: wrong length
    elif len(isbn) != 10:
        return False
    
    for d in isbn:
        if d == 'X' and len(isbn_list) == 9:  # X only allowed in last place
            isbn_list.append(10)
        elif d.isdigit():
            isbn_list.append(int(d))
        else:
            return False
            break
    else:
        total_list = [10,9,8,7,6,5,4,3,2,1]
        
        sum = 0
        for i, j in zip(isbn_list, total_list):
            sum += i*j
        sum
        
        if sum%11 == 0:
            return True
        else:
            return False