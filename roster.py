# https://goheels.com/sports/mens-basketball/roster 

import pandas as pd

roster = ["Cadeau", "Davis", "Washington", "Withers", "Trimble", "Jackson" ]
player = {"Last Name": roster,
          "FirstName": ["Elliot", "RJ", "Jalen", "Jaelyn", "Seth", "Ian"],
          "height": [73, 72, 80, 79, 75, 76],
          "weight": [180, 180, 190, 195, 185, 190]}
data = pd.DataFrame(player)
print(data)



