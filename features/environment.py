import email_my


def after_feature(context, feature):
    email_my.send_email('sender@mail.ru', 'reciever@mail.ru', '123456', 'smtp.gmail.com', 587)