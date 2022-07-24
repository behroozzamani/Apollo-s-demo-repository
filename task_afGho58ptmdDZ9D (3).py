
def countOfCurrentWord(input_str, word):
  splited_arr = input_str.split()
  count = 0
 
  for a in splited_arr:
    if word == a:
      count = count + 1
 
  return count
 
def remove(input_str, word, count_of_remove):
  words = input_str.split()
  new_str = ""
 
  count = 0
  for w in words:
    if (w != word) or (count >= count_of_remove):
      new_str = new_str + w + " "
    else:
      count = count + 1
 
  return new_str
 
s = input("Enter s : ").strip()
s = " ".join(s.split(','))
p = input("Enter p : ").strip()
w = int(input("Enter w : ").strip())
m = int(input("Enter m : ").strip())
r = countOfCurrentWord(s, p)
print("task1: ", s)

if r >= m:
    print("task2: ", remove(s, p, r - m))
else:
    print("task2: ", s)
