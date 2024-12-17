const fs = require('node:fs')

const input_sparsity = parseFloat(process.argv[2]);

function sampleDistinctPercentile(percentile, N) {
  if (percentile < 0 || percentile > 1) {
      throw new Error("Percentile must be between 0 and 1.");
  }

  const k = Math.floor(percentile * N); // Calculate the number of elements to sample
  if (k === 0) {
      throw new Error("Percentile too small, resulting in k = 0.");
  }

  const result = new Set();
  while (result.size < k) {
      const randNum = Math.floor(Math.random() * N); // N is excluded
      result.add(randNum);
  }

  return Array.from(result).sort((a, b) => a - b);
  //return result;
}

function randomInteger(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

let ARRAY_LEN = 10000000
let density = input_sparsity / 100

let MAX_NUM = 10000


function createSparseTensor(per, N) {
  //let array = new Array(N).fill(0);
  let idxs = sampleDistinctPercentile(per, N)
  let vals = []
  for (let idx of idxs) {
    //array[idx] = randomInteger(1, MAX_NUM);
    vals.push(randomInteger(1, MAX_NUM))
  }
  return {idxs, vals}
}

function createTns(sparseVec) {
  let idxs = sparseVec.idxs
  let vals = sparseVec.vals
  const zip = (a, b) => a.map((k, i) => [k, b[i]])
  return zip(idxs, vals).map(x => `${x[0] + 1} ${x[1]}`).join("\r\n")
}

function createCSV(sparseVec) {
  let idxs = sparseVec.idxs
  let vals = sparseVec.vals
  let start = 0
  let end = idxs.length
  return {data:vals, cols:idxs, start, end}
}

let B = createSparseTensor(density, ARRAY_LEN)
let B_tns = createTns(B)
fs.writeFileSync('B.tns', B_tns)
fs.writeFileSync('B.json', JSON.stringify(createCSV(B)))
let C = createSparseTensor(density, ARRAY_LEN)
let C_tns = createTns(C)
fs.writeFileSync('C.tns', C_tns)
fs.writeFileSync('C.json', JSON.stringify(createCSV(C)))
let D = createSparseTensor(density, ARRAY_LEN)
let D_tns = createTns(D)
fs.writeFileSync('D.tns', D_tns)
fs.writeFileSync('D.json', JSON.stringify(createCSV(D)))
let E = createSparseTensor(density, ARRAY_LEN)
let E_tns = createTns(E)
fs.writeFileSync('E.tns', E_tns)
fs.writeFileSync('E.json', JSON.stringify(createCSV(E)))