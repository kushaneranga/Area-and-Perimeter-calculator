print("Area and Perimeter calculator (for Plane Shapes)")
print("""
Things that can be calculated:
    01. Area.
    02. Perimeter.
""")
mi_list = ["area", "perimeter"]
while True:
    main_input = str(input("What is needed to calculate (Area,Perimeter)? ").lower())
    if main_input in mi_list:
        break
    else:
        print("Please check the spelling, tye again!")

if main_input == "area":
    print("""
    Shapes:
        01. Square          02. Rectangle
        03. Parallelogram   04. Trapezoid
        05. Triangle        06. Circle
        07. Ellipse         08. Sector
    """)


    class area:
        sa_list = ["square", "rectangle", "parallelogram", "trapezoid",
                   "triangle", "circle", "ellipse", "sector"]

        def __init__(self):
            self.h = 0
            self.w = 0
            self.a = 0
            self.r = 0
            self.q = 0
            self.square = 0
            self.rectangle = 0
            self.parallelogram = 0
            self.trapezoid = 0
            self.triangle = 0
            self.circle = 0
            self.ellipse = 0
            self.sector = 0

        def SquareArea(self):
            self.h = float(input("length of side: "))
            self.square = (self.h ** 2)
            print("Area of square: ", self.square)

        def RectangleArea(self):
            self.w = float(input("width: "))
            self.h = float(input("height: "))
            self.rectangle = (self.w * self.h)
            print("Area of rectangle: ", self.rectangle)

        def ParallelogramArea(self):
            self.w = float(input("base: "))
            self.h = float(input("vertical height: "))
            self.parallelogram = (self.w * self.h)
            print("Area of parallelogram: ", self.parallelogram)

        def TrapezoidArea(self):
            self.w = float(input("long base: "))
            self.a = float(input("short base: "))
            self.h = float(input("height: "))
            self.trapezoid = ((self.w + self.a) / 2) * self.h
            print("Area of trapezoid: ", self.trapezoid)

        def TriangleArea(self):
            self.w = float(input("base: "))
            self.h = float(input("vertical height: "))
            self.triangle = (self.w * self.h) / 2
            print("Area of triangle: ", self.triangle)

        def CircleArea(self):
            self.r = float(input("radius: "))
            self.circle = ((22 / 7) * (self.r ** 2))
            print("Area of circle: ", self.circle)

        def EllipseArea(self):
            self.w = float(input("major axis (a axis): "))
            self.h = float(input("minor axis (b axis): "))
            self.ellipse = ((22 / 7) * self.h * self.w)
            print("Area of ellipse: ", self.ellipse)

        def SectorArea(self):
            self.r = float(input("radius: "))
            while True:
                self.q = float(input("angle in radians: "))
                if self.q <= 360:
                    break
                else:
                    print("Angle is not possible, try again!")
            self.sector = ((self.q / 360) * (22 / 7) * (self.r ** 2))
            print("Area of sector: ", self.sector)


    call0 = area()
    while True:
        inputArea_shape = str(input("What shapes do you need to calculate the area?: ")).lower()
        if inputArea_shape in area.sa_list:
            break
        else:
            print("Please check the spelling, tye again!")

    call1 = area()
    if inputArea_shape == "square":
        call1.SquareArea()
    elif inputArea_shape == "rectangle":
        call1.RectangleArea()
    elif inputArea_shape == "parallelogram":
        call1.ParallelogramArea()
    elif inputArea_shape == "trapezoid":
        call1.TrapezoidArea()
    elif inputArea_shape == "triangle":
        call1.TriangleArea()
    elif inputArea_shape == "circle":
        call1.CircleArea()
    elif inputArea_shape == "ellipse":
        call1.EllipseArea()
    else:
        call1.SectorArea()
else:
    print("""
    Shapes:
        01. Square          02. Rectangle
        03. Quadrilateral   04. Triangle
        05. Circle          06. Sector
    """)


    class perimeter:
        sp_list = ["square", "rectangle", "quadrilateral", "triangle", "circle", "sector"]

        def __init__(self):
            self.h = 0
            self.w = 0
            self.a = 0
            self.b = 0
            self.r = 0
            self.q = 0
            self.square = 0
            self.rectangle = 0
            self.quadrilateral = 0
            self.triangle = 0
            self.circle = 0
            self.sector = 0

        def SquarePerimeter(self):
            self.h = float(input("length of side: "))
            self.square = (self.h * 4)
            print("Perimeter of square: ", self.square)

        def RectanglePerimeter(self):
            self.h = float(input("height: "))
            self.w = float(input("width: "))
            self.rectangle = ((self.h * 2) + (self.w * 2))
            print("Perimeter of rectangle: ", self.rectangle)

        def QuadrilateralPerimeter(self):
            self.h = float(input("a axis: "))
            self.w = float(input("b axis: "))
            self.a = float(input("c axis: "))
            self.b = float(input("d axis: "))
            self.quadrilateral = (self.h + self.w + self.a + self.b)
            print("Perimeter of quadrilateral: ", self.quadrilateral)

        def TrianglePerimeter(self):
            self.h = float(input("a axis: "))
            self.w = float(input("b axis: "))
            self.a = float(input("c axis: "))
            self.triangle = (self.h + self.w + self.a)
            print("Perimeter of triangle: ", self.triangle)

        def CirclePerimeter(self):
            self.r = float(input("radius: "))
            self.circle = (2 * (22 / 7) * self.r)
            print("Perimeter of circle: ", self.circle)

        def SectorPerimeter(self):
            self.r = float(input("radius: "))
            while True:
                self.q = float(input("angle in radians: "))
                if self.q < 360:
                    break
                else:
                    print("Angle is not possible, try again!")
            self.sector = ((self.q / 360) * (2 * (22 / 7) * self.r)) + (2 * self.r)
            print("Perimeter of sector: ", self.sector)


    callP0 = perimeter()
    while True:
        inputPerimeter_shape = str(input("What shapes do you need to calculate the perimeter?: ")).lower()
        if inputPerimeter_shape in perimeter.sp_list:
            break
        else:
            print("Please check the spelling, tye again!")

    callP1 = perimeter()
    if inputPerimeter_shape == "square":
        callP1.SquarePerimeter()
    elif inputPerimeter_shape == "rectangle":
        callP1.RectanglePerimeter()
    elif inputPerimeter_shape == "quadrilateral":
        callP1.QuadrilateralPerimeter()
    elif inputPerimeter_shape == "triangle":
        callP1.TrianglePerimeter()
    elif inputPerimeter_shape == "circle":
        callP1.CirclePerimeter()
    else:
        callP1.SectorPerimeter()

print("Thank you!!")
