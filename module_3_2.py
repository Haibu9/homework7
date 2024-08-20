
def check(email):
    q = False
    for i in email:
        if i == "@":
            if email[-4:] == '.com' or email[-4:] == '.net' or email[-3:] == '.ru':
                q = True
                break
    return q


def send_email(message, recipient, *, sender = "university.help@gmail.com"):
    y = False
    z = False
    x = check(recipient)
    n = check(sender)

    if sender == recipient:
        y = True

    if sender == "university.help@gmail.com":
        z = True

    if x == 0 or n == 0:
        print("Невозможно отправить письмо с адреса ", sender, "на адрес ",recipient)

    elif y == 1:
        print("Нельзя отправить письмо самому себе!")

    elif z == 1:
        print("Письмо успешно отправлено с адреса ", sender," на адрес ", recipient, ".")

    else:
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса ", sender," на адрес ", recipient, ".")

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')