print("?")
n = int(input())
def giaiThua(n):
    if(n < 0):
        print("bạn đã nhập sai, xin hãy kiểm tra lại")
    else:
        if n == 0:
            return 1
        return n * giaiThua(n - 1)
print("đáp số là:",giaiThua(n))