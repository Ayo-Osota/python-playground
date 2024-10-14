from translate import Translator

translator = Translator(to_lang="fr")

translation = translator.translate("This is a pen.")

print(translation)

# with open('text.txt', mode="r+") as my_file:
#     text = my_file.write("hey it/'s me")
#     print(my_file.read())

# my_file.close()

try:
    with open('text.txt', mode="r+") as my_file:
        read = my_file.read()
        translation = translator.translate(read)
        print(translation)
        text = my_file.write(translation)
        print(text)
except FileNotFoundError as err:
    print(err)
except IOError as err:
    print(err)
