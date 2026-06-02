# ========== КОРРЕКТНЫЕ ДАННЫЕ ==========

valid_common_date = {"date": "15.03.1975"}

double_param_date_same_dates = {"date": "15.03.1975", "date": "15.03.1975"}

double_param_date_different_dates = {"date": "15.03.1975", "date": "01.07.1980"}


# ========= НЕКОРРЕКТНЫЕ ДАННЫЕ =========

double_param_date_different_dates_first_valid_second_invalid = {
    "date": "15.03.1975",
    "date": "00.07.1980",
}

date_0_symbols_empty_string = {"date": ""}

date_1_symbol = {"date": "1"}

date_5_symbols = {"date": "15.03"}

date_8_symbols = {"date": "15.03.19"}

date_9_symbols = {"date": "15.03.197"}

date_11_symbols = {"date": "15.03.19751"}

date_12_symbols = {"date": "15.03.197512"}

date_45_symbols = {"date": "5.03.197515.03.197515.03.197515.03.197515.03"}

date_without_dots = {"date": "15031975"}

date_with_only_one_dot = {"date": "15.031975"}

date_with_three_dots = {"date": "15.03.19.75"}

date_with_dots_instead_of_date = {"date": ".........."}

date_with_letters_in_the_beginning = {"date": "фы.03.1975"}

date_with_letters_in_center = {"date": "15.фы.1975"}

date_with_letters_in_the_ending = {"date": "15.03.19фы"}

date_with_letters_instead_of_date = {"date": "фы.ва.прол"}

date_with_specials_in_the_beginning = {"date": "%?.03.1975"}

date_with_specials_in_center = {"date": "15.%?.1975"}

date_with_specials_in_the_ending = {"date": "15.03.19%?"}

date_with_specials_instead_of_date = {"date": "!№.%*.()%?"}

date_with_spaces_in_the_beginning = {"date": "  .03.1975"}

date_with_spaces_in_center = {"date": "15.  .1975"}

date_with_spaces_in_the_ending = {"date": "15.03.19  "}

date_with_spaces_instead_of_date = {"date": "  .  .    "}

date_with_incorrect_type = {"date": True}

request_with_empty_object = {}
