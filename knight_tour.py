import numpy as np

# Các nước có thể đi tương ứng
X = [-2,-2,-1,-1, 1, 1, 2, 2]
Y = [-1, 1,-2, 2,-2, 2,-1, 1]

# Khởi tạo bàn cờ vua n x n:
def init(n):
    return np.zeros((n,n), dtype = int)

# Hàm di chuyển vị trí phù hợp
# input:  Ma trận A(bàn cờ), n: số chiều của ma trận A,
# x, y : Tọa độ của điểm
# count: Số bước đi
count = 0

def move(A,n,x,y,count):
    # Khởi tạo số bước đi
    count += 1
    A[x][y] = count
    for i in range(8):
        # Kiểm tra đã đi hết bàn cờ chưa
        if (count == n**2):
            print("Cách đi là: ")
            print(A)
            quit()
        # Tạo bước mới khi chưa đi hết bàn cờ:
        a = x + X[i]
        b = y + Y[i]
        # Kiểm tra có vị trí chuẩn bị đi có hợp lệ không
        if (a >= 0 and a < n and b >= 0 and b < n and A[a][b] == 0):
            move(A,n,a,b,count)
    # Nếu không tìm được bước đi thì trả lại:
    count -= 1
    A[x][y] = 0

def main():
    n = int(input("Nhập kích thước bàn cờ vua: "))
    A = init(n)
    print("Nhập vị trí ban đầu")
    x = int(input("Nhập x = "))
    y = int(input("Nhập y = "))
    move(A,n,x,y,count)
    print("Không tìm thấy đường đi")

if __name__ == "__main__":
    main()