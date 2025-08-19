import json

def shannon_fano(symbols, freqs):
    if len(symbols) == 1:
        return {symbols[0]: ""}
    
    # Sort symbols by frequency descending
    paired = sorted(zip(symbols, freqs), key=lambda x: x[1], reverse=True)
    symbols, freqs = zip(*paired)
    
    # Find split point
    total = sum(freqs)
    acc = 0
    split = 0
    for i, f in enumerate(freqs):
        acc += f
        if acc >= total/2:
            split = i + 1
            break
    
    left = shannon_fano(symbols[:split], freqs[:split])
    right = shannon_fano(symbols[split:], freqs[split:])
    
    # Add prefix
    for k in left: left[k] = '0' + left[k]
    for k in right: right[k] = '1' + right[k]
    
    left.update(right)
    return left

if __name__=="__main__":
    symbols = ['A','B','C','D','E']
    freqs = [0.35, 0.25, 0.2, 0.15, 0.05]

    sf_codes = shannon_fano(symbols, freqs)
    print("Shannon-Fano Codes:", sf_codes)

    # Save as JSON-wrapped dictionary in a .txt file
    with open('shannon_code_output.txt', 'w', encoding='utf-8') as f:
        json.dump({"Shannon-Fano Codes": sf_codes}, f, indent=4)

    print("✅ Saved Shannon-Fano codes to 'shannon_code_output.txt'")
