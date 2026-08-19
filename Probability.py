import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

np.random.seed(42)

n = 1000
# outcomes = np.random.choice(['H','T'],size = n) # ! so it creates an array with n elements in it and in that it can be either h or t
# print(outcomes[:150])
# heads = np.sum(outcomes='H')
# tails = np.sum(outcomes='T')

# print('Head:',heads)
# print('Tails:',tails)

dice = np.random.randint(1,7,size=n)
p_dice = np.mean(dice == 4)
# # print("Probability of 4 = ",p_dice)

# vals, counts = np.unique(dice,return_counts=True) #! YOU CAN PASS ANY ARRAY THROUGH IT AND WHAT THIS SAYS IS "FIND THE UNIQUE VALUES AND HOW MANY TIMES THEY HAVE APPEARED"
# print(vals)
# print(counts)
# sns.histplot(dice,discrete=True,kde=True)
# plt.show()

data = pd.DataFrame({
    'Likes ML': np.random.choice([1,0] ,size =100,p=[0.6,0.4]) #? iska idhar matlab hai ki out of 100,60% chance h ki kisi bande ko ml pasand ho 
})
data ["Likes DL"] = [
    np.random.choice([1,0], p = [0.7,0.3]) if ml else #? ML pasand hai = Matlab 70% chance hai ki DL bhi pasand ho (1) aur 30% chance hai ki nahi ho (0).
    np.random.choice([1,0], p = [ 0.2,0.8])
                     for ml in data['Likes ML'] #? ML nahi pasand hai = Matlab 80% chance hai ki value 9 ho aur 20% chance hai ki 1 ho
]

z = data.head()
print(z)

p_ml = data['Likes DL'].mean()
p_dl = data['Likes ML'].mean()

print(round(p_ml,2))
print(round(p_dl,2))