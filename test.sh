node genvectors.js
TACO_INCLUDE="${PWD}/taco/include"
TACO_LIB="${PWD}/taco/build/lib"
JSON_INCLUDE="${PWD}/json/include"
RHYME_INCLUDE="${PWD}/rhyme/cgen"
g++ -I${TACO_INCLUDE} -L${TACO_LIB}  -std=c++11 taco.cpp -ltaco  -O3 -o taco.out
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:${TACO_LIB}
./taco.out > taco.log
g++ -I${JSON_INCLUDE}  -I${RHYME_INCLUDE}  rhyme.cpp --std=c++17  -O3 -ffast-math  -o rhyme.out
./rhyme.out > rhyme.log

python3 plot.py