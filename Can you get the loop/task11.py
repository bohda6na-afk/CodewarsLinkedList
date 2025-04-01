def loop_size(start):
    a = start
    b = start
    
    while b and b.next:
        a = a.next
        b = b.next.next
        if a == b:
            count = 1
            b = b.next
            while b != a:
                b = b.next
                count += 1
            return count
    return 0
