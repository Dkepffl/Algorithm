'''def solution(phone_book):
    pb = sorted(phone_book)
    for i in range(len(pb)-1):
        if pb[i+1].startswith(pb[i]) : return False
    return True
'''
def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True