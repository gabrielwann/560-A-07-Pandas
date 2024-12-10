# https://goheels.com/sports/mens-basketball/roster 

import pandas as pd

player = {"Last Name": ["Cadeau", "Davis", "Washington", "Withers", "Trimble", "Jackson"],
          "FirstName": ["Elliot", "RJ", "Jalen", "Jaelyn", "Seth", "Ian"],
          "height": [73, 72, 80, 79, 75, 76],
          "weight": [180, 180, 190, 195, 185, 190]}
data = pd.DataFrame(player)
print(data)



