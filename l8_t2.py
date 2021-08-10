# 2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.

# имопрт стандартных модулей для работы с "минимальной кучей" и словаря с поддержкой счетчика
import heapq
from collections import Counter
from collections import namedtuple


# Объявление класса для хранения информации о структуре дерева
class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")


# Объявление класса для "Листьев" дерева
class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"


# Функция кодирования строки в коды Хаффмана
def hufman_encode(s):
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))
    heapq.heapify(h)
    count = len(h)
    while len(h) > 1:
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count2, rigth = heapq.heappop(h)

        heapq.heappush(h, (freq1 + freq2, count, Node(left, rigth)))

        count += 1
    code = {}
    if h:
        [(_freq, _count, root)] = h
        root.walk(code, "")
    return code


# Функция декодирования строки
def huffman_decode(encoded, code):
    sx = []
    enc_ch = ""
    for ch in encoded:
        enc_ch += ch
        for dec_ch in code:
            if code.get(dec_ch) == enc_ch:
                sx.append(dec_ch)
                enc_ch = ""
                break

    return "".join(sx)


s = input()  # ввод данных пользователем
code = hufman_encode(s)
encoded = "".join(code[ch] for ch in s)

print(f'Длина закодоированной строки - {len(code)}, Длина изначальной строки - {len(encoded)}')
print('Закодированные символы и их коды')
for ch in sorted(code):
    print("{}: {}".format(ch, code[ch]))
print(f'Закодированная строка - {encoded}')
print(f'Раскодированная строка - {huffman_decode(encoded, code)}')
