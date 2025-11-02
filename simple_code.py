#Create a dictionary containing the keys and matching values for all the team members(make sure it is matching in the exact order for all members)
team = {
  "Name": ["Santosh","Svetlana","Debangana","Hana E", "Gideon Danso", "Mosunmola Temitope Christianah", "Jegede Judah Olayemi", "Adewumi Esther Adeola"],
  "Slack Username": ["Santosh T","Svetlana Sokolova","debangana","Hana E", "Joegidi4real", "Temmy", "Jegede Judah", "adewumiesther"],
  "Country": ["United States of America","United Kingdom","United Kingdom","Canada", "Ghana", "Nigeria", "Nigeria", "Nigeria"],
  "Hobby": ["Tennis","Playing Piano","Badminton","Hiking", "Listening to music", "Cooking", "Playing Soccer", "Cooking"],
  "Affiliation": ["University of Texas at San Antonio","Queens University Belfast","Queens University Belfast (Alumna)","Boise State University", "University of Cape Coast", "Obafemi Awolowo University", "Obafemi Awolowo University", "Obafemi Awolowo University"],
  "Favourite Gene": ["IFNB1- ATTCTAACTGCAACCTTTCGAAGCCTTTGCTCTGGCAC","TP53-TCCTACAGTACTCCCCTGCCCTCAACATGTG","BRCA1- ATGGATTTATCTGCTCTTCGCGTTGAAGAAGTACAA","glnD- AGGAAACGCAGATAGCGGGGCCTTGCGGAGAGAG", "BRCA2- GACCACTCTAAGCTTTTGTAAGATCGGCTCGC", "TNNT2- AGTCCCCGCTGAGACTGAGCAGACGCCTCCAG", "POSTN- GCCAGTTCTCTTCGGGGACTAACTGCAACGGAGAGA", "TP53-TCCTACAGTACTCCCCTGCCCTCAACATGTG"]
}

print(f"-------------------------------Members of Team_Phenylalanine----------------------------------------") #Print a title at the top
print()
for i in range(len(team["Name"])): #Set the possible number of iterations to run the loop(based on the # of values in each key)
    #each iteration prints out the matching values for different keys = 1 member 
    print(f"---Member#{i+1}---") #Print the team member # based on the index(1st member is index 1 and adds 1 every iteration)
    print(f"Name: {team['Name'][i]}") #print the name based on the iteration number 
    print(f"Slack Username: {team['Slack Username'][i]}") #print the slack username based on the iteration number 
    print(f"Country: {team['Country'][i]}") #print the country for based on the iteration number 
    print(f"Hobby: {team['Hobby'][i]}") #print the hobby based on the iteration number 
    print(f"Affiliation: {team['Affiliation'][i]}") #print the affiliation based on the iteration number
    print(f"Favourite Gene: {team['Favourite Gene'][i]}")  #print the affiliation based on the iteration number
    print() #Add space between each section    