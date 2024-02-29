def find_msd_lsd(num):
    num_str = str(num)

    msd = int(num_str[0])
    lsd = int(num_str[-1])

    return msd,lsd
input_number = 1010101
msd, lsd = find_msd_lsd(input_number)
print(f"MSD: {msd}")
print(f"LSD: {lsd}")
