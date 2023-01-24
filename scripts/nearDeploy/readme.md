# File order

1. Get the viewport. Only do this once.

File: **queue_scrape.py**

2. Plan the grid. Only do this once or as needed.

File: Also **queue_scrape.py**

3. Queue the scrapes. Only do this once or when the grid from #2 changes.

File: Also **queue_scrape.py**

4. Activate the scraper. This needs to be scheduled weekly.

File: **monthly_activate_rotation.py**

This requires scheduling using Linux.

5. Activate qualification. This needs to be done weekly, AND occur after step 4 finishes.

File: **weekly_qualification_ritual.py**

Requires scheduling using Linux.

6. Activate deletion of unqualified. Also weekly, after step 5.

Same file as above.