def generate_pascals_triangle(num_rows):
    triangle = []
    for row_num in range(num_rows):
        # Each row starts and ends with 1
        row = [1]
        if triangle:
            # Compute middle elements based on previous row
            last_row = triangle[-1]
            row.extend([last_row[i] + last_row[i+1] for i in range(len(last_row)-1)])
            row.append(1)
        triangle.append(row)
    return triangle

def print_pascals_triangle(triangle):
    max_width = len(' '.join(map(str, triangle[-1])))
    for row in triangle:
        row_str = ' '.join(map(str, row)).center(max_width)
        print(row_str)

num_rows = int(input("Enter the number of rows for Pascal's triangle: "))
triangle = generate_pascals_triangle(num_rows)
print_pascals_triangle(triangle)
