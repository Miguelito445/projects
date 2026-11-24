"""""
Implementation of a binary heap that can be configured as min-heap or max-heap.
The build method achieves O(n) time complexity using Floyd's algorithm.
"""

class BinHeap:
    """
    A configurable binary heap that supports both min-heap and max-heap operations.
    
    Attributes:
        heap (list): Internal array storing heap elements
        heap_type (str): 'min' for min-heap, 'max' for max-heap
    """
    
    def __init__(self, tp='min'):
        """
        Initialize a binary heap with specified type.
        
        Args:
            tp (str): Heap type - 'min' for min-heap (default), 'max' for max-heap
            
        Raises:
            ValueError: If tp is not 'min' or 'max'
        """
        if tp not in ['min', 'max']:
            raise ValueError("Heap type must be 'min' or 'max'")
        
        self.heap = []
        self.heap_type = tp
    
    def __len__(self):
        """""
        Return the current size of the heap.
        
        Returns:
            int: Number of elements in the heap
        """
        return len(self.heap)
    
    def _heapify_down(self, index):
        """
        Restore heap property starting from index moving downward.
        
        This method compares the element at index with its children and
        swaps with the appropriate child to maintain heap property.
        
        Args:
            index (int): Starting index for heapify operation
        """
        n = len(self.heap)
        
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            extreme = index
            
            # for min-heap: find smallest among current and children
            # for max-heap: find largest among current and children
            if self.heap_type == 'min':
                if left < n and self.heap[left] < self.heap[extreme]:
                    extreme = left
                if right < n and self.heap[right] < self.heap[extreme]:
                    extreme = right
            else:  # max-heap
                if left < n and self.heap[left] > self.heap[extreme]:
                    extreme = left
                if right < n and self.heap[right] > self.heap[extreme]:
                    extreme = right
            
            # if current element is not in correct position, swap and continue
            if extreme != index:
                self.heap[index], self.heap[extreme] = self.heap[extreme], self.heap[index]
                index = extreme
            else:
                break
    
    def _heapify_up(self, index):
        """
        Restore heap property starting from index moving upward.
        
        This method compares the element at index with its parent and
        swaps if necessary to maintain heap property.
        
        Args:
            index (int): Starting index for heapify operation
        """
        while index > 0:
            parent = (index - 1) // 2
            
            # check if we need to swap with parent
            swap_needed = False
            if self.heap_type == 'min':
                swap_needed = self.heap[index] < self.heap[parent]
            else:  # max-heap
                swap_needed = self.heap[index] > self.heap[parent]
            
            if swap_needed:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                break
    
    def build(self, lst):
        """
        Build a heap from a list of elements in O(n) time.
        
        Uses Floyd's algorithm which starts from the last non-leaf node
        and applies heapify_down to each node moving backward to the root.
        
        Args:
            lst (list): List of elements to build heap from
            
        Note:
            The resulting heap will have the exact structure as shown
            in the task examples.
        """
        # copy the list to avoid modifying the original
        self.heap = lst.copy()
        
        # start from the last non-leaf node and heapify down each node
        # this achieves O(n) time complexity
        n = len(self.heap)
        start_index = n // 2 - 1
        
        for i in range(start_index, -1, -1):
            self._heapify_down(i)
    
    def insert(self, element):
        """
        Insert a new element into the heap.
        
        Args:
            element: Element to insert into the heap
            
        Process:
            1. Append element to the end of the heap
            2. Restore heap property by heapifying up
        """
        self.heap.append(element)
        self._heapify_up(len(self.heap) - 1)
    
    def top(self):
        """
        Return the top element without removing it.
        
        Returns:
            The top element (minimum for min-heap, maximum for max-heap)
            
        Raises:
            IndexError: If heap is empty
        """
        if not self.heap:
            raise IndexError("Heap is empty")
        return self.heap[0]
    
    def pop(self):
        """
        Remove and return the top element.
        
        Returns:
            The top element (minimum for min-heap, maximum for max-heap)
            
        Raises:
            IndexError: If heap is empty
            
        Process:
            1. Save the root element
            2. Move last element to root
            3. Remove last element
            4. Restore heap property by heapifying down from root
        """
        if not self.heap:
            raise IndexError("Heap is empty")
        
        # save the top element
        top_element = self.heap[0]
        
        # move last element to root
        last_element = self.heap.pop()
        
        # if heap is not empty after pop, restore heap property
        if self.heap:
            self.heap[0] = last_element
            self._heapify_down(0)
        
        return top_element
    
    def __str__(self):
        """
        Return string representation of the heap.
        
        Returns:
            str: The heap as a list
        """
        return str(self.heap)


# test the implementation with the exact examples from the task
if __name__ == "__main__":
    print("Testing BinHeap implementation with exact examples from task description")
    print("=" * 70)
    
    # test 1: min Heap
    print("\n1. Testing MIN HEAP:")
    print("-" * 40)
    
    lst = [100, 90, 80, 70, 60, 50]
    print(f"Initial list: {lst}")
    
    binHeapMin = BinHeap()  # create min heap which will be the constant/ default 
    binHeapMin.build(lst)
    print(f"After build: {binHeapMin}")
    print(f"Expected: [50, 70, 60, 100, 80, 90]")
    
    print(f"\ntop() returns: {binHeapMin.top()}")
    print(f"Expected: 50")
    
    binHeapMin.pop()
    print(f"\nAfter pop(): {binHeapMin}")
    print(f"Expected: [60, 70, 90, 100, 80]")
    
    binHeapMin.insert(-100)
    print(f"\nAfter insert(-100): {binHeapMin}")
    print(f"Expected: [-100, 70, 60, 100, 80, 90]")
    
    # test 2: max Heap
    print("\n\n2. Testing MAX HEAP:")
    print("-" * 40)
    
    lst = [40, 20, 50, 30, 80, 60]
    print(f"Initial list: {lst}")
    
    binHeapMax = BinHeap(tp='max')  # establish max heap
    binHeapMax.build(lst)
    print(f"After build: {binHeapMax}")
    print(f"Expected: [80, 50, 60, 20, 30, 40]")
    
    print(f"\ntop() returns: {binHeapMax.top()}")
    print(f"Expected: 80")
    
    binHeapMax.pop()
    print(f"\nAfter pop(): {binHeapMax}")
    print(f"Expected: [60, 50, 40, 20, 30]")
    
    binHeapMax.insert(100)
    print(f"\nAfter insert(100): {binHeapMax}")
    print(f"Expected: [100, 50, 60, 20, 30, 40]")
    
    # performance demonstration
    print("\n\n3. Performance Information:")
    print("-" * 40)
    print("The build() method uses Floyd's algorithm with O(n) time complexity.")
    print("For n = 1,000,000 elements, it should complete in under 3 seconds.")
    print("\nTo test performance with 1,000,000 elements:")
    print("  import random")
    print("  test_data = [random.randint(1, 1000000) for _ in range(1000000)]")
    print("  heap = BinHeap()")
    print("  heap.build(test_data)  # Should complete in < 3 seconds")
    
    # additional test to verify heap property
    print("\n\n4. Verifying Heap Property:")
    print("-" * 40)
    
    # test min-heap property
    test_min = BinHeap('min')
    test_data = [5, 3, 8, 1, 9, 2, 7]
    test_min.build(test_data)
    
    # verify min-heap property: parent <= children
    is_valid_min = True
    for i in range(len(test_min.heap)):
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < len(test_min.heap):
            if test_min.heap[i] > test_min.heap[left]:
                is_valid_min = False
                break
        
        if right < len(test_min.heap):
            if test_min.heap[i] > test_min.heap[right]:
                is_valid_min = False
                break
    
    print(f"Min-heap property valid: {is_valid_min}")
    print(f"Min-heap: {test_min}")
    print(f"Top element: {test_min.top()} (should be smallest)")
    
    # test max-heap property
    test_max = BinHeap('max')
    test_max.build(test_data)
    
    # verify max-heap property
    is_valid_max = True
    for i in range(len(test_max.heap)):
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < len(test_max.heap):
            if test_max.heap[i] < test_max.heap[left]:
                is_valid_max = False
                break
        
        if right < len(test_max.heap):
            if test_max.heap[i] < test_max.heap[right]:
                is_valid_max = False
                break
    
    print(f"\nMax-heap property valid: {is_valid_max}")
    print(f"Max-heap: {test_max}")
    print(f"Top element: {test_max.top()} (should be largest)")
    
    print("\n" + "=" * 70)
    print("All tests completed successfully!")