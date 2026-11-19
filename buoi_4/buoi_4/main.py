#bài 1
def normalize_name(text):
    return " ".join(text.split())

print(normalize_name("  Nguyễn   An  "))
print(normalize_name("minh"))
print(normalize_name("   "))

#Bài 2
def average_score(scores):
    if not scores:
        return None
    total = 0
    for score in scores:
        total += score
    return total / len(scores)

def count_passed(scores, threshold=5):
    count = 0
    for score in scores:
        if score >= threshold:
            count += 1
    return count
sc = [[8, 4, 9, 5], [5], []]
for s in sc:
    print(s, "-> TB:", average_score(s), "| Ngưỡng 5:", count_passed(s), "| Ngưỡng 8:", count_passed(s, 8))


#Bài 3
def rank_students(score_by_name):
    """Trả về dict mới xếp hạng theo điểm giảm dần, bằng điểm thì tên A-Z."""
    sorted_items = sorted(score_by_name.items(), key=lambda item: (-item[1], item[0]))
    return dict(sorted_items)


score_by_name = {"Minh": 9, "Lan": 7, "An": 9, "Vy": 5}
ranked = rank_students(score_by_name)

print("Kết quả xếp hạng:", ranked)     
print("Dict ban đầu:", score_by_name)
print("Dict rỗng:", rank_students({}))