def solution(phone_book):
    pb = sorted(phone_book)
    for i in range(len(pb)-1):
        if pb[i+1].startswith(pb[i]) : return False
    return True
