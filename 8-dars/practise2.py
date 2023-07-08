numb = list(range(120,1201,2))
summa = sum(numb)
numbers = numb[:]
print(summa)

mini = min(numb)
maxi = max(numb)
overal = maxi - mini

print(overal)
print(len(numb))

begin  = numb[0:19]
mid = numbers[260:280]
end = numbers[521:541]

print("Ro'yxat boshidan 20 son: ", begin, "\n", "Ro'yxat o'rtasidan 20 ta son: ", mid, "\n", "Ro'yxat oxiridan 20 ta son: ", end )

# done
