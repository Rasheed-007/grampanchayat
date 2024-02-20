# def charEncrypt(character, key):
#
#     alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
#
#
#     if character.isupper():
#
#         char_index = alphabet_upper.find(character)
#         encrypted_index = (char_index + key) % 26
#         encrypted_char = alphabet_upper[encrypted_index]
#     elif character.islower():
#
#         char_index = alphabet_lower.find(character)
#         encrypted_index = (char_index + key) % 26
#         encrypted_char = alphabet_lower[encrypted_index]
#     else:
#
#         encrypted_char = character
#
#     return encrypted_char
#
# def main():
#
#     character = str(input().strip())
#
#
#     key = int(input().strip())
#
#
#     result = charEncrypt(character, key)
#
#
#     print(result)
#
#
# if __name__ == "__main__":
#     main()


def calculate_discounted_products(order_size, order, dis_amount):
    discounted_products = 0

    for i in range(order_size):
        if order[i] > 0 and dis_amount % abs(order[i]) == 0:
            discounted_products += 1

    return discounted_products
def main():
    order_size = int(input().strip())
    order = list(map(int, input().strip().split()))
    dis_amount = int(input().strip())
    result = calculate_discounted_products(order_size, order, dis_amount)
    print(result)

if __name__ == "__main__":
    main()
