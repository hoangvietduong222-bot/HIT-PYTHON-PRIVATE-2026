score = 10
classification = None
# TODO: dung if/elif/else de gan classification
if(score<0 and score >10):
    classification = "Không hợp lệ"
elif(score >= 8):
    classification = "Tot"
elif(score>=5):
    classification = "Dat"
else:
    classification = "Can co gang"

print(classification)