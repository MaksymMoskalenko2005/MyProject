def currency_converter():
    # Фіксовані курси валют (для прикладу)
    exchange_rates = {
        'USD': {'EUR': 0.92, 'UAH': 41.5, 'GBP': 0.77},
        'EUR': {'USD': 1.07, 'UAH': 44.9, 'GBP': 0.83},
        'UAH': {'USD': 0.024, 'EUR': 0.022, 'GBP': 0.021},
        'GBP': {'USD': 1.28, 'EUR': 1.19, 'UAH': 54.2}
    }
    
    print("Конвертер валют")
    print("Доступні валюти: USD, EUR, UAH, GBP")
    
    while True:
        print("\nМеню:")
        print("1. Конвертувати валюту")
        print("2. Показати курси")
        print("3. Вийти")
        
        choice = input("Виберіть опцію (1-3): ")
        
        if choice == '1':
            from_curr = input("З валюти (напр. USD): ").upper()
            to_curr = input("На валюту (напр. EUR): ").upper()
            amount = float(input("Сума: "))
            
            if from_curr in exchange_rates and to_curr in exchange_rates[from_curr]:
                rate = exchange_rates[from_curr][to_curr]
                converted = amount * rate
                print(f"{amount} {from_curr} = {converted:.2f} {to_curr}")
            else:
                print("Невірний ввід або курс не знайдений!")
        
        elif choice == '2':
            print("\nПоточні курси:")
            for from_curr in exchange_rates:
                print(f"\n{from_curr}:")
                for to_curr, rate in exchange_rates[from_curr].items():
                    print(f"  {to_curr}: {rate}")
        
        elif choice == '3':
            print("Дякую за використання конвертера!")
            break
        
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    currency_converter()