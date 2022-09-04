with open('input.txt', 'r') as f:
	 data = f.read().splitlines()


n_len, m_len = data[0].split()
size = data[0].split()
n_len, m_len = int(size[0]), int(size[1])

border = '#'
way = '.'
exit = 'S'

flow = [[(n, m) for m in range(m_len)] for n in range(n_len)]
exit_way = [['#' for m in range(m_len)] for n in range(n_len)]


def find_exit():
    for num, row in enumerate(data[1:]):
        if exit in row:
            return (num, row.index(exit))



exit_coord = find_exit()
exit_way[exit_coord[0]][exit_coord[1]] = exit

for hor_step in range(int(n_len/2)):
    n, m = exit_coord[0], exit_coord[1]
    print(data[1+(n-hor_step)][m])
    if data[1+(n-hor_step)][m] == way:
        
        exit_way[n-hor_step][m] = 'D'
    if data[1+(n+hor_step)][m] == way:
        exit_way[n+hor_step][m] = 'U'
    for vert_step in range(int(m_len/2)):



with open('output.txt', 'w') as outfile:
    outfile.writelines(f'{"".join(s)}\n' for s in exit_way)