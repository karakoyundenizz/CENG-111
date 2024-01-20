Vertices_Quadrilateral = eval(input())
x0 = float(Vertices_Quadrilateral[0][0])
y0 = abs(float(Vertices_Quadrilateral[0][1]))
x1 = float(Vertices_Quadrilateral[1][0])
y1 = abs(float(Vertices_Quadrilateral[1][1]))
x2 = float(Vertices_Quadrilateral[2][0])
y2 = abs(float(Vertices_Quadrilateral[2][1]))
x3 = float(Vertices_Quadrilateral[3][0])
y3 = abs(float(Vertices_Quadrilateral[3][1]))
max_x_mesafe = (abs(x0 - x1), abs(x1 - x2), abs(x3 - x2), abs(x0 - x3), abs(x0 - x2), abs(x1 - x3))
First_area = float((abs((x0 * y1 - x1 * y0) + (x1 * y2 - x2 * y1) + (x2 * y3 - x3 * y2) + (x3 * y0 - x0 * y3))) / 2)

# y lerin pozitif olduğu durum
if y0 >= 0 and y1 >= 0 and y2 >= 0 and y3 >= 0:
    # xler arası mesafenin en uzak olduğu durum ardışık x arasında ise

    if max(max_x_mesafe) == abs(x0 - x1):
        if y3 - y0 > (x3 - x0) * ((y1 - y0) / (x1 - x0)) and y2 - y0 > (x2 - x0) * (
                (y1 - y0) / (x1 - x0)) and x1 != x3 and x2 != x0 and x1 != x2:
            print("%.2f" % (((y0 + y1) / 2) * abs(x1 - x0)))
        elif y3 - y0 < (x3 - x0) * ((y1 - y0) / (x1 - x0)) and y2 - y0 < (x2 - x0) * (
                (y1 - y0) / (x1 - x0)) and x1 != x3 and x2 != x0 and x1 != x2:
            print("%.2f" % ((((y0 + y1) / 2) * abs(x0 - x1)) - First_area))
        elif y3 - y0 < (x3 - x0) * ((y1 - y0) / (x1 - x0)) and y2 - y0 < (x2 - x0) * (
                (y1 - y0) / (x1 - x0)) and x1 == x3 and x2 != x0:
            print("%.2f" % ((abs((y3 + y0)) / 2) * abs(x0 - x3)))
        elif y3 - y0 > (x3 - x0) * ((y1 - y0) / (x1 - x0)) and y2 - y0 > (x2 - x0) * (
                (y1 - y0) / (x1 - x0)) and x1 == x3 and x2 != x0:
            print("%.2f" % ((abs((y1 + y0)) / 2) * abs(x0 - x1)))
        elif y3 - y0 < (x3 - x0) * ((y1 - y0) / (x1 - x0)) and y2 - y0 < (x2 - x0) * (
                (y1 - y0) / (x1 - x0)) and x2 == x0 and x1 != x3:
            print("%.2f" % ((abs((y1 + y2)) / 2) * abs(x2 - x1)))
        elif y3 - y0 > (x3 - x0) * ((y1 - y0) / (x1 - x0)) and y2 - y0 > (x2 - x0) * (
                (y1 - y0) / (x1 - x0)) and x2 == x0 and x1 != x3:
            print("%.2f" % ((abs((y1 + y0)) / 2) * abs(x0 - x1)))
        elif y3 - y0 < (x3 - x0) * ((y1 - y0) / (x1 - x0)) and y2 - y0 < (x2 - x0) * (
                (y1 - y0) / (x1 - x0)) and x1 != x3 and x2 != x0 and x1 == x2:
            print("%.2f" % ((((y0 + y1) / 2) * abs(x0 - x1)) - First_area))
        elif y3 - y0 > (x3 - x0) * ((y1 - y0) / (x1 - x0)) and y2 - y0 > (x2 - x0) * (
                (y1 - y0) / (x1 - x0)) and x1 != x3 and x2 != x0 and x1 == x2:
            print("%.2f" % (((y0 + y1) / 2) * abs(x1 - x0)))



    elif max(max_x_mesafe) == abs(x2 - x1) and x0 != x1 and x1 != x3 and x0 != x2 and x3 != x2:
        if y0 - y1 > (x0 - x1) * ((y1 - y2) / (x1 - x2)) and y3 - y1 > (x3 - x1) * ((y1 - y2) / (x1 - x2)):
            print("%.2f" % (((y1 + y2) / 2) * abs(x1 - x2)))
        else:
            print("%.2f" % ((((y2 + y1) / 2) * abs(x2 - x1)) - First_area))

    if max(max_x_mesafe) == abs(x3 - x2):
        if y1 - y3 > (x1 - x3) * ((y3 - y2) / (x3 - x2)) and y0 - y3 > (x0 - x3) * (
                (y3 - y2) / (x3 - x2)) and x0 != x2 and x1 != x2:
            print("%.2f" % (((y3 + y2) / 2) * abs(x2 - x3)))
        elif y1 - y3 < (x1 - x3) * ((y3 - y2) / (x3 - x2)) and y0 - y3 < (x0 - x3) * (
                (y3 - y2) / (x3 - x2)) and x0 != x2 and x1 != x3 and x1 != x2:
            print("%.2f" % ((((y3 + y2) / 2) * abs(x2 - x3)) - First_area))
        elif y1 - y3 > (x1 - x3) * ((y3 - y2) / (x3 - x2)) and y0 - y3 > (x0 - x3) * (
                (y3 - y2) / (x3 - x2)) and x0 == x2:
            print("%.2f" % ((((y3 + y2) / 2) * abs(x2 - x3))))
        elif y1 - y3 < (x1 - x3) * ((y3 - y2) / (x3 - x2)) and y0 - y3 < (x0 - x3) * (
                (y3 - y2) / (x3 - x2)) and x0 == x2:
            print("%.2f" % ((((y3 + y0) / 2) * abs(x0 - x3))))
        elif y1 - y3 < (x1 - x3) * ((y3 - y2) / (x3 - x2)) and y0 - y3 < (x0 - x3) * (
                (y3 - y2) / (x3 - x2)) and x0 != x2 and x1 == x3:
            print("%.2f" % ((((y1 + y2) / 2) * abs(x2 - x1))))
        elif y1 - y3 > (x1 - x3) * ((y3 - y2) / (x3 - x2)) and y0 - y3 > (x0 - x3) * (
                (y3 - y2) / (x3 - x2)) and x0 != x2 and x1 == x2 and x0 != x3:
            print("%.2f" % (((y3 + y2) / 2) * abs(x2 - x3)))
        elif y1 - y3 < (x1 - x3) * ((y3 - y2) / (x3 - x2)) and y0 - y3 < (x0 - x3) * (
                (y3 - y2) / (x3 - x2)) and x0 != x2 and x1 == x2 and x0 != x3:
            print("%.2f" % ((((y3 + y2) / 2) * abs(x2 - x3)) - First_area))

    if max(max_x_mesafe) == abs(x0 - x3) and x0 != x1 and x0 != x2 and x3 != x1:
        if y1 - y3 > (x1 - x3) * ((y3 - y0) / (x3 - x0)) and y2 - y3 > (x2 - x3) * ((y3 - y0) / (x3 - x0)):
            print("%.2f" % (((y3 + y0) / 2) * abs(x0 - x3)))
        else:
            print("%.2f" % ((((y3 + y0) / 2) * abs(x0 - x3)) - First_area))

    # x lerin ardışık olmadığı durumlar

    if max(max_x_mesafe) == abs(x0 - x2) and x2 != x3 and x1 != x2 and x0 != x3:
        if y1 > y3:
            if y0 > y1 and y3 - y2 > (x3 - x2) * ((y2 - y0) / (x2 - x0)):
                print("%.2f" % (((((y2 + y0) / 2)) * abs(x2 - x0)) + (
                            1 / 2 * abs((((x2 * y0) + (x0 * y3) + (x3 * y2)) - ((y2 * x0) + (y0 * x3) + (y3 * x2)))))))
            elif y0 > y1 and y3 - y2 < (x3 - x2) * ((y2 - y0) / (x2 - x0)):
                print("%.2f" % (((((y2 + y0) / 2)) * abs(x2 - x0)) - (
                            1 / 2 * abs((((x2 * y0) + (x0 * y3) + (x3 * y2)) - ((y2 * x0) + (y0 * x3) + (y3 * x2)))))))
            elif y1 > y0:
                if y3 > y0 and y3 - y2 < (x3 - x2) * ((y2 - y0) / (x2 - x0)):
                    print("%.2f" % (((((y2 + y0) / 2)) * abs(x2 - x0)) - (1 / 2 * abs(
                        (((x2 * y0) + (x0 * y3) + (x3 * y2)) - ((y2 * x0) + (y0 * x3) + (y3 * x2)))))))
                elif y3 > y0 and y3 - y2 > (x3 - x2) * ((y2 - y0) / (x2 - x0)):
                    print("%.2f" % (((((y2 + y0) / 2)) * abs(x2 - x0)) + (1 / 2 * abs(
                        (((x2 * y0) + (x0 * y3) + (x3 * y2)) - ((y2 * x0) + (y0 * x3) + (y3 * x2)))))))
                elif y0 > y3 and y3 - y2 > (x3 - x2) * ((y2 - y0) / (x2 - x0)):
                    print("%.2f" % (((((y2 + y0) / 2)) * abs(x2 - x0)) + (1 / 2 * abs(
                        (((x2 * y0) + (x0 * y3) + (x3 * y2)) - ((y2 * x0) + (y0 * x3) + (y3 * x2)))))))
                elif y0 > y3 and y3 - y2 < (x3 - x2) * ((y2 - y0) / (x2 - x0)):
                    print("%.2f" % (((((y2 + y0) / 2)) * abs(x2 - x0)) - (1 / 2 * abs(
                        (((x2 * y0) + (x0 * y3) + (x3 * y2)) - ((y2 * x0) + (y0 * x3) + (y3 * x2)))))))
                elif y0 == y3 and y3 - y2 > (x3 - x2) * ((y2 - y0) / (x2 - x0)):
                    print("%.2f" % (((((y2 + y0) / 2)) * abs(x2 - x0)) + (1 / 2 * abs(
                        (((x2 * y0) + (x0 * y3) + (x3 * y2)) - ((y2 * x0) + (y0 * x3) + (y3 * x2)))))))
                elif y0 == y3 and y3 - y2 < (x3 - x2) * ((y2 - y0) / (x2 - x0)):
                    print("%.2f" % (((((y2 + y0) / 2)) * abs(x2 - x0)) - (1 / 2 * abs(
                        (((x2 * y0) + (x0 * y3) + (x3 * y2)) - ((y2 * x0) + (y0 * x3) + (y3 * x2)))))))
            elif y0 == y1 and y3 - y2 < (x3 - x2) * ((y2 - y0) / (x2 - x0)):
                print("%.2f" % (((((y2 + y0) / 2)) * abs(x2 - x0)) - (
                            1 / 2 * abs((((x2 * y0) + (x0 * y3) + (x3 * y2)) - ((y2 * x0) + (y0 * x3) + (y3 * x2)))))))
            elif y0 == y1 and y3 - y2 > (x3 - x2) * ((y2 - y0) / (x2 - x0)):
                print("%.2f" % (((((y2 + y0) / 2)) * abs(x2 - x0)) + (
                            1 / 2 * abs((((x2 * y0) + (x0 * y3) + (x3 * y2)) - ((y2 * x0) + (y0 * x3) + (y3 * x2)))))))



        elif y3 > y1:
            if y0 > y3 and y1 - y2 < (x1 - x2) * ((y2 - y0) / (x2 - x0)):
                print("%.2f" % (((((y2 + y0) / 2)) * abs(x2 - x0)) - (
                            1 / 2 * abs((((x0 * y1) + (x1 * y2) + (x2 * y0)) - ((y0 * x1) + (y1 * x2) + (y2 * x0)))))))
            elif y0 > y3 and y1 - y2 > (x1 - x2) * ((y2 - y0) / (x2 - x0)):
                print("%.2f" % (((((y2 + y0) / 2)) * abs(x2 - x0)) + (
                            1 / 2 * abs((((x0 * y1) + (x1 * y2) + (x2 * y0)) - ((y0 * x1) + (y1 * x2) + (y2 * x0)))))))
            elif y3 > y0:
                if y1 > y0 and y1 - y2 > (x1 - x2) * ((y2 - y0) / (x2 - x0)):
                    print("%.2f" % (((((y2 + y0) / 2)) * abs(x2 - x0)) + (1 / 2 * abs(
                        (((x0 * y1) + (x1 * y2) + (x2 * y0)) - ((y0 * x1) + (y1 * x2) + (y2 * x0)))))))
                elif y1 > y0 and y1 - y2 < (x1 - x2) * ((y2 - y0) / (x2 - x0)):
                    print("%.2f" % (((((y2 + y0) / 2)) * abs(x2 - x0)) - (1 / 2 * abs(
                        (((x0 * y1) + (x1 * y2) + (x2 * y0)) - ((y0 * x1) + (y1 * x2) + (y2 * x0)))))))
                elif y0 > y1 and y1 - y2 > (x1 - x2) * ((y2 - y0) / (x2 - x0)):
                    print("%.2f" % (((((y2 + y0) / 2)) * abs(x2 - x0)) + (1 / 2 * abs(
                        (((x0 * y1) + (x1 * y2) + (x2 * y0)) - ((y0 * x1) + (y1 * x2) + (y2 * x0)))))))
                elif y0 > y1 and y1 - y2 < (x1 - x2) * ((y2 - y0) / (x2 - x0)):
                    print("%.2f" % (((((y2 + y0) / 2)) * abs(x2 - x0)) - (1 / 2 * abs(
                        (((x0 * y1) + (x1 * y2) + (x2 * y0)) - ((y0 * x1) + (y1 * x2) + (y2 * x0)))))))
                elif y0 == y1 and y1 - y2 > (x1 - x2) * ((y2 - y0) / (x2 - x0)):
                    print("%.2f" % (((((y2 + y0) / 2)) * abs(x2 - x0)) + (1 / 2 * abs(
                        (((x0 * y1) + (x1 * y2) + (x2 * y0)) - ((y0 * x1) + (y1 * x2) + (y2 * x0)))))))
                elif y0 == y1 and y1 - y2 < (x1 - x2) * ((y2 - y0) / (x2 - x0)):
                    print("%.2f" % (((((y2 + y0) / 2)) * abs(x2 - x0)) - (1 / 2 * abs(
                        (((x0 * y1) + (x1 * y2) + (x2 * y0)) - ((y0 * x1) + (y1 * x2) + (y2 * x0)))))))
            elif y0 == y3 and y1 - y2 > (x1 - x2) * ((y2 - y0) / (x2 - x0)):
                print("%.2f" % (((((y2 + y0) / 2)) * abs(x2 - x0)) + (
                            1 / 2 * abs((((x0 * y1) + (x1 * y2) + (x2 * y0)) - ((y0 * x1) + (y1 * x2) + (y2 * x0)))))))
            elif y0 == y3 and y1 - y2 < (x1 - x2) * ((y2 - y0) / (x2 - x0)):
                print("%.2f" % (((((y2 + y0) / 2)) * abs(x2 - x0)) - (
                            1 / 2 * abs((((x0 * y1) + (x1 * y2) + (x2 * y0)) - ((y0 * x1) + (y1 * x2) + (y2 * x0)))))))



        elif y3 == y1:
            b = abs(((y0 - y2) / (x0 - x3)) * x1 - y1 - (((y0 - y2) / (x0 - x2)) * x2) + y2) / (
                        ((((y0 - y2) / (x0 - x2)) ** 2) + 1) ** (1 / 2))
            a = abs(((y0 - y2) / (x0 - x2)) * x3 - y3 - (((y0 - y2) / (x0 - x2)) * x2) + y2) / (
                        ((((y0 - y2) / (x0 - x2)) ** 2) + 1) ** (1 / 2))
            if y2 > y1:
                if y2 > y1 and y1 - y2 < (x1 - x2) * ((y2 - y0) / (x2 - x0)) and y3 - y2 < (x3 - x2) * (
                        (y2 - y0) / (x2 - x0)) and a > b:
                    print("%.2f" % (((((y2 + y0) / 2)) * abs(x2 - x0)) - (1 / 2 * abs(
                        (((x2 * y0) + (x0 * y3) + (x3 * y2)) - ((y2 * x0) + (y0 * x3) + (y3 * x2)))))))

                elif y2 > y1 and y1 - y2 < (x1 - x2) * ((y2 - y0) / (x2 - x0)) and y3 - y2 > (x3 - x2) * (
                        (y2 - y0) / (x2 - x0)):
                    print("%.2f" % (((((y2 + y0) / 2)) * abs(x2 - x0)) - (1 / 2 * abs(
                        (((x2 * y1) + (x1 * y0) + (x0 * y2)) - ((y2 * x1) + (y1 * x0) + (y0 * x2)))))))

                elif y2 > y1 and y1 - y2 > (x1 - x2) * ((y2 - y0) / (x2 - x0)) and y3 - y2 < (x3 - x2) * (
                        (y2 - y0) / (x2 - x0)):
                    print("%.2f" % (((((y2 + y0) / 2)) * abs(x2 - x0)) - (1 / 2 * abs(
                        (((x0 * y2) + (x2 * y3) + (x3 * y0)) - ((y0 * x2) + (y2 * x3) + (y3 * x0)))))))

                elif y2 > y1 and y1 - y2 < (x1 - x2) * ((y2 - y0) / (x2 - x0)) and y3 - y2 < (x3 - x2) * (
                        (y2 - y0) / (x2 - x0)) and b > a:
                    print("%.2f" % (((((y2 + y0) / 2)) * abs(x2 - x0)) - (1 / 2 * abs(
                        (((x0 * y1) + (x1 * y2) + (x2 * y0)) - ((y0 * x1) + (y1 * x2) + (y2 * x0)))))))

                elif y2 > y1 and y1 - y2 > (x1 - x2) * ((y2 - y0) / (x2 - x0)) and y3 - y2 > (x3 - x2) * (
                        (y2 - y0) / (x2 - x0)) and a > b:
                    print("%.2f" % (((((y2 + y0) / 2)) * abs(x2 - x0)) + (1 / 2 * abs(
                        (((x0 * y1) + (x1 * y2) + (x2 * y0)) - ((y0 * x1) + (y1 * x2) + (y2 * x0)))))))

                elif y2 > y1 and y1 - y2 > (x1 - x2) * ((y2 - y0) / (x2 - x0)) and y3 - y2 > (x3 - x2) * (
                        (y2 - y0) / (x2 - x0)) and b > a:
                    print("%.2f" % (((((y2 + y0) / 2)) * abs(x2 - x0)) + (1 / 2 * abs(
                        (((x0 * y2) + (x2 * y3) + (x3 * y0)) - ((y0 * x2) + (y2 * x3) + (y3 * x0)))))))
            elif y1 > y2:
                if y1 > y2 and y1 - y2 < (x1 - x2) * ((y2 - y0) / (x2 - x0)) and y3 - y2 < (x3 - x2) * (
                        (y2 - y0) / (x2 - x0)) and a > b:
                    print("%.2f" % (((((y2 + y0) / 2)) * abs(x2 - x0)) - (1 / 2 * abs(
                        (((x0 * y2) + (x2 * y3) + (x3 * y0)) - ((y0 * x2) + (y2 * x3) + (y3 * x0)))))))

                elif y1 > y2 and y1 - y2 < (x1 - x2) * ((y2 - y0) / (x2 - x0)) and y3 - y2 > (x3 - x2) * (
                        (y2 - y0) / (x2 - x0)):
                    print("%.2f" % (((((y2 + y0) / 2)) * abs(x2 - x0)) - (1 / 2 * abs(
                        (((x0 * y1) + (x1 * y2) + (x2 * y0)) - ((y0 * x1) + (y1 * x2) + (y2 * x0)))))))

                elif y1 > y2 and y1 - y2 > (x1 - x2) * ((y2 - y0) / (x2 - x0)) and y3 - y2 < (x3 - x2) * (
                        (y2 - y0) / (x2 - x0)):
                    print("%.2f" % (((((y2 + y0) / 2)) * abs(x2 - x0)) - (1 / 2 * abs(
                        (((x0 * y2) + (x2 * y3) + (x3 * y0)) - ((y0 * x2) + (y2 * x3) + (y3 * x0)))))))

                elif y1 > y2 and y1 - y2 < (x1 - x2) * ((y2 - y0) / (x2 - x0)) and y3 - y2 < (x3 - x2) * (
                        (y2 - y0) / (x2 - x0)) and b > a:
                    print("%.2f" % (((((y2 + y0) / 2)) * abs(x2 - x0)) - (1 / 2 * abs(
                        (((x0 * y1) + (x1 * y2) + (x2 * y0)) - ((y0 * x1) + (y1 * x2) + (y2 * x0)))))))

                elif y1 > y2 and y1 - y2 > (x1 - x2) * ((y2 - y0) / (x2 - x0)) and y3 - y2 > (x3 - x2) * (
                        (y2 - y0) / (x2 - x0)) and a > b:
                    print("%.2f" % (((((y2 + y0) / 2)) * abs(x2 - x0)) + (1 / 2 * abs(
                        (((x0 * y1) + (x1 * y2) + (x2 * y0)) - ((y0 * x1) + (y1 * x2) + (y2 * x0)))))))

                elif y1 > y2 and y1 - y2 > (x1 - x2) * ((y2 - y0) / (x2 - x0)) and y3 - y2 > (x3 - x2) * (
                        (y2 - y0) / (x2 - x0)) and b > a:
                    print("%.2f" % (((((y2 + y0) / 2)) * abs(x2 - x0)) + (1 / 2 * abs(
                        (((x0 * y2) + (x2 * y3) + (x3 * y0)) - ((y0 * x2) + (y2 * x3) + (y3 * x0)))))))



    elif max(max_x_mesafe) == abs(x1 - x3) and x1 != x2 and x0 != x3 and x2 != x3:
        if y0 > y2:
            if y1 > y0 and y2 - y3 > (x2 - x3) * ((y3 - y1) / (x3 - x1)):
                print("%.2f" % (((((y1 + y3) / 2)) * abs(x1 - x3)) + (
                            1 / 2 * abs((((x2 * y1) + (x1 * y3) + (x3 * y2)) - ((y2 * x1) + (y1 * x3) + (y3 * x2)))))))
            elif y1 > y0 and y2 - y3 < (x2 - x3) * ((y3 - y1) / (x3 - x1)):
                print("%.2f" % (((((y1 + y3) / 2)) * abs(x1 - x3)) - (
                            1 / 2 * abs((((x2 * y1) + (x1 * y3) + (x3 * y2)) - ((y2 * x1) + (y1 * x3) + (y3 * x2)))))))
            elif y0 > y1:
                if y2 > y1 and y2 - y3 < (x2 - x3) * ((y3 - y1) / (x3 - x1)):
                    print("%.2f" % (((((y1 + y3) / 2)) * abs(x1 - x3)) - (
                                abs((((x1 * y2) + (x2 * y3) + (x3 * y1)) - ((y1 * x2 + (y2 * x3) + (y3 * x1))))) / 2)))
                elif y2 > y1 and y2 - y3 > (x2 - x3) * ((y3 - y1) / (x3 - x1)):
                    print("%.2f" % (((((y1 + y3) / 2)) * abs(x1 - x3)) + (
                                abs((((x1 * y2) + (x2 * y3) + (x3 * y1)) - ((y1 * x2 + (y2 * x3) + (y3 * x1))))) / 2)))
                elif y1 > y2 and y2 - y3 > (x2 - x3) * ((y3 - y1) / (x3 - x1)):
                    print("%.2f" % (((((y1 + y3) / 2)) * abs(x1 - x3)) + (1 / 2 * abs(
                        (((x2 * y1) + (x1 * y3) + (x3 * y2)) - ((y2 * x1) + (y1 * x3) + (y3 * x2)))))))
                elif y1 > y2 and y2 - y3 < (x2 - x3) * ((y3 - y1) / (x3 - x1)):
                    print("%.2f" % (((((y1 + y3) / 2)) * abs(x1 - x3)) - (1 / 2 * abs(
                        (((x2 * y1) + (x1 * y3) + (x3 * y2)) - ((y2 * x1) + (y1 * x3) + (y3 * x2)))))))
                elif y2 == y1 and y2 - y3 > (x2 - x3) * ((y3 - y1) / (x3 - x1)):
                    print("%.2f" % (((((y1 + y3) / 2)) * abs(x1 - x3)) + (
                                abs((((x1 * y2) + (x2 * y3) + (x3 * y1)) - ((y1 * x2 + (y2 * x3) + (y3 * x1))))) / 2)))
                elif y2 == y1 and y2 - y3 < (x2 - x3) * ((y3 - y1) / (x3 - x1)):
                    print("%.2f" % (((((y1 + y3) / 2)) * abs(x1 - x3)) - (
                                abs((((x1 * y2) + (x2 * y3) + (x3 * y1)) - ((y1 * x2 + (y2 * x3) + (y3 * x1))))) / 2)))
            elif y0 == y1 and y2 - y3 < (x2 - x3) * ((y3 - y1) / (x3 - x1)):
                print("%.2f" % (((((y1 + y3) / 2)) * abs(x1 - x3)) - (
                            abs((((x1 * y2) + (x2 * y3) + (x3 * y1)) - ((y1 * x2 + (y2 * x3) + (y3 * x1))))) / 2)))
            elif y0 == y1 and y2 - y3 > (x2 - x3) * ((y3 - y1) / (x3 - x1)):
                print("%.2f" % (((((y1 + y3) / 2)) * abs(x1 - x3)) + (
                            abs((((x1 * y2) + (x2 * y3) + (x3 * y1)) - ((y1 * x2 + (y2 * x3) + (y3 * x1))))) / 2)))

        elif y2 > y0:
            if y1 > y2 and y0 - y3 < (x0 - x3) * ((y3 - y1) / (x3 - x1)):
                print("%.2f" % (((((y1 + y3) / 2)) * abs(x1 - x3)) - (
                            1 / 2 * abs((((x0 * y1) + (x1 * y3) + (x3 * y0)) - ((y0 * x1) + (y1 * x3) + (y3 * x0)))))))
            elif y1 > y2 and y0 - y3 > (x0 - x3) * ((y3 - y1) / (x3 - x1)):
                print("%.2f" % (((((y1 + y3) / 2)) * abs(x1 - x3)) + (
                            1 / 2 * abs((((x0 * y1) + (x1 * y3) + (x3 * y0)) - ((y0 * x1) + (y1 * x3) + (y3 * x0)))))))
            elif y2 > y1:
                if y0 > y1 and y0 - y3 > (x0 - x3) * ((y3 - y1) / (x3 - x1)):
                    print("%.2f" % (((((y1 + y3) / 2)) * abs(x1 - x3)) + (1 / 2 * abs(
                        (((x0 * y1) + (x1 * y3) + (x3 * y0)) - ((y0 * x1) + (y1 * x3) + (y3 * x0)))))))
                elif y0 > y1 and y0 - y3 < (x0 - x3) * ((y3 - y1) / (x3 - x1)):
                    print("%.2f" % (((((y1 + y3) / 2)) * abs(x1 - x3)) - (1 / 2 * abs(
                        (((x0 * y1) + (x1 * y3) + (x3 * y0)) - ((y0 * x1) + (y1 * x3) + (y3 * x0)))))))
                elif y1 > y0 and y0 - y3 > (x0 - x3) * ((y3 - y1) / (x3 - x1)):
                    print("%.2f" % (((((y1 + y3) / 2)) * abs(x1 - x3)) + (1 / 2 * abs(
                        (((x0 * y1) + (x1 * y3) + (x3 * y0)) - ((y0 * x1) + (y1 * x3) + (y3 * x0)))))))
                elif y1 > y0 and y0 - y3 < (x0 - x3) * ((y3 - y1) / (x3 - x1)):
                    print("%.2f" % (((((y1 + y3) / 2)) * abs(x1 - x3)) - (1 / 2 * abs(
                        (((x0 * y1) + (x1 * y3) + (x3 * y0)) - ((y0 * x1) + (y1 * x3) + (y3 * x0)))))))
                elif y0 == y1 and y0 - y3 > (x0 - x3) * ((y3 - y1) / (x3 - x1)):
                    print("%.2f" % (((((y1 + y3) / 2)) * abs(x1 - x3)) + (1 / 2 * abs(
                        (((x0 * y1) + (x1 * y3) + (x3 * y0)) - ((y0 * x1) + (y1 * x3) + (y3 * x0)))))))
                elif y0 == y1 and y0 - y3 < (x0 - x3) * ((y3 - y1) / (x3 - x1)):
                    print("%.2f" % (((((y1 + y3) / 2)) * abs(x1 - x3)) - (1 / 2 * abs(
                        (((x0 * y1) + (x1 * y3) + (x3 * y0)) - ((y0 * x1) + (y1 * x3) + (y3 * x0)))))))
            elif y1 == y2 and y0 - y3 > (x0 - x3) * ((y3 - y1) / (x3 - x1)):
                print("%.2f" % (((((y1 + y3) / 2)) * abs(x1 - x3)) + (
                            1 / 2 * abs((((x0 * y1) + (x1 * y3) + (x3 * y0)) - ((y0 * x1) + (y1 * x3) + (y3 * x0)))))))
            elif y1 == y2 and y0 - y3 < (x0 - x3) * ((y3 - y1) / (x3 - x1)):
                print("%.2f" % (((((y1 + y3) / 2)) * abs(x1 - x3)) - (
                            1 / 2 * abs((((x0 * y1) + (x1 * y3) + (x3 * y0)) - ((y0 * x1) + (y1 * x3) + (y3 * x0)))))))
        elif y2 == y0:
            b = abs(((y1 - y3) / (x1 - x3)) * x0 - y0 - (((y1 - y3) / (x1 - x3)) * x3) + y3) / (
                        ((((y1 - y3) / (x1 - x3)) ** 2) + 1) ** (1 / 2))
            a = abs(((y1 - y3) / (x1 - x3)) * x2 - y2 - (((y1 - y3) / (x1 - x3)) * x3) + y3) / (
                        ((((y1 - y3) / (x1 - x3)) ** 2) + 1) ** (1 / 2))
            if y1 > y2:
                if y1 > y2 and y2 - y3 < (x2 - x3) * ((y3 - y1) / (x3 - x1)) and y0 - y3 < (x0 - x3) * (
                        (y3 - y1) / (x3 - x1)) and a > b:
                    print("%.2f" % (((((y1 + y3) / 2)) * abs(x1 - x3)) - (1 / 2 * abs(
                        (((x2 * y1) + (x1 * y3) + (x3 * y2)) - ((y2 * x1) + (y1 * x3) + (y3 * x2)))))))
                elif y1 > y2 and y2 - y3 < (x2 - x3) * ((y3 - y1) / (x3 - x1)) and y0 - y3 > (x0 - x3) * (
                        (y3 - y1) / (x3 - x1)):
                    print("%.2f" % (((((y1 + y3) / 2)) * abs(x1 - x3)) - (1 / 2 * abs(
                        (((x2 * y1) + (x1 * y3) + (x3 * y2)) - ((y2 * x1) + (y1 * x3) + (y3 * x2)))))))
                elif y1 > y2 and y2 - y3 > (x2 - x3) * ((y3 - y1) / (x3 - x1)) and y0 - y3 < (x0 - x3) * (
                        (y3 - y1) / (x3 - x1)):
                    print("%.2f" % (((((y1 + y3) / 2)) * abs(x1 - x3)) - (1 / 2 * abs(
                        (((x0 * y1) + (x1 * y3) + (x3 * y0)) - ((y0 * x1) + (y1 * x3) + (y3 * x0)))))))

                elif y1 > y2 and y2 - y3 < (x2 - x3) * ((y3 - y1) / (x3 - x1)) and y0 - y3 < (x0 - x3) * (
                        (y3 - y1) / (x3 - x1)) and b > a:
                    print("%.2f" % (((((y1 + y3) / 2)) * abs(x1 - x3)) - (1 / 2 * abs(
                        (((x0 * y1) + (x1 * y3) + (x3 * y0)) - ((y0 * x1) + (y1 * x3) + (y3 * x0)))))))
                elif y1 > y2 and y2 - y3 > (x2 - x3) * ((y3 - y1) / (x3 - x1)) and y0 - y3 > (x0 - x3) * (
                        (y3 - y1) / (x3 - x1)) and a > b:
                    print("%.2f" % (((((y1 + y3) / 2)) * abs(x1 - x3)) + (1 / 2 * abs(
                        (((x0 * y1) + (x1 * y3) + (x3 * y0)) - ((y0 * x1) + (y1 * x3) + (y3 * x0)))))))
                elif y1 > y2 and y2 - y3 > (x2 - x3) * ((y3 - y1) / (x3 - x1)) and y0 - y3 > (x0 - x3) * (
                        (y3 - y1) / (x3 - x1)) and b > a:
                    print("%.2f" % (((((y1 + y3) / 2)) * abs(x1 - x3)) + (1 / 2 * abs(
                        (((x2 * y1) + (x1 * y3) + (x3 * y2)) - ((y2 * x1) + (y1 * x3) + (y3 * x2)))))))
            elif y2 > y1:
                if y1 < y2 and y2 - y3 < (x2 - x3) * ((y3 - y1) / (x3 - x1)) and y0 - y3 < (x0 - x3) * (
                        (y3 - y1) / (x3 - x1)) and a > b:
                    print("%.2f" % (((((y1 + y3) / 2)) * abs(x1 - x3)) - (1 / 2 * abs(
                        (((x2 * y1) + (x1 * y3) + (x3 * y2)) - ((y2 * x1) + (y1 * x3) + (y3 * x2)))))))
                elif y1 < y2 and y2 - y3 < (x2 - x3) * ((y3 - y1) / (x3 - x1)) and y0 - y3 > (x0 - x3) * (
                        (y3 - y1) / (x3 - x1)):
                    print("%.2f" % (((((y1 + y3) / 2)) * abs(x1 - x3)) - (1 / 2 * abs(
                        (((x2 * y1) + (x1 * y3) + (x3 * y2)) - ((y2 * x1) + (y1 * x3) + (y3 * x2)))))))
                elif y1 < y2 and y2 - y3 > (x2 - x3) * ((y3 - y1) / (x3 - x1)) and y0 - y3 < (x0 - x3) * (
                        (y3 - y1) / (x3 - x1)):
                    print("%.2f" % (((((y1 + y3) / 2)) * abs(x1 - x3)) - (1 / 2 * abs(
                        (((x0 * y1) + (x1 * y3) + (x3 * y0)) - ((y0 * x1) + (y1 * x3) + (y3 * x0)))))))

                elif y1 < y2 and y2 - y3 < (x2 - x3) * ((y3 - y1) / (x3 - x1)) and y0 - y3 < (x0 - x3) * (
                        (y3 - y1) / (x3 - x1)) and b > a:
                    print("%.2f" % (((((y1 + y3) / 2)) * abs(x1 - x3)) - (1 / 2 * abs(
                        (((x0 * y1) + (x1 * y3) + (x3 * y0)) - ((y0 * x1) + (y1 * x3) + (y3 * x0)))))))
                elif y1 < y2 and y2 - y3 > (x2 - x3) * ((y3 - y1) / (x3 - x1)) and y0 - y3 > (x0 - x3) * (
                        (y3 - y1) / (x3 - x1)) and a > b:
                    print("%.2f" % (((((y1 + y3) / 2)) * abs(x1 - x3)) + (1 / 2 * abs(
                        (((x0 * y1) + (x1 * y3) + (x3 * y0)) - ((y0 * x1) + (y1 * x3) + (y3 * x0)))))))
                elif y1 < y2 and y2 - y3 > (x2 - x3) * ((y3 - y1) / (x3 - x1)) and y0 - y3 > (x0 - x3) * (
                        (y3 - y1) / (x3 - x1)) and b > a:
                    print("%.2f" % (((((y1 + y3) / 2)) * abs(x1 - x3)) + (1 / 2 * abs(
                        (((x2 * y1) + (x1 * y3) + (x3 * y2)) - ((y2 * x1) + (y1 * x3) + (y3 * x2)))))))



    elif max(max_x_mesafe) == abs(x1 - x3) and x1 != x2 and x0 != x3 and x2 == x3:
        if y0 > y2:
            if y1 > y0:
                print("%.2f" % (((((y1 + y3) / 2)) * abs(x1 - x3)) - (
                        1 / 2 * abs((((x2 * y1) + (x1 * y3) + (x3 * y2)) - ((y2 * x1) + (y1 * x3) + (y3 * x2)))))))
            elif y0 > y1:
                if y2 > y1:
                    print("%.2f" % (((((y1 + y3) / 2)) * abs(x1 - x3)) - (
                            abs((((x1 * y2) + (x2 * y3) + (x3 * y1)) - ((y1 * x2 + (y2 * x3) + (y3 * x1))))) / 2)))
                elif y1 >= y2:
                    print("%.2f" % (((((y1 + y3) / 2)) * abs(x1 - x3)) - (1 / 2 * abs(
                        (((x2 * y1) + (x1 * y3) + (x3 * y2)) - ((y2 * x1) + (y1 * x3) + (y3 * x2)))))))

        elif y2 > y0:
            if y1 > y2 and y0 - y3 > (x0 - x3) * ((y3 - y1)) / (x3 - x1):
                print("%.2f" % (((((y1 + y3) / 2)) * abs(x1 - x3)) + (
                        1 / 2 * abs((((x0 * y1) + (x1 * y3) + (x3 * y0)) - ((y0 * x1) + (y1 * x3) + (y3 * x0)))))))
            elif y1 > y2 and y0 - y3 > (x0 - x3) * ((y3 - y1)) / (x3 - x1):
                print("%.2f" % (((((y1 + y3) / 2)) * abs(x1 - x3)) - (
                        1 / 2 * abs((((x0 * y1) + (x1 * y3) + (x3 * y0)) - ((y0 * x1) + (y1 * x3) + (y3 * x0)))))))
            elif y2 == y1 and y0 - y3 > (x0 - x3) * ((y3 - y1)) / (x3 - x1):
                print("%.2f" % (((((y1 + y3) / 2)) * abs(x1 - x3)) + (
                        1 / 2 * abs((((x0 * y1) + (x1 * y3) + (x3 * y0)) - ((y0 * x1) + (y1 * x3) + (y3 * x0)))))))
            elif y2 == y1 and y0 - y3 < (x0 - x3) * ((y3 - y1)) / (x3 - x1):
                print("%.2f" % (((((y1 + y3) / 2)) * abs(x1 - x3)) - (
                        1 / 2 * abs((((x0 * y1) + (x1 * y3) + (x3 * y0)) - ((y0 * x1) + (y1 * x3) + (y3 * x0)))))))
            elif y2 > y1:
                if y0 > y1 and y0 - y3 > (x0 - x3) * ((y3 - y1) / (x3 - x1)):
                    print("%.2f" % (((((y1 + y3) / 2)) * abs(x1 - x3)) + (1 / 2 * abs(
                        (((x0 * y1) + (x1 * y3) + (x3 * y0)) - ((y0 * x1) + (y1 * x3) + (y3 * x0)))))))
                elif y0 > y1 and y0 - y3 < (x0 - x3) * ((y3 - y1) / (x3 - x1)):
                    print("%.2f" % (((((y1 + y3) / 2)) * abs(x1 - x3)) - (1 / 2 * abs(
                        (((x0 * y1) + (x1 * y3) + (x3 * y0)) - ((y0 * x1) + (y1 * x3) + (y3 * x0)))))))
                elif y1 > y0 and y0 - y3 < (x0 - x3) * ((y3 - y1) / (x3 - x1)):
                    print("%.2f" % (((((y1 + y3) / 2)) * abs(x1 - x3)) - (1 / 2 * abs(
                        (((x0 * y1) + (x1 * y3) + (x3 * y0)) - ((y0 * x1) + (y1 * x3) + (y3 * x0)))))))
                elif y1 > y0 and y0 - y3 > (x0 - x3) * ((y3 - y1) / (x3 - x1)):
                    print("%.2f" % (((((y1 + y3) / 2)) * abs(x1 - x3)) + (1 / 2 * abs(
                        (((x0 * y1) + (x1 * y3) + (x3 * y0)) - ((y0 * x1) + (y1 * x3) + (y3 * x0)))))))
                elif y1 == y0 and y0 - y3 > (x0 - x3) * ((y3 - y1) / (x3 - x1)):
                    print("%.2f" % (((((y1 + y3) / 2)) * abs(x1 - x3)) + (1 / 2 * abs(
                        (((x0 * y1) + (x1 * y3) + (x3 * y0)) - ((y0 * x1) + (y1 * x3) + (y3 * x0)))))))
                elif y1 == y0 and y0 - y3 < (x0 - x3) * ((y3 - y1) / (x3 - x1)):
                    print("%.2f" % (((((y1 + y3) / 2)) * abs(x1 - x3)) - (1 / 2 * abs(
                        (((x0 * y1) + (x1 * y3) + (x3 * y0)) - ((y0 * x1) + (y1 * x3) + (y3 * x0)))))))
        elif y2 == y0:
            if y1 > y2 and y0 - y3 > (x0 - x3) * (((y3 - y1)) / (x3 - x1)):
                print("%.2f" % (((((y1 + y3) / 2)) * abs(x1 - x3)) + (
                        1 / 2 * abs((((x0 * y1) + (x1 * y3) + (x3 * y0)) - ((y0 * x1) + (y1 * x3) + (y3 * x0)))))))
            elif y1 > y2 and y0 - y3 < (x0 - x3) * ((y3 - y1) / (x3 - x1)):
                print("%.2f" % (((((y1 + y3) / 2)) * abs(x1 - x3)) - (
                        1 / 2 * abs((((x0 * y1) + (x1 * y3) + (x3 * y0)) - ((y0 * x1) + (y1 * x3) + (y3 * x0)))))))
            elif y2 > y1:
                if y0 > y1 and y2 - y3 > (x2 - x3) * ((y3 - y1) / (x3 - x1)):
                    print("%.2f" % (((((y1 + y3) / 2)) * abs(x1 - x3)) + (1 / 2 * abs(
                        (((x2 * y1) + (x1 * y3) + (x3 * y2)) - ((y2 * x1) + (y1 * x3) + (y3 * x2)))))))

                elif y0 > y1 and y2 - y3 < (x2 - x3) * ((y3 - y1) / (x3 - x1)):
                    print("%.2f" % (((((y1 + y3) / 2)) * abs(x1 - x3)) - (1 / 2 * abs(
                        (((x2 * y1) + (x1 * y3) + (x3 * y2)) - ((y2 * x1) + (y1 * x3) + (y3 * x2)))))))
