# alert('Hello world')  # скрипт  JS вызовет алерт
# confirm('Do U understand?')  # скрипт JS вызовет конфирм окно
# prompt('Enter something')  # скрипт JS вернет окно с полем ввода

alert = browser.switch_to.alert  # переключиться на окно с алертом
alert_text = alert.text  # получить текст из алерта
alert.accept()  # подтвердить алерт

confirm = browser.switch_to.alert  # переключиться и на окно с конфирмом
confirm.accept()  # принять
confirm.dismiss()  # отклонить

prompt = browser.switch_to.alert
prompt.send_keys('some')  # отправить в промпт текст
prompt.accept()

