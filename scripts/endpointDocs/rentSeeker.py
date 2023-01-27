from translator import translate_to_english

r1 = 'https://8hvk5i2wd9-dsn.algolia.net/1/indexes/rentseeker_prod_properties/query?x-algolia-agent=Algolia%20for%20JavaScript%20(3.33.0)%3B%20Browser&x-algolia-application-id=8HVK5I2WD9&x-algolia-api-key=68a749c1cd4aff1ca2c87a160617bd61'
r1payload = '{"params":"query=&hitsPerPage=1000&page=0&numericFilters=%5B%5B%22type%3D2%22%5D%5D&insideBoundingBox=%5B%5B45.411018479152524%2C-73.66012480493166%2C45.592213534937706%2C-73.47438719506837%5D%5D"}'

r2 = 'https://8hvk5i2wd9-dsn.algolia.net/1/indexes/rentseeker_prod_properties/query?x-algolia-agent=Algolia%20for%20JavaScript%20(3.33.0)%3B%20Browser&x-algolia-application-id=8HVK5I2WD9&x-algolia-api-key=68a749c1cd4aff1ca2c87a160617bd61'
r2payload = '{"params":"query=&hitsPerPage=1000&page=0&numericFilters=%5B%5B%22type%3D2%22%5D%5D&insideBoundingBox=%5B%5B45.45637191330834%2C-73.61369040246583%2C45.54696944019165%2C-73.5208215975342%5D%5D"}'

r3 = 'https://8hvk5i2wd9-dsn.algolia.net/1/indexes/rentseeker_prod_properties/query?x-algolia-agent=Algolia%20for%20JavaScript%20(3.33.0)%3B%20Browser&x-algolia-application-id=8HVK5I2WD9&x-algolia-api-key=68a749c1cd4aff1ca2c87a160617bd61'
r3payload = '{"params":"query=&hitsPerPage=1000&page=0&numericFilters=%5B%5B%22type%3D2%22%5D%5D&insideBoundingBox=%5B%5B45.47903496252904%2C-73.59047320123292%2C45.52433372584454%2C-73.5440387987671%5D%5D"}'

r1t = translate_to_english(r1payload)

r2t = translate_to_english(r2payload)
r3t = translate_to_english(r3payload)
print(r1t)
print(r2t)
print(r3t)
# same story. its a viewport. southwest coords, northeast coords.
