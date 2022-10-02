"""
Напишите программу печатающую бейджики учеников.
Программа запрашивает ввод числа учеников и печатает каждому бейджик. Бейдж содержит название учебного заведения:
«Колледж Сириус», поле для имени:
«Имя: ____» и поле для школы:
«Группа: ____». Напиши программу, печатающую бейджики студентов как на картинке. В завершении программа должна печатать:
«Готово! Заберите бейджики.»
Функция должна принимать имя и группу ученика.
"""
new_cards_data = []
que = int(input())

def control_group(id_group):
    print("Group", id_group)

def control_que():
    for students in range(que):
        new_cards_data.append(input())
    return new_cards_data

def control_output():
    control_que()
    print("College Sirius(*)")
    id = int(input('Which group? -- '))
    control_group(id)
    for studs in new_cards_data:
        print("Name:", studs)
    print('Take your base --*--')

def main():
    control_output()


if __name__ == "__main__":
    main()
