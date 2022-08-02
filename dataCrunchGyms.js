const fs = require('fs')

const raw = fs.readFileSync('./stolenData/mtlGyms.json')
const housing = JSON.parse(raw)
const hits = housing.results

const locs = []
for (let i = 0; i < hits.length; i++) {
    locs.push(hits[i].geometry.location)
}

const data = JSON.stringify(locs)
fs.writeFileSync('mtlGyms2.json', data)
