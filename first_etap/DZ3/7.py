# Напишите программу, где исходный список содержит положительные и отрицательные числа.
# Требуется положительные поместить в один список, а отрицательные - в другой.

def pos_neg(numbers):
    positive = []
    negative = []
    for i in numbers:
        if i >= 0:
            positive.append(i)
        else:
            negative.append(i)

            return positive, negative

numbers = [1, 4, 6, 2.3, -3, -5, -92]

print(pos_neg(numbers))
