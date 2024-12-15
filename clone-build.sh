git clone https://github.com/nlohmann/json.git
git clone https://github.com/rhyme-lang/rhyme.git
git clone https://github.com/tensor-compiler/taco.git
cd taco
mkdir build
cd build
cmake -DCMAKE_BUILD_TYPE=Release ..
make -j8
cd ../..