
def write_file_w(path):
    with open(path, 'w', encoding="utf-8") as file:
        file.write(input("Введите текст: "))

def read_file_r(path):
    with open(path,'r', encoding="utf-8") as file:
        return file.read()

def write_file(path, text):
    with open(path, 'w', encoding="utf-8") as file:
        file.write(text)
