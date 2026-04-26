def is_palindrome(s: str) -> bool:
    # Step 1: Normalize the string (lowercase, remove non-alphanumeric)
    cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
    
    # Step 2: Check palindrome using two-pointer technique
    left, right = 0, len(cleaned) - 1
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True

# Example test cases
print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("race a car"))                      # False
print(is_palindrome("No lemon, no melon"))              # True