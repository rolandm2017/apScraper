from time import sleep
from celery import current_app


@current_app.task(name="delayed_math")
def delayed_math(x):
    sleep(x / 10)
    return x + 100


MAX_RETRIES = 5
END_OF_LOOP = MAX_RETRIES - 1


@current_app.task(name="scrape_stuff")
def scrape_stuff(scraper, task):
    for index in range(0, MAX_RETRIES):
        scrape = scraper.scrape(task)
        scrape_was_successful = len(scrape) > 0
        if scrape_was_successful:
            scraper.report_apartments_and_mark_complete(task, scrape)
            break
        else:
            # todo: determine type of failure. "is banned?" "429?"
            scraper.add_failure_to_logs(scrape)
            if index is END_OF_LOOP:
                scraper.report_failure_for(task)
                scraper.reset_logs()
