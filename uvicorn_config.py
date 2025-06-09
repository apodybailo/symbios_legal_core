import multiprocessing

workers = max(1, multiprocessing.cpu_count() // 2)
