const fs = require('fs')

const raw = fs.readFileSync('./stolenData/moreData00.json')
const housing = JSON.parse(raw)
const hits = housing.hits

const locs = []
for (let i = 0; i < hits.length; i++) {
    locs.push(hits[i]._geoloc)
}

const data = JSON.stringify(locs)
fs.writeFileSync('housing2.json', data)
