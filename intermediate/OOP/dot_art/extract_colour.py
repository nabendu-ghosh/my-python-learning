import colorgram

class ExtractColours:
    
    def __init__(self, image_name, no_of_colours):
        self.no_of_colours = no_of_colours
        self.image_name = image_name
    
    def get_colours(self):
        list_of_colours = []
        colours = colorgram.extract(self.image_name, self.no_of_colours)
        for i in range(self.no_of_colours):
            r = colours[i].rgb.r
            g = colours[i].rgb.g
            b = colours[i].rgb.b
            if r + g + b < 700:
                list_of_colours.append((r, g, b))
        return list_of_colours