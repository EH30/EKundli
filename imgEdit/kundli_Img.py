from PIL import Image, ImageDraw, ImageFont, ImageTk, ImageFilter



PLANETS = {
    "sun": "Sun", 
    "moon": "Moon", 
    "mercury": "Mercury", 
    "venus": "Venus", 
    "mars": "Mars", 
    "jupiter": "Jupiter", 
    "saturn": "Saturn", 
    "rahu": "Rahu",
    "ketu": "Ketu",
    "uranus": "Uranus", 
    "pluto": "Pluto",
    "neptune": "Neptune" 
}

class EditImg:
    def write_to_image(self, kundli, image_pos, kundli_img, mode):
        img = Image.open(kundli_img)
        font_sign   = ImageFont.truetype("arial.ttf", 24)
        font_planet = ImageFont.truetype("arial.ttf", 26)
        draw = ImageDraw.Draw(img)
        house = 0
        if mode == 0:
            for item in image_pos:
                draw.text(image_pos[item]["sign_pos"], str(kundli[house].sign_num), (0,0,0), font=font_sign)
                temp = 0
                if house == 0 :
                    draw.text((image_pos[item]["planet_pos"][0], image_pos[item]["planet_pos"][1]+temp), "Asc", (0,0,0), font=font_planet)
                    temp += 30
                if len(kundli[house].planets) != 0:
                    for planet in kundli[house].planets:
                        draw.text((image_pos[item]["planet_pos"][0], image_pos[item]["planet_pos"][1]+temp), PLANETS[str(planet)], (0,0,0), font=font_planet)
                        temp += 30
                house += 1
        elif mode == 1:
            for item in image_pos:
                draw.text(image_pos[item]["sign_pos"], str(kundli[house].sign_num), (0,0,0), font=font_sign)
                temp = 0
                if kundli[house].asc_signlon != None:
                    draw.text((image_pos[item]["planet_pos"][0], image_pos[item]["planet_pos"][1]+temp), "Asc", (0,0,0), font=font_planet)
                    temp += 30
                if len(kundli[house].planets) != 0:
                    for planet in kundli[house].planets:
                        draw.text((image_pos[item]["planet_pos"][0], image_pos[item]["planet_pos"][1]+temp), PLANETS[str(planet)], (0,0,0), font=font_planet)
                        temp += 30
                house += 1
        elif mode == 2:
            for item in image_pos:
                draw.text(image_pos[item]["sign_pos"], str(kundli[house].sign_num), (0,0,0), font=font_sign)
                temp = 0
                if house == 0:
                    draw.text((image_pos[item]["planet_pos"][0], image_pos[item]["planet_pos"][1]+temp), "Asc", (0,0,0), font=font_planet)
                    temp += 30
                if len(kundli[house].planets) != 0:
                    for planet in kundli[house].planets:
                        draw.text((image_pos[item]["planet_pos"][0], image_pos[item]["planet_pos"][1]+temp), PLANETS[str(planet)], (0,0,0), font=font_planet)
                        temp += 30
                house += 1
        return img

