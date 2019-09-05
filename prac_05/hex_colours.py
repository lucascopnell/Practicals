HEX_COLOURS = {"beige": "#f5f5dc", "bisque3": "#cdb79e", "black": "#000000", "brown": "#a52a2a", "burlywood": "#deb887",
               "cadetblue": "#5f9ea0", "chartreuse1": "#7fff00", "coral": "#ff7f50", "cornflowerblue": "#6495ed", "cyan3": "#00cdcd" }



colour = input("Enter colour name: ").lower()
while colour != "":
    if colour in HEX_COLOURS:
        print("{} hex code is {}".format(colour, HEX_COLOURS[colour]))
    else:
        print("Invalid colour")
    colour = input("Enter colour name: ")

