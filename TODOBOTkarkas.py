import random
HELP = """
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи.
random - случайная задача"""

RANDOM_TASKS = ["Закибербулили тебя да? Выключи устройство - сделай анжуманя",
"На чиле на раслабоне","Отдыхаешь",
"Оторвись от анжуманя и сделай прес"]


tasks = {

}
#Дата: Сегодня, завтра, 31.12 
#[Задача1, Задача2,Задача3]
#Дата -> [Задача1, Задача2, Задача3]



run = True

def add_todo(date, task):
  if date in tasks:
    tasks[date].append(task)
  else:
    tasks[date] = []
    tasks[date] = [task]
  print("Задача ",task, " добавлена на дату ", date)

while run:
  command = input("Введите команду: ")
  if command == "help":
    print(HELP)
  elif command == "show":
    date = input("Введите дату для изображения задач: ")
    if date in tasks:
      for task in tasks[date]:
        print ("-", task)
    else:
      ("Такой даты нет")
  elif command == "add":
    date = input("Введите дату для добавления задачи: ")
    task = input("Введите название задачи: ")
    add_todo(date, task)
  elif command == "random":
    task = random.choice(RANDOM_TASKS)
    add_todo("Today", task)
  else: 
    print("Неизвестная команда")
    break

print("До свидания!")