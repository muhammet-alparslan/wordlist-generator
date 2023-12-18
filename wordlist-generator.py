    def wordlist_generator():
        print(Fore.YELLOW + "Wordlist Generator Aracına Hoş Geldiniz!" + Style.RESET_ALL)
        print()

        word = input("Türetilmesi için bir kelime girin: ")
        count = int(input("Türetilen kelime sayısını girin: "))

        derivatives = generate_derivatives(word, count)

        if derivatives:
            print(Fore.GREEN + f"{len(derivatives)} Türetilen Kelimeler:")
            for derivative in derivatives:
                print(derivative)
        else:
            print(Fore.RED + "Kelimeler türetilirken hata oluştu.")


    def generate_derivatives(word, count):
        # Dönüşüm fonksiyonlarının listesi
        transformations = [
            capitalize,
            reverse,
            duplicate_vowels,
            remove_vowels,
            append_numbers
        ]

        derivatives = []

        while len(derivatives) < count:
            transformation = random.choice(transformations)
            derivative = transformation(word)
            if derivative != word and derivative not in derivatives:
                derivatives.append(derivative)

        return derivatives


    def capitalize(word):
        return word.capitalize()


    def reverse(word):
        return word[::-1]


    def duplicate_vowels(word):
        vowels = "aeiou"
        result = ""
        for char in word:
            result += char
            if char.lower() in vowels:
                result += char
        return result


    def remove_vowels(word):
        vowels = "aeiou"
        return "".join(char for char in word if char.lower() not in vowels)


    def append_numbers(word):
        numbers = random.sample(range(10), 3)
        return f"{word}{numbers[0]}{numbers[1]}{numbers[2]}"

    # Wordlist oluşturma aracını çalıştırma
    wordlist_generator()