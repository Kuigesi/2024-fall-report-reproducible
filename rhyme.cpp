#include <chrono>
#include "rhyme.hpp"

using namespace  std::chrono;

#define IT_NUM 10

int main() {
    CSVector<int, int> B = read_1D_sparse_tensor<int, int>("B.json");
    CSVector<int, int> C = read_1D_sparse_tensor<int, int>("C.json");
    CSVector<int, int> D = read_1D_sparse_tensor<int, int>("D.json");
    CSVector<int, int> E = read_1D_sparse_tensor<int, int>("E.json");

    int tmp0 = 0;
    double total_time = 0.0;
    for (int it = 0; it < IT_NUM; it++) {

      auto start = high_resolution_clock::now();
      tmp0 = 0;
      for (auto xi_mit = CSVector<int, int>::multi_iterator({&B,&C,&D,&E});!xi_mit.finish(); ++xi_mit) {
          tmp0 += (int)(((((*xi_mit).second[0] * (*xi_mit).second[1]) * (*xi_mit).second[2]) * (*xi_mit).second[3]));
      }
      auto end = std::chrono::high_resolution_clock::now();
      std::chrono::duration<double, std::micro> elapsed = end - start;
      total_time += elapsed.count();
    }
    int res = tmp0;
    //write_result(res);

    std::cout << "res: " << res << std::endl;
    std::cout << "Iterations: " << IT_NUM <<  " Time taken : " << (long)total_time << " microseconds" << std::endl;
}