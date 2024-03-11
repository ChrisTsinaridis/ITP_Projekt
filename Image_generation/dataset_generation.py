from PIL import Image, ImageDraw, ImageFont
import random
import os

os.makedirs("checkbox_images", exist_ok=True)

def create_box_with_X(number):
   for i in range(number):
      # Pfad zur handschriftlichen Schriftart 
      font_list = ["./Image_generation/ttf/Autography.otf",
                  ]
         
       
      font_path = random.choice(font_list)

       # Festlegen der Bildgröße
      image_size = (500, 500)

      # Berechnen der Boxgröße als 10% kleiner als die Bildgröße
      box_padding = int(image_size[0] * 0.1)  # 10% Padding
      box_size = (box_padding, box_padding, image_size[0] - box_padding, image_size[1] - box_padding)

      # Erstelle ein weißes Bild
      image = Image.new('RGB', image_size, 'white')
      draw = ImageDraw.Draw(image)

      # Zeichne eine Box
      draw.rectangle(box_size, outline='black', width=2)

      draw_x = random.choice([True, False])

      # Lade die handschriftliche Schriftart
      if draw_x:
         # Die Schriftgröße wird auf 80% der Boxbreite gesetzt
         font_size = int((box_size[2] - box_size[0]) * 1)
         font = ImageFont.truetype(font_path, font_size)

         # Generiere eine zufällige Position für das "X" innerhalb des Kästchens
         padding = int(font_size * 0.3)  # 10% der Schriftgröße als Rand für das "X"
         x_min = box_size[0] + padding
         y_min = box_size[1] + padding
         x_max = box_size[2] - padding
         y_max = box_size[3] - padding

         # Zufällige Koordinaten für das "X"
         x_random = random.randint(x_min, x_max)
         y_random = random.randint(y_min, y_max)

         # Zeichne das "X" an der zufälligen Position
         draw.text((x_random, y_random), "X", font=font, fill='black', anchor="mm")

      # Speichere das Bild
      image_filename = f"checkbox_images/checkbox{i+1}.png"
      image.save(image_filename)

create_box_with_X(240)