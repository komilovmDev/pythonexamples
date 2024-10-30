def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2  # O'rta indeksni topamiz
        if arr[mid] == target:
            return mid  # Agar topilsa, indeksni qaytaramiz
        elif arr[mid] < target:
            left = mid + 1  # Chap chegarani o'rtadan keyingi elementga siljitamiz
        else:
            right = mid - 1  # O'ng chegarani o'rtadan oldingi elementga siljitamiz
    
    return -1  # Agar qiymat topilmasa, -1 qaytaradi

# Misol
arr = [1, 3, 5, 7, 9, 11]
target = 7

result = binary_search(arr, target)
if result != -1:
    print(f"Element {target} indeksda topildi: {result}")
else:
    print("Element topilmadi")
