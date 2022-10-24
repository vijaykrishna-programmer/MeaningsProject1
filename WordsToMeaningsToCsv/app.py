from PyDictionary import PyDictionary

dictionary1 = PyDictionary()

import pandas as pd

mywordlist_initial = input().split(",")
print(mywordlist_initial)

mywordlist = ["adulterate" ,"vacillate" ,'pedant' ,'laudable' ,'gullible', 'desiccate' ,'audacious' ,'abstain' ,'zeal' ,'placate' ,'fervid' ,'enigma','prodigal','opaque' ,'erudite' ,'assuage' ,'precipitate' ,'audacious' ,'lucid' ,'equivocal' ]   #["zeal" ,"lucid"]

# ["adulterate" ,"vacillate" ,'pedant' ,'laudable' ,'gullible', 'desiccate' ,'audacious' ,'abstain' ,'zeal' ,'placate' ,'fervid' ,'enigma','prodigal','opaque' ,'erudite' ,'assuage' ,'precipitate' ,'audacious' ,'lucid' ,'equivocal' ]

Words_List = []
Meanings_List = []

for word in mywordlist:
  # print(word)

  meanings = dictionary1.meaning(word)
  
  Entire_Meaning = " "
  for key,Values in meanings.items():


    for i in range(len(Values)):
      Entire_Meaning = Entire_Meaning + "\n" + str(i) + ". "+ Values[i] + "\n "


  # print(Entire_Meaning)

  Words_List.append(word)
  Meanings_List.append(Entire_Meaning)

# print(Words_dictionary)

My_dictonary = {"Word":Words_List, "Meanings": Meanings_List } 
df = pd.DataFrame(My_dictonary)

print(df)

df.to_csv('file1.csv')


