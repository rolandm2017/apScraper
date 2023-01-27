open_bracket = "%7B"
close_bracket = "%7D"
quotation_mark = "%22"


def translate_to_english(start):
    print("translating")
    translated = start.replace(open_bracket, "{").replace(close_bracket, "}").replace(quotation_mark, '"')
    translated = translated.replace("%5B", "[").replace("%5D", "]").replace("%22", '"').replace("%3D", "=").replace("%2C", ",")
    return translated
