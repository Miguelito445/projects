from Binary_heap import BinHeap
import random
import time

print("Performance Test")

print("Generating 1,000,000 random numbers...")
test_data = [random.randint(1, 1000000) for _ in range(1000000)]

print("Building min-heap with 1,000,000 elements...")
start_time = time.time()

heap = BinHeap()
heap.build(test_data)

end_time = time.time()
build_time = end_time - start_time

print(f"Build time: {build_time:.4f} seconds")
print(f"Required: < 3 seconds")
print(f"Pass: {build_time < 3}")

print("\nVerifying heap property on first 1000 elements...")
is_valid = True
for i in range(min(1000, len(heap))):
    left = 2*i + 1
    right = 2*i + 2
    
    if left < len(heap) and heap.heap[i] > heap.heap[left]:
        is_valid = False
        print(f"Heap property violated at index {i}")
        break
    
    if right < len(heap) and heap.heap[i] > heap.heap[right]:
        is_valid = False
        print(f"Heap property violated at index {i}")
        break

print(f"Heap property valid: {is_valid}")
print(f"Top element: {heap.top()}")
print(f"Heap size: {len(heap)}")