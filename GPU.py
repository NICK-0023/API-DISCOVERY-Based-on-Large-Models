import torch

if torch.cuda.is_available():
    # 显示 GPU 设备数量
    num_gpus = torch.cuda.device_count()
    print(f"Number of GPUs available: {num_gpus}")

    # 输出每个 GPU 的显存总量和已用显存
    for i in range(num_gpus):
        total_memory = torch.cuda.get_device_properties(i).total_memory  # 总显存
        allocated_memory = torch.cuda.memory_allocated(i)  # 已分配显存
        cached_memory = torch.cuda.memory_reserved(i)  # 保留显存（通常会在 CUDA 内存池中）

        print(f"GPU {i}:")
        print(f"  Total Memory: {total_memory / (1024 ** 3):.2f} GB")
        print(f"  Allocated Memory: {allocated_memory / (1024 ** 3):.2f} GB")
        print(f"  Cached Memory: {cached_memory / (1024 ** 3):.2f} GB")
else:
    print("No CUDA-capable GPU available.")
