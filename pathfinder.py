from PIL import Image, ImageDraw

# class PathFinder:
def find_way(g, start, t):
    n = len(g)
    INF = 10000000
    d = [INF for i in range(n)]
    p = [0 for i in range(n)]
    d[start] = 0
    u = [False for i in range(n)]
    for i in range(n):
        v = -1
        for j in range(n):
            if u[j] is False and (v == -1 or d[j] < d[v]):
                v = j
        if d[v] == INF:
            break
        u[v] = True
        for j in range(len(g[v])):
            to = g[v][j][0]
            leng = g[v][j][1]
            if d[v] + leng < d[to]:
                d[to] = d[v] + leng
                p[to] = v
    path = []
    v = t
    while v != start:
        path.append(v)
        v = p[v]

    path.append(start)
    path.reverse()
    return path


def draw_line(draw, x1, y1, x2, y2):
    draw.line((x1, y1, x2, y2), fill=(220, 20, 60), width=15)

#===================1=====================================#
enter = 0
enter_promej1 = 1
teatr_prom = 2
teatr_prom_inner = 3
teatr = 4
lestnica1 = 5
enter_promej2 = 6
reg_prom = 7
reg = 8
lect = 9
gard_prom = 10
gard = 11
sanuzel = 12
#===================2=====================================#
lestnica2 = 13
formular = 14
form_right_promej = 15
k207 = 16
k207_right_promej = 17
k208 = 18
k208_right_promej_1 = 19
k208_right_promej_2 = 20
k210_prom = 21
k210 = 22
k212 = 23
k211 = 24
k202 = 25
form_left_promej = 26
form_left_promej_2 = 27
tri_promej = 28
k205 = 29
tri_promej_down = 30
k203 = 31
k203_prom1 = 32
k203_prom2 = 33
k203a = 34
museum = 35


coords = [[0] for i in range(36)]
coords[lestnica1] = [970, 200]
coords[enter] = [1045, 580]
coords[enter_promej1] = [1045, 525]
coords[enter_promej2] = [890, 525]
coords[teatr_prom] = [1045, 300]
coords[teatr_prom_inner] = [1300, 300]
coords[teatr] = [1300, 150]
coords[sanuzel] = [625, 180]
coords[lect] = [620, 525]
coords[reg_prom] = [890, 350]
coords[reg] = [750, 350]
coords[gard_prom] = [620, 340]
coords[gard] = [545, 340]

coords[lestnica2] = [3100, 600]
coords[formular] = [3100, 640]
coords[form_right_promej] = [3500, 640]
coords[k207] = [3750, 720]
coords[k207_right_promej] = [3750, 640]
coords[k208] = [4225, 720]
coords[k208_right_promej_1] = [4225, 640]
coords[k208_right_promej_2] = [4670, 640]
coords[k210_prom] = [4970, 640]
coords[k211] = [5100, 640]
coords[k210] = [4970, 720]
coords[k212] = [4970, 580]
coords[k202] = [2870, 800]
coords[form_left_promej] = [2650, 750]
coords[form_left_promej_2] = [2225, 750]
coords[tri_promej] = [2115, 750]
coords[tri_promej_down] = [2115, 820]
coords[k205] = [2115, 685]
coords[k203] = [2025, 820]
coords[k203_prom1] = [1700, 820]
coords[k203_prom2] = [1700, 650]
coords[k203a] = [1750, 650]
coords[museum] = [750, 800]

floor_rooms = [(13, coords[lestnica1],), (23, coords[lestnica2],)] #формат - (кол-во комнат, координаты лестницы)
g = [
    [(enter, 0,), (enter_promej1, 1,)],  # enter, 0
    [(enter, 1,), (enter_promej1, 0,), (enter_promej2, 1,), (teatr_prom, 1,)],  # enter_prom1, 1
    [(enter_promej1, 1,), (teatr_prom, 0,), (teatr_prom_inner, 1,), (lestnica1, 1,)],  # teatr_prom, 2
    [(teatr_prom, 1,), (teatr_prom_inner, 0,), (teatr, 1,)],  # teatr_prom_inner, 3
    [(teatr_prom_inner, 1,), (teatr, 0,)],  # teatr, 4
    [(teatr_prom, 1,), (lestnica1, 0,), (reg_prom, 1,), (lestnica2, 1)],  # lestnica1, 5
    [(enter_promej1, 1,), (enter_promej2, 0,), (reg_prom, 1,), (lect, 1,)],  # enter_prom2, 6
    [(enter_promej2, 1,), (reg_prom, 0,), (reg, 1,), (lestnica1, 1)],  # reg_prom7
    [(reg_prom, 1,), (reg, 0,)],  # reg, 8
    [(enter_promej2, 1,), (lect, 0,), (gard_prom, 1)],  # lect, 9
    [(lect, 1,), (gard_prom, 0,), (gard, 1,), (sanuzel, 1)],  # gard_prom, 10
    [(gard_prom, 1,), (gard, 0,)],  # gard, 11
    [(gard_prom, 1,), (sanuzel, 0)],  # sanuzel, 12
    #########################################################################
    [(lestnica2, 0,), (formular, 1,), (lestnica1, 1)], #lestnica, 13
    [(lestnica2, 1,), (formular, 0,), (form_right_promej, 1,), (form_left_promej, 1,)], #formular, 14
    [(formular, 1,), (form_right_promej, 0,), (k207_right_promej, 1,)], #form_right, 15
    [(k207, 0,), (k207_right_promej, 1,)], #k207, 16
    [(k207, 1,), (k207_right_promej, 0,), (k208_right_promej_1, 1,)], #k207_right, 17
    [(k208, 0,), (k208_right_promej_1, 1,)], #k208, 18
    [(k208, 1,), (k208_right_promej_1, 0,), (k208_right_promej_2, 1,)], #k208_right1, 19
    [(k208_right_promej_1, 1,), (k208_right_promej_2, 0,), (k210_prom, 1,)], #k208_right2, 20
    [(k208_right_promej_2, 1,), (k210_prom, 0,), (k210, 1,), (k211, 1,), (k212, 1,)], #k210_prom, 21
    [(k210_prom, 1,), (k210, 0,)], #k210, 22
    [(k210_prom, 1,), (k211, 0,)], #k211, 23
    [(k210_prom, 1,), (k212, 0,)], #k212, 24
    [(formular, 1,), (k202, 0,)], #k202, 125
    [(formular, 1,), (form_left_promej, 0,), (form_left_promej_2, 1,)], #form_left,26
    [(form_left_promej, 1,), (form_left_promej_2, 0,), (tri_promej, 1,)], #form_left2, 27
    [(form_left_promej_2, 1), (tri_promej, 0,), (k205, 1,), (tri_promej_down, 1,)], #tripromej, 28
    [(tri_promej, 1,), (k205, 0,)], #k205, 29
    [(tri_promej, 1), (tri_promej_down, 0), (k203, 1,)], #tripromleft, 30
    [(tri_promej_down, 1,), (k203, 0,), (k203_prom1, 1,)], #k203, 31
    [(k203, 1,), (k203_prom1, 0,), (k203_prom2, 1,), (museum, 1)], #k203_prom1, 32
    [(k203_prom1, 1,), (k203_prom2, 0,), (k203a, 1)], #k203_prom2, 33
    [(k203_prom2, 1), (k203a, 0)], #k203a, 34
    [(k203_prom1, 1), (museum, 0)], #museum, 35
]

start = 0
end = k202
way = find_way(g, start, end)
print(way)

if end <= 13:
    image = Image.open('assets/floors/1.png')
    draw = ImageDraw.Draw(image)
    x, y = coords[way[0]]
    for w in way[1:]:
        draw_line(draw, x, y, coords[w][0], coords[w][1])
        x, y = coords[w]
    image.show()
elif end <= 35:
    image2 = Image.open('assets/floors/2.png')
    image1 = Image.open('assets/floors/1.png')
    draw1 = ImageDraw.Draw(image1)
    draw2 = ImageDraw.Draw(image2)
    x, y = coords[way[0]]
    idx = 0
    for w in way[1:]:
        idx += 1
        draw_line(draw1, x, y, coords[w][0], coords[w][1])
        x, y = coords[w]
        if [x, y] == coords[lestnica1]:
            break
    x, y = coords[way[idx + 1]]
    for w in way[idx+1:]:
        draw_line(draw2, x, y, coords[w][0], coords[w][1])
        x, y = coords[w]
    image1.show()
    image2.show()


'''x, y = coords[way[0]]
for w in way[1:]:
    for i in range(1,len(floor_rooms)):
        if coords.index([x, y]) < floor_rooms[i][0]:
            image = Image.open(str(i) + 'floor.png') #стандартное название плана - 1floor, 2floor..., потом можно будет добавить возможность его менять
            draw = ImageDraw.Draw(image)
            for j in range(len(way[:way.index(floor_rooms[i][0])])):
                draw_line(draw, x, y, coords[w][0], coords[w][1])
                x, y = coords[w]
            image.show()'''
