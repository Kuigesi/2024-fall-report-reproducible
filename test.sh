declare -a sparsity_array
sparsity_array+=(10)
sparsity_array+=(25)
sparsity_array+=(50)
sparsity_array+=(75)

TACO_INCLUDE="${PWD}/taco/include"
TACO_LIB="${PWD}/taco/build/lib"
JSON_INCLUDE="${PWD}/json/include"
RHYME_INCLUDE="${PWD}/rhyme/cgen"
g++ -I${TACO_INCLUDE} -L${TACO_LIB}  -std=c++11 taco.cpp -ltaco  -O3 -o taco.out
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:${TACO_LIB}
g++ -I${JSON_INCLUDE}  -I${RHYME_INCLUDE}  rhyme.cpp --std=c++17  -O3 -ffast-math  -o rhyme.out

for sp in "${!sparsity_array[@]}"; do
  density=${sparsity_array[$sp]}
  node genvectors.js $density
  ./taco.out > "taco_${density}.log"
  ./rhyme.out > "rhyme_${density}.log"
  rm -rf ./*.json ./*.tns
done

python3 plot.py