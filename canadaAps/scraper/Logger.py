from simple_chalk import green, yellow, red


def report_progress(*txt):
    return green(txt)


def report_warning(*txt):
    return yellow(txt)


def report_problem(*txt):
    return red(txt)


