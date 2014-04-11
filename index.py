
input_word = raw_input()

points = [["e, a, i, o, n, r, t, l, s, u", 1],
          ["d, g", 2],
          ["b, c, m, p", 3],
          ["f, h, v, w, y", 4],
          ["k", 5],
          ["j, x", 8],
          ["q, z", 10]
         ]

max_count = 0
t_max_count = 0
max_word = ""
flag = True

f1 = open("words.txt", "r")
for word in f1.readlines():
    flag = True
    for letter in input_word:
        if letter not in word:
            flag = False

    if flag and word.count(letter) == input_word.count(letter):
        for letter in word:
            for l in points:
                if letter in l[0]:
                    t_max_count += l[1]
        if t_max_count > max_count:
            max_count = t_max_count
            max_word = word
        t_max_count = 0

f1.close()
print(max_word)