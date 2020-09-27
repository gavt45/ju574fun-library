# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw


class BestPathFinder:
    def __init__(self):
        # self.image1 = Image.open('assets/floors/1.png')
        # self.image2 = Image.open('assets/floors/2.png')
        self.akindofdb = {}

        # ===================1=====================================#
        self.enter = 0
        self.enter_promej1 = 1
        self.teatr_prom = 2
        self.teatr_prom_inner = 3
        self.teatr = 4
        self.lestnica1 = 5
        self.enter_promej2 = 6
        self.reg_prom = 7
        self.reg = 8
        self.lect = 9
        self.gard_prom = 10
        self.gard = 11
        self.sanuzel = 12
        # ===================2=====================================#
        self.lestnica2 = 13
        self.formular = 14
        self.form_right_promej = 15
        self.k207 = 16
        self.akindofdb[207] = self.k207
        self.k207_right_promej = 17
        self.k208 = 18
        self.akindofdb[208] = self.k208
        self.k208_right_promej_1 = 19
        self.k208_right_promej_2 = 20
        self.k210_prom = 21
        self.k210 = 22
        self.akindofdb[210] = self.k210
        self.k212 = 23
        self.akindofdb[212] = self.k212
        self.k211 = 24
        self.akindofdb[211] = self.k211
        self.k202 = 25
        self.akindofdb[202] = self.k202
        self.form_left_promej = 26
        self.form_left_promej_2 = 27
        self.tri_promej = 28
        self.k205 = 29
        self.akindofdb[205] = self.k205
        self.tri_promej_down = 30
        self.k203 = 31
        self.akindofdb[203] = self.k203
        self.k203_prom1 = 32
        self.k203_prom2 = 33
        self.k203a = 34
        self.museum = 35

        self.coords = [[0] for i in range(36)]
        self.coords[self.lestnica1] = [970, 200, 1]
        self.coords[self.enter] = [1045, 580, 1]
        self.coords[self.enter_promej1] = [1045, 525, 1]
        self.coords[self.enter_promej2] = [890, 525, 1]
        self.coords[self.teatr_prom] = [1045, 300, 1]
        self.coords[self.teatr_prom_inner] = [1300, 300, 1]
        self.coords[self.teatr] = [1300, 150, 1]
        self.coords[self.sanuzel] = [625, 180, 1]
        self.coords[self.lect] = [620, 525, 1]
        self.coords[self.reg_prom] = [890, 350, 1]
        self.coords[self.reg] = [750, 350, 1]
        self.coords[self.gard_prom] = [620, 340, 1]
        self.coords[self.gard] = [545, 340, 1]

        self.coords[self.lestnica2] = [3100, 600, 2]
        self.coords[self.formular] = [3100, 640, 2]
        self.coords[self.form_right_promej] = [3500, 640, 2]
        self.coords[self.k207] = [3750, 720, 2]
        self.coords[self.k207_right_promej] = [3750, 640, 2]
        self.coords[self.k208] = [4225, 720, 2]
        self.coords[self.k208_right_promej_1] = [4225, 640, 2]
        self.coords[self.k208_right_promej_2] = [4670, 640, 2]
        self.coords[self.k210_prom] = [4970, 640, 2]
        self.coords[self.k211] = [5100, 640, 2]
        self.coords[self.k210] = [4970, 720, 2]
        self.coords[self.k212] = [4970, 580, 2]
        self.coords[self.k202] = [2870, 800, 2]
        self.coords[self.form_left_promej] = [2650, 750, 2]
        self.coords[self.form_left_promej_2] = [2225, 750, 2]
        self.coords[self.tri_promej] = [2115, 750, 2]
        self.coords[self.tri_promej_down] = [2115, 820, 2]
        self.coords[self.k205] = [2115, 685, 2]
        self.coords[self.k203] = [2025, 820, 2]
        self.coords[self.k203_prom1] = [1700, 820, 2]
        self.coords[self.k203_prom2] = [1700, 650, 2]
        self.coords[self.k203a] = [1750, 650, 2]
        self.coords[self.museum] = [750, 800, 2]

        self.floor_rooms = [(13, self.coords[self.lestnica1],),
                            (23, self.coords[self.lestnica2],)]  # формат - (кол-во комнат, координаты лестницы)
        # self.g = [
        #     [(self.enter, 0,), (self.enter_promej1, 1,)],  # enter, 0
        #     [(self.enter, 1,), (self.enter_promej1, 0,), (self.enter_promej2, 1,), (self.teatr_prom, 1,)],  # enter_prom1, 1
        #     [(self.enter_promej1, 1,), (self.teatr_prom, 0,), (self.teatr_prom_inner, 1,), (self.lestnica1, 1,)],  # teatr_prom, 2
        #     [(self.teatr_prom, 1,), (self.teatr_prom_inner, 0,), (self.teatr, 1,)],  # teatr_prom_inner, 3
        #     [(self.teatr_prom_inner, 1,), (self.teatr, 0,)],  # teatr, 4
        #     [(self.teatr_prom, 1,), (self.lestnica1, 0,), (self.reg_prom, 1,), (self.lestnica2, 1)],  # lestnica1, 5
        #     [(self.enter_promej1, 1,), (self.enter_promej2, 0,), (self.reg_prom, 1,), (self.lect, 1,)],  # enter_prom2, 6
        #     [(self.enter_promej2, 1,), (self.reg_prom, 0,), (self.reg, 1,), (self.lestnica1, 1)],  # reg_prom7
        #     [(self.reg_prom, 1,), (self.reg, 0,)],  # reg, 8
        #     [(self.enter_promej2, 1,), (self.lect, 0,), (self.gard_prom, 1)],  # lect, 9
        #     [(self.lect, 1,), (self.gard_prom, 0,), (self.gard, 1,), (self.sanuzel, 1)],  # gard_prom, 10
        #     [(self.gard_prom, 1,), (self.gard, 0,)],  # gard, 11
        #     [(self.gard_prom, 1,), (self.sanuzel, 0)],  # sanuzel, 12
        #     #########################################################################
        #     [(self.lestnica2, 0,), (self.formular, 1,), (self.lestnica1, 1)],  # lestnica, 13
        #     [(self.lestnica2, 1,), (self.formular, 0,), (self.form_right_promej, 1,), (self.form_left_promej, 1,)],  # formular, 14
        #     [(self.formular, 1,), (self.form_right_promej, 0,), (self.k207_right_promej, 1,)],  # form_right, 15
        #     [(self.k207, 0,), (self.k207_right_promej, 1,)],  # k207, 16
        #     [(self.k207, 1,), (self.k207_right_promej, 0,), (self.k208_right_promej_1, 1,)],  # k207_right, 17
        #     [(self.k208, 0,), (self.k208_right_promej_1, 1,)],  # k208, 18
        #     [(self.k208, 1,), (self.k208_right_promej_1, 0,), (self.k208_right_promej_2, 1,)],  # k208_right1, 19
        #     [(self.k208_right_promej_1, 1,), (self.k208_right_promej_2, 0,), (self.k210_prom, 1,)],  # k208_right2, 20
        #     [(self.k208_right_promej_2, 1,), (self.k210_prom, 0,), (self.k210, 1,), (self.k211, 1,), (self.k212, 1,)],  # k210_prom, 21
        #     [(self.k210_prom, 1,), (self.k210, 0,)],  # k210, 22
        #     [(self.k210_prom, 1,), (self.k211, 0,)],  # k211, 23
        #     [(self.k210_prom, 1,), (self.k212, 0,)],  # k212, 24
        #     [(self.formular, 1,), (self.k202, 0,)],  # k202, 125
        #     [(self.formular, 1,), (self.form_left_promej, 0,), (self.form_left_promej_2, 1,)],  # form_left,26
        #     [(self.form_left_promej, 1,), (self.form_left_promej_2, 0,), (self.tri_promej, 1,)],  # form_left2, 27
        #     [(self.form_left_promej_2, 1), (self.tri_promej, 0,), (self.k205, 1,), (self.tri_promej_down, 1,)],  # tripromej, 28
        #     [(self.tri_promej, 1,), (self.k205, 0,)],  # k205, 29
        #     [(self.tri_promej, 1), (self.tri_promej_down, 0), (self.k203, 1,)],  # tripromleft, 30
        #     [(self.tri_promej_down, 1,), (self.k203, 0,), (self.k203_prom1, 1,)],  # k203, 31
        #     [(self.k203, 1,), (self.k203_prom1, 0,), (self.k203_prom2, 1,), (self.museum, 1)],  # k203_prom1, 32
        #     [(self.k203_prom1, 1,), (self.k203_prom2, 0,), (self.k203a, 1)],  # k203_prom2, 33
        #     [(self.k203_prom2, 1), (self.k203a, 0)],  # k203a, 34
        #     [(self.k203_prom1, 1), (self.museum, 0)],  # museum, 35
        # ]

        self.g = [
            [(self.enter, 0,), (self.enter_promej1, 1,)],  # enter, 0
            [(self.enter, 1,), (self.enter_promej1, 0,), (self.enter_promej2, 1,), (self.teatr_prom, 1,)],
            # enter_prom1, 1
            [(self.enter_promej1, 1,), (self.teatr_prom, 0,), (self.teatr_prom_inner, 1,), (self.lestnica1, 1,)],
            # teatr_prom, 2
            [(self.teatr_prom, 1,), (self.teatr_prom_inner, 0,), (self.teatr, 1,)],  # teatr_prom_inner, 3
            [(self.teatr_prom_inner, 1,), (self.teatr, 0,)],  # teatr, 4
            [(self.teatr_prom, 1,), (self.lestnica1, 0,), (self.reg_prom, 1,), (self.lestnica2, 1)],  # lestnica1, 5
            [(self.enter_promej1, 1,), (self.enter_promej2, 0,), (self.reg_prom, 1,), (self.lect, 1,)],
            # enter_prom2, 6
            [(self.enter_promej2, 1,), (self.reg_prom, 0,), (self.reg, 1,), (self.lestnica1, 1)],  # reg_prom7
            [(self.reg_prom, 1,), (self.reg, 0,)],  # reg, 8
            [(self.enter_promej2, 1,), (self.lect, 0,), (self.gard_prom, 1)],  # lect, 9
            [(self.lect, 1,), (self.gard_prom, 0,), (self.gard, 1,), (self.sanuzel, 1)],  # gard_prom, 10
            [(self.gard_prom, 1,), (self.gard, 0,)],  # gard, 11
            [(self.gard_prom, 1,), (self.sanuzel, 0)],  # sanuzel, 12
            #########################################################################
            [(self.lestnica2, 0,), (self.formular, 1,), (self.lestnica1, 1)],  # lestnica, 13
            [(self.lestnica2, 1,), (self.formular, 0,), (self.form_right_promej, 1,), (self.form_left_promej, 1,),
             (self.k202, 1)],
            # formular, 14
            [(self.formular, 1,), (self.form_right_promej, 0,), (self.k207_right_promej, 1,)],  # form_right, 15
            [(self.k207, 0,), (self.k207_right_promej, 1,)],  # k207, 16
            [(self.k207, 1,), (self.k207_right_promej, 0,), (self.k208_right_promej_1, 1,)],  # k207_right, 17
            [(self.k208, 0,), (self.k208_right_promej_1, 1,)],  # k208, 18
            [(self.k208, 1,), (self.k208_right_promej_1, 0,), (self.k208_right_promej_2, 1,)],  # k208_right1, 19
            [(self.k208_right_promej_1, 1,), (self.k208_right_promej_2, 0,), (self.k210_prom, 1,)],  # k208_right2, 20
            [(self.k208_right_promej_2, 1,), (self.k210_prom, 0,), (self.k210, 1,), (self.k211, 1,), (self.k212, 1,)],
            # k210_prom, 21
            [(self.k210_prom, 1,), (self.k210, 0,)],  # k210, 22
            [(self.k210_prom, 1,), (self.k211, 0,)],  # k211, 23
            [(self.k210_prom, 1,), (self.k212, 0,)],  # k212, 24
            [(self.formular, 1,), (self.k202, 0,), (self.form_left_promej, 1)],  # k202, 25
            [(self.formular, 1,), (self.form_left_promej, 0,), (self.form_left_promej_2, 1,), (self.k202, 1)],
            # form_left,26
            [(self.form_left_promej, 1,), (self.form_left_promej_2, 0,), (self.tri_promej, 1,)],  # form_left2, 27
            [(self.form_left_promej_2, 1), (self.tri_promej, 0,), (self.k205, 1,), (self.tri_promej_down, 1,)],
            # tripromej, 28
            [(self.tri_promej, 1,), (self.k205, 0,)],  # k205, 29
            [(self.tri_promej, 1), (self.tri_promej_down, 0), (self.k203, 1,)],  # tripromleft, 30
            [(self.tri_promej_down, 1,), (self.k203, 0,), (self.k203_prom1, 1,)],  # k203, 31
            [(self.k203, 1,), (self.k203_prom1, 0,), (self.k203_prom2, 1,), (self.museum, 1)],  # k203_prom1, 32
            [(self.k203_prom1, 1,), (self.k203_prom2, 0,), (self.k203a, 1)],  # k203_prom2, 33
            [(self.k203_prom2, 1), (self.k203a, 0)],  # k203a, 34
            [(self.k203_prom1, 1), (self.museum, 0)],  # museum, 35
        ]

    def find_way(self, g, start, t):
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

    def draw_line(self, draw, x1, y1, x2, y2):
        draw.line((x1, y1, x2, y2), fill=(220, 20, 60), width=15)

    def find_path(self, _start, _end, out_files: str, logger):
        """Finds path from `_start` to `_end` id and writes result to {`out_files`}_1.png and {`out_files`}_2.png
            if the room is on the second floor
            :returns maximum floor"""
        # self.image1 = Image.open('assets/floors/1.png')
        # self.image2 = Image.open('assets/floors/2.png')
        try:
            start = self.akindofdb[int(_start)]
        except KeyError:
            start = int(_start)
        try:
            end = self.akindofdb[int(_end)]
        except KeyError:
            end = int(_end)
        # end = k203
        logger.warn("Akindofdb: {}".format(self.akindofdb))
        logger.warn("Pathfinder from {} to {} path: {}".format(start, end, out_files))
        way = self.find_way(self.g, start, end)
        logger.warn(way)

        '''if end <= 13:
            image = self.image1  # Image.open('assets/floors/1.png')
            draw = ImageDraw.Draw(image)
            x, y = self.coords[way[0]]
            for w in way[1:]:
                self.draw_line(draw, x, y, self.coords[w][0], self.coords[w][1])
                x, y = self.coords[w]
            # image.show()
            draw.ellipse((self.coords[start][0], self.coords[start][1], self.coords[start][0] + 4,
                           self.coords[start][1] + 4), fill=(240, 20, 0))
            image.save('{}_1.png'.format(out_files))
            return 1
        elif end <= 35:
            image2 = self.image2  # Image.open('assets/floors/2.png')
            image1 = self.image1  # Image.open('assets/floors/1.png')
            draw1 = ImageDraw.Draw(image1)
            draw2 = ImageDraw.Draw(image2)
            x, y = self.coords[way[0]]
            idx = 0
            for w in way[1:]:
                idx += 1
                self.draw_line(draw1, x, y, self.coords[w][0], self.coords[w][1])
                x, y = self.coords[w]
                if [x, y] == self.coords[self.lestnica1]:
                    break
            if idx + 1 < len(way):
                x, y = self.coords[way[idx + 1]]
                for w in way[idx + 1:]:
                    self.draw_line(draw2, x, y, self.coords[w][0], self.coords[w][1])
                    x, y = self.coords[w]
            if start > 13:
                draw2.ellipse((self.coords[start][0],self.coords[start][1],self.coords[start][0]+30,self.coords[start][1]+30), fill=(240, 20, 0))
            else:
                draw1.ellipse((self.coords[start][0], self.coords[start][1], self.coords[start][0] + 30,
                               self.coords[start][1] + 30), fill=(240, 20, 0))
            # image1.show()
            image1.save('{}_1.png'.format(out_files))
            # image2.show()
            image2.save('{}_2.png'.format(out_files))
            return 2'''
        ###########################################################
        # x, y, f = self.coords[way[0]]
        # lastopened = f
        # image = Image.open('assets/floors/{}.png'.format(f))
        # draw = ImageDraw.Draw(image)
        # x, y, f = self.coords[way[0]]
        # draw.ellipse((x, y, x + 50,
        #               y + 50), fill=(240, 20, 0))
        # floor = f
        # image.save('{}_{}.png'.format(out_files, f))
        # for w in way[1:]:
        #     for i in range(1, len(self.floor_rooms)):
        #         if self.coords.index([x, y]) < self.floor_rooms[i][0]:
        #             image = Image.open('assets/floors/{}.png'.format(
        #                 i))  # стандартное название плана - 1floor, 2floor..., потом можно будет добавить возможность его менять
        #             draw = ImageDraw.Draw(image)
        #             for j in range(len(way[:way.index(self.floor_rooms[i][0])])):
        #                 self.draw_line(draw, x, y, self.coords[w][0], self.coords[w][1])
        #                 x, y = self.coords[w]
        #             image.save('{}_{}.png'.format(out_files, i))
        #             # image.show()
        #             floor = i

        x, y, f = self.coords[way[0]]
        lastopened = f
        image = Image.open('assets/floors/{}.png'.format(f))
        draw = ImageDraw.Draw(image)
        draw.ellipse((x, y, x + 50, y + 50), fill=(240, 20, 0))
        # logger.warn("Way: {}".format(way))
        for w in way[1:]:
            if [x, y, f] != self.floor_rooms[f - 1][1]:
                self.draw_line(draw, x, y, self.coords[w][0], self.coords[w][1])
            x, y, f = self.coords[w]
            # logger.warn("Adding coords: {}".format((x,y,f,lastopened)))
            if lastopened != f:
                # logger.warn("Saving to {}".format('{}_{}.png'.format(out_files, f-1)))
                image.save('{}_{}.png'.format(out_files, f-1))
                image, lastopened = Image.open('assets/floors/{}.png'.format(f)), f  # стандартное название плана - 1floor, 2floor..., потом можно будет добавить возможность его менятьe
                draw = ImageDraw.Draw(image)
        image.save('{}_{}.png'.format(out_files, f))
        #############################################################
        return f
