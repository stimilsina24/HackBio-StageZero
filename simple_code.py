#Importing Pandas
import pandas as pd

#Creating dictionary with Column names (key) and Adding Member information next to each Column name (Values)
data = {
  "Name": ["Santosh","Svetlana","Debangana","Hana E", "Gideon Danso", "Mosunmola Temitope Christianah", "Jegede Judah Olayemi"],
  "Slack Username": ["Svetlana Sokolova","Santosh T","debangana","Hana E", "Joegidi4real", "Hana E", "Jegede Judah"],
  "Country" :["United Kingdom","United States of America","United Kingdom","Canada", "Hana E", "Hana E", "Hana E"],
  "Hobby":["Playing Piano","Tennis","Badminton","Hiking", "Listening to music", "Cooking", "Playing Soccer"],
  "Affiliation":["Queens University Belfast","University of Texas at San Antonio","Queens University Belfast (Alumna)","Boise State University", "University of Cape Coast", "Obafemi Awolowo University", "Obafemi Awolowo University "],
  "Favourite Gene":["TP53:TCCTACAGTACTCCCCTGCCCTCAACATGTG","IFNB1: ATTCTAACTGCAACCTTTCGAAGCCTTTGCTCTGGCAC","BRCA1: ATGGATTTATCTGCTCTTCGCGTTGAAGAAGTACAA","glnD: AGGAAACGCAGATAGCGGGGCCTTGCGGAGAGAG", "BRCA2: GACCACTCTAAGCTTTTGTAAGATCGGCTCGC", "TNNT2: AGTCCCCGCTGAGACTGAGCAGACGCCTCCAG", "POSTN: GCCAGTTCTCTTCGGGGACTAACTGCAACGGAGAGA"]
}

#Converting the dictionary to Dataframe with custom row names for better clarity 
df = pd.DataFrame(data, index = ["Member 1", "Member 2", "Member 3","Member 4", "Member 5", "Member 6", "Member 7"])

#Print out the table
print(df)