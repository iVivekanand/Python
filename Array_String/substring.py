import math

def check_rotated(str1, str2):
    len1 = len(str1)
    len2 = len(str2)

    if len1 != len2:
        return False

    rotation_count = 0
    rotation_index = 0

    if True:
        i = len1//2-1
        for j in range(len1-1,-1,-1):
            if rotation_count == len1//2:
                rotation_index = j + 1
                break
            if str2[j] == str1[i]:
                i -= 1
                rotation_count += 1
            else:
                i += rotation_count
                j += 1
    else:
        i = len1//2
        for j in range(0, len1, 1):
            if rotation_count == math.ceil(len1/2):
                rotation_index = j
                break
            if str2[j] == str1[i]:
                i += 1
                rotation_count += 1
            else:
                i -= rotation_count
                j -= 1
            
    for i in range(len1):
        print(f"str1[{i}]({str1[i]})==str2[{(i+rotation_index)%len1}]({str2[(i+rotation_index)%len1]})")
        if str1[i] != str2[(i+rotation_index)%len1]:
            return False

    return True

if __name__ == "__main__":
    print(check_rotated("babaa", "ababa"))