import datetime
import card_validator

if __name__ == "__main__":

    card = {
        "exp_date": "04/2021",
        "holder": "Fulano",
        "number": "0000000000000001",
        "cvv": "123",
    }

    card_exp_date = card_validator.validate_card_exp_date(card["exp_date"])
    get_last_day = card_validator.get_last_day(card["exp_date"])
    card_holder = card_validator.validate_card_holder(card["holder"])
    card_number = card_validator.validate_card_number(card["number"])
    cvv_number = card_validator.validate_cvv_number(card["cvv"])
    