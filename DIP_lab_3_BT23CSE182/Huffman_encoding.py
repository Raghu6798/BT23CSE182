import heapq
from collections import defaultdict, Counter
import json

def huffman(symbols, freqs):
    heap = [[weight, [sym, ""]] for sym, weight in zip(symbols, freqs)]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0]+hi[0]] + lo[1:] + hi[1:])
    
    return dict(sorted(heapq.heappop(heap)[1:], key=lambda x: x[0]))




if __name__=="__main__":
    symbols = ['A','B','C','D','E']
    freqs = [0.35, 0.25, 0.2, 0.15, 0.05]

    huff_codes = huffman(symbols, freqs)
    print("Huffman Codes:", huff_codes)

    with open('huffman_code_output.txt', 'w', encoding='utf-8') as f:
        json.dump({"Huffman Codes": huff_codes}, f, indent=4)

    print("✅ Saved Huffman_code codes to 'Huffman_code_output.txt'")
