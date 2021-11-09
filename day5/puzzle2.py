

if __name__ == '__main__':
    source_file = open('input', 'r').readlines()
    # source_file = ['BFFFBBFRRR', 'FFFBBBFRRR', 'BBFFBBFRLL']

    seat_ids = []
    for enc_seat in source_file:
        print(enc_seat.strip(), end=": ")
        bin_row = enc_seat[:7].replace("B", "1").replace("F", "0")
        row = int(bin_row, 2)
        print(row, end=";")
        bin_col = enc_seat[-4:].replace("R", "1").replace("L", "0")
        col = int(bin_col, 2)
        print(col, end=": ")

        seat_id = row * 8 + col
        print(seat_id)
        seat_ids.append(seat_id)

    seat_ids = sorted(seat_ids)
    for seat_index in range(len(seat_ids)):
        seat_id = seat_ids[seat_index]
        if seat_index == 0 or seat_index == len(seat_ids) - 1:
            # Ignore first and last seats
            continue
        pref_seat = seat_ids[seat_index-1]
        next_seat = seat_ids[seat_index+1]
        if next_seat - seat_id != 1 or seat_id - pref_seat != 1:
            print(seat_id)

