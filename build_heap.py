# python3


def heapify(arr, n, i, swaps):

    smallest = i 	
    left = 2*i + 1
    right = 2*i + 2
    
 
    if left < n and arr[left] < arr[smallest]:
        smallest = left
        
   
    if right < n and arr[right] < arr[smallest]:
        smallest = right
    

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]  
        swaps.append((i, smallest))  
        heapify(arr, n, smallest, swaps)  

def build_heap(arr):

    n = len(arr)
    swaps = []

    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i, swaps)
    
    return swaps

def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    letter = input().strip()
    if letter == 'I':
        n = int(input().strip())
        data = list(map(int, input().split()))

        assert len(data) == n

    elif letter == 'F':
        file_name = input()
        with open(file_name, "r") as f:
            n = int(f.readline())
            data = list(map(int, f.readline().split()))  
            
            assert len(data) == n
    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))
    print(len(swaps))
    assert len(swaps) <= 4 * n
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
