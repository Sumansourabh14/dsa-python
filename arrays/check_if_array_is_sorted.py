def check_if_array_is_sorted(a):
    for i in range(1, len(a)):
        if (a[i] >= a[i-1]):
            pass
        else:
            return False
    return True 

print(check_if_array_is_sorted([1,2,2,3,3,4]))       
print(check_if_array_is_sorted([1,2,1,3,4]))       