S = "MLMMLLM" 
K = 3

split_S = S.split('L')

counts_m = list(map(lambda x: x.count("M"), S.split('L')))
counts_l = list(map(lambda x: x.count("L"), S.split('M')))
max_val = max(counts_m)

