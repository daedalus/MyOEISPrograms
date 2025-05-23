def a(n):
    if n <= 2: return 1
    c = 0
    p2 = 1 << n
    n2 = n << 1
    full_mask = p2 - 1
    high_bit = 1 << (n - 1)
    max_sum_bit = 1 << n2  # large enough for sums

    # Precompute numbers by parity index, 1-based indexing:
    even_nums = [i for i in range(2, n + 1, 2)]
    odd_nums = [i for i in range(1, n + 1, 2)]

    # Convert parity subsets to bitmasks for quick access
    even_len = len(even_nums)
    odd_len = len(odd_nums)

    # Function to get sum bits for a parity subset bitmask:
    def sum_bits(nums, bitmask):
        sums = 0
        subset = [nums[i] for i in range(len(nums)) if (bitmask & (1 << i))]
        # sums of pairs (including pairs of the same element)
        for i in range(len(subset)):
            a = subset[i]
            for j in range(i, len(subset)):
                s = a + subset[j]
                if s > n2: break
                # Set bit (s // 2 - 1)
                sums |= 1 << ((s >> 1) - 1)
        return sums

    for subset_mask in range(high_bit + 1, p2, 2):
        if (subset_mask & high_bit) == 0: continue
        # Extract parity subsets bitmasks from subset_mask:
        even_mask = 0
        odd_mask = 0
        for bit in range(n):
            if subset_mask & (1 << bit):
                x = bit + 1
                x2 = x >> 1
                if x & 1:
                    # odd index in odd_nums is at position (x//2)
                    # odd_nums are at indices 0,1,... with values 1,3,5,...
                    odd_mask |= 1 << x2
                else:
                    # even index in even_nums at position (x//2 - 1)
                    even_mask |= 1 << (x2 - 1)
        m = 0
        if odd_mask:
            m |= sum_bits(odd_nums, odd_mask)
        if even_mask:
            m |= sum_bits(even_nums, even_mask)
        if m == full_mask:
            c += 1
    return c
