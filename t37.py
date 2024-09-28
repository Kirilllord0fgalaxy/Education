def letters(let):
    if let.lower()=='y':return 'Гласная-согласная'
    return 'Гласная' if let.lower() in ['a','e','i','o','u'] else 'Согласная'

print(letters(input('Буква латинского алфавита:')))
# Красивое!