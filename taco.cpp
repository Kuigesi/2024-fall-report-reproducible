#include <iostream>
#include <chrono>
#include "taco.h"

using namespace  std::chrono;
using namespace taco;

#define ARRAY_LEN  10000000

#define IT_NUM 10

int main(int argc, char* argv[]) {
  Format  scalar;
  Format  sv({Sparse});

  Tensor<int> A(0);

  Tensor<double> B_double = read("B.tns", sv);
  Tensor<double> C_double = read("C.tns", sv);
  Tensor<double> D_double = read("D.tns", sv);
  Tensor<double> E_double = read("E.tns", sv);

  Tensor<int> B("B", {ARRAY_LEN}, sv);
  Tensor<int> C("C", {ARRAY_LEN}, sv);
  Tensor<int> D("D", {ARRAY_LEN}, sv);
  Tensor<int> E("E", {ARRAY_LEN}, sv);

  for (auto m:B_double) {
    B(m.first[0]) = (int)m.second;
  }
  B.pack();
  for (auto m:C_double) {
    C(m.first[0]) = (int)m.second;
  }
  C.pack();
  for (auto m:D_double) {
    D(m.first[0]) = (int)m.second;
  }
  D.pack();
  for (auto m:E_double) {
    E(m.first[0]) = (int)m.second;
  }
  E.pack();

  double total_time = 0.0;
  for (int it = 0; it < IT_NUM; it++) {
    IndexVar i;
    A = B(i) * C(i) * D(i) * E(i);
    A.compile();
    A.assemble();
    auto start = high_resolution_clock::now();
    A.compute();
    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double, std::micro> elapsed = end - start;
    total_time += elapsed.count();
  }

  std::cout << "res: " << A.begin()->second << std::endl;
  std::cout << "Iterations: " << IT_NUM <<  "Time taken : " << total_time << " microseconds" << std::endl;
}
