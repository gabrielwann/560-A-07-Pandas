# https://goheels.com/sports/mens-basketball/roster 

import pandas as pd


player = {"Last Name": ["Cadeau", "Davis", "Washington", "Withers", "Trimble", "Jackson", 
                        "Powell", "Hawkins", "Lubin", "Holbrook"],
          "FirstName": ["Elliot", "RJ", "Jalen", "Jaelyn", "Seth", "Ian", 
                        "Drake", "Russell", "Ven-Allen", "John"],
          "height": [73, 72, 80, 79, 75, 76, 
                     78, 73, 80, 80],  
          "weight": [180, 180, 190, 195, 185, 190, 
                     195, 175, 230, 230]} 

data = pd.DataFrame(player)


data["bmi"] = ((data["weight"] / 2.205) / ((data["height"] / 39.37) ** 2)).round(3)

print(data)

data.to_csv("bmi.csv", index=False)



