def raita_search(text, pattern):
    if not pattern or not text or len(pattern) > len(text):
        return -1
    n = len(text)
    m = len(pattern)
    skip = {pattern[i]: m - i - 1 for i in range(m-1)}
    skip[pattern[-1]] = m
    mid = m // 2
    i = 0
    while i <= n - m:
        # Kiểm tra ký tự ở giữa, đầu và cuối mẫu
        if (text[i + mid] == pattern[mid] and text[i] == pattern[0] and text[i + m - 1] == pattern[-1]):
            # Nếu các ký tự chiến lược khớp, kiểm tra toàn bộ mẫu
            if text[i:i + m] == pattern:
                return i
        i += skip.get(text[i + m - 1], m)  # Nhảy qua dựa trên bảng skip
    return -1

# Ví dụ sử dụng:
text = "HERE IS A SIMPLE EXAMPLE"
pattern = "EXAMPLE"
result = raita_search(text, pattern)

if result != -1:
    print(f"Pattern found at index: {result}")
else:
    print("Pattern not found")
