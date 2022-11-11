#include <iostream>
#include "threadpool.hpp"

ThreadPool TP(8);

int main() {
	auto square = [](const uint64_t x) {
		return x * x;
	};

	const uint64_t num_nodes = 12;
	std::vector<std::future<uint64_t>> futures;

	typedef std::function<void(uint64_t)> traverse_t;
	traverse_t traverse = [&] (uint64_t node) {
		if (node < num_nodes) {
			auto future = TP.enqueue(square, node);
			futures.emplace_back(std::move(future));
		}
		
		traverse(2*node+1);
		traverse(2*node+2);
	};

	traverse(0);

	for (auto& future : futures)
		std::cout << future.get() << '\n';

	return 0;
}