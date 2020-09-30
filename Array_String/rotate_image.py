import random

def rotate(inp_img, orientation=90):
    i = 0
    j = 0
    N = len(inp_img) - 1

    while i < N/2:
        while j <= N-i-1:
            inp_img[i][j], inp_img[j][N-i] = inp_img[j][N-i], inp_img[i][j]
            inp_img[i][j], inp_img[N-i][N-j] = inp_img[N-i][N-j], inp_img[i][j]
            inp_img[i][j], inp_img[N-j][i] = inp_img[N-j][i], inp_img[i][j]
            j += 1
        
        i += 1
        j = i

    return inp_img

def print_img(img):
    img_xy = len(img)
    for i in range(img_xy):
        for j in range(img_xy):
            print(f"{inp_img[i][j]:5}", end='')
        print()


if __name__ == "__main__":
    img_xy = 4
    inp_img = [[random.randrange(0,256) for i in range(img_xy)] for j in range(img_xy)]
    print(f"Input image")
    print_img(inp_img)

    out_img = rotate(inp_img)
    print(f"Output image")

    print_img(out_img)