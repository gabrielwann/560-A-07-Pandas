# https://goheels.com/sports/mens-basketball/roster 

import pandas as pd

roster = ["Cadeau", "Davis", "Washington", "Withers", "Trimble", "Jackson" ]
player = {"Last Name": roster}
data = pd.DataFrame(roster)
print(data)

