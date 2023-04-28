#Нужно создать класс который принимет модель ноутбука(Acer, Asus, ...)
# и возвращает полную комплектацию ноутбука со всеми характеристиками.
class NoteBook:
    def __init__(self, processor, memory, video_card, hard_disc, mother_plata, screen_size):
        self.processor = processor
        self.memory = memory
        self.video_card = video_card
        self.hard_disc = hard_disc
        self.mother_plata = mother_plata
        self.screen_size = screen_size
    def get_keys_hard_disc(self):
        return list(self.hard_disc.keys())

    def get_values_processor(self):
        return tuple(self.processor.values())

    def get_keys_memory(self):
        print(set(self.memory.keys()))


    def build(self):
        print(f'процессор - {str(self.processor)}\n оперативная память - {str(self.memory)}\n видео карта - {str(self.video_card)} \n жесткий диск - {str(self.hard_disc)}\n материнская плата - {str(self.mother_plata)} \n размер экрана - {str(self.screen_size)}')


Acer = NoteBook(processor=55, memory=77, video_card=12, hard_disc=8, mother_plata=12.6, screen_size=45)
Asus = NoteBook(50, 70, 12, 10, 12.11, 29)

# print(Acer.mother_plata)
# print("Acer", Acer.build())
print(Asus.get_keys_memory())



#Нужно создать класс который принимает данные в формате dict.
# Эти данные, вы сможете взять из Data #1.
#Вам нужно создать 6 методов класса:
# Получить все ключи в TUPLE.
# Получить все значения в TUPLE.
# Получить все ключи в LIST.
# Получить все значения в LIST.
# Получить все ключи в SET.
# Получить все значения в SET.
#
# Ниже когда вы будете передавать Словарь классу он и вызывать из него любой метод Вы должны получать соответственно нужные типы данных.
# Example: my_class = Parser("DICT") | my_class.get_keys_tuple()