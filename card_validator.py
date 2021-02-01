from datetime import datetime,date

# Valida
def validate_card_exp_date(card_exp_date):
    print("Validando data")

    date_now = date.today()
    month, year = card_exp_date.split("/")
    month = int(month)
    year = int(year)
    
    if year < int(date_now.year): 
        exit("Ano expirado")
    if month < 1 or month > 12:
        exit("Mês incorreto")
    if month < int(date_now.month):
        exit("Cartão expirado")


# não estou sabendo conectar as duas funções.
# def get_last_day(card_exp_date):
    
#     if month in (1, 3, 5, 7, 8, 10, 12):
#         last_day = 31
#     elif month == 2:
#         # verifica se é ano bissexto
#         if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
#             last_day = 29
#         else:
#             last_day = 28
#     else:
#         last_day = 30
    
#     print (last_day)

def validate_card_holder(card_holder):
    print("Validando holder")
    if len(card_holder) <2:
        exit("Campo obrigatório")
        
    return card_holder

def validate_card_number(card_number):
    print("Validando número o cartão")

    if len(card_number) != 16:
        exit("Número do cartão precisa ter pelo menos 16 caracteres")
    try:
        int(card_number)
    except TypeError:
        exit("Formato de cartão inválido. Envie números inteiros")

    return card_number

def validate_cvv_number(cvv_number):
    print("Validando cvv number")

    if len(cvv_number) >4 or len(cvv_number) <3:
        exit("Número incorreto")
    try:
        int(cvv_number)
    except TypeError:
        exit("Formato de cartão inválido. Envie apenas números inteiros")

    return cvv_number