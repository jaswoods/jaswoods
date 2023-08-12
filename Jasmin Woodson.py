notes = []
for i in range(5):
    note = float(input(f"tape nòt ou yo pou ekzamen yo {i+1} : "))
    notes.append(note)

moyenne = sum(notes) / len(notes)

print(f"Notes ou yo se : {notes}")
print(f"Moyenne nan se : {moyenne:.2f}")

if moyenne >= 90:
    lettre = "A"
elif moyenne >= 80:
    lettre = "B"
elif moyenne >= 70:
    lettre = "C"
elif moyenne >= 60:
    lettre = "D"
else:
    lettre = "F"

print(f"Moyenne nan correspond a lettre : {lettre}")
