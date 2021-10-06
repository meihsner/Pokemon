from PokemonStructures import *


class PalletTown:
    def __init__(self, path_structures):
        self.path_structures = path_structures
        self.house_PT = House(245, 40, path_structures)
        self.house2_PT = House(698, 40, path_structures)
        self.lab_PT = Lab(624, 325, path_structures)
        self.mailbox_PT = Mailbox(215, 178, path_structures)
        self.mailbox2_PT = Mailbox(668, 178, path_structures)
        self.brown_sign_PT = BrownSign(190, 520, path_structures)
        self.white_sign_PT = WhiteSign(774, 620, path_structures)
        self.white_sign2_PT = WhiteSign(430, 375, path_structures)
        self.bacground1_PT = GrassBackground(0, 0, path_structures)
        self.bacground2_PT = GrassBackground(-620, 0, path_structures)
        self.bacground3_PT = GrassBackground(0, 470, path_structures)
        self.bacground4_PT = GrassBackground(-620, 470, path_structures)
        self.bacground5_PT = GrassBackground(620, 0, path_structures)
        self.bacground6_PT = GrassBackground(0, -470, path_structures)
        self.bacground7_PT = GrassBackground(620, -470, path_structures)
        self.bacground8_PT = GrassBackground(-620, -470, path_structures)
        self.bacground9_PT = GrassBackground(620, 470, path_structures)
        self.bacground10_PT = GrassBackground(1240, 0, path_structures)
        self.bacground11_PT = GrassBackground(1240, 470, path_structures)
        self.bacground12_PT = GrassBackground(1240, -470, path_structures)
        self.bacground13_PT = GrassBackground(0, 940, path_structures)
        self.bacground14_PT = GrassBackground(-620, 940, path_structures)
        self.bacground15_PT = GrassBackground(620, 940, path_structures)

        self.grasses = []
        for y in range(-312, -88, 32):
            gr = Grass(610, y, path_structures)
            self.grasses.append(gr)
        for y in range(-312, -88, 32):
            gr = Grass(642, y, path_structures)
            self.grasses.append(gr)

        self.path_e_NW = [PathEntrance(278, 230, 2, path_structures), PathEntrance(730, 230, 2, path_structures),
                          PathEntrance(762, 544, 2, path_structures)]
        self.path_e_NE = [PathEntrance(308, 230, 1, path_structures), PathEntrance(760, 230, 1, path_structures),
                          PathEntrance(792, 544, 1, path_structures)]

        self.trees = []
        for y in range(-360, 986, 64):
            tr = Tree(1060, y, path_structures)
            self.trees.append(tr)
        for y in range(-360, 986, 64):
            tr = Tree(1125, y, path_structures)
            self.trees.append(tr)
        for y in range(-360, 986, 64):
            tr = Tree(1190, y, path_structures)
            self.trees.append(tr)
        for y in range(-360, 986, 64):
            tr = Tree(1255, y, path_structures)
            self.trees.append(tr)
        for y in range(-360, 986, 64):
            tr = Tree(1320, y, path_structures)
            self.trees.append(tr)

        for y in range(-360, 986, 64):
            tr = Tree(35, y, path_structures)
            self.trees.append(tr)
        for y in range(-360, 986, 64):
            tr = Tree(-30, y, path_structures)
            self.trees.append(tr)
        for y in range(-360, 986, 64):
            tr = Tree(-95, y, path_structures)
            self.trees.append(tr)
        for y in range(-360, 986, 64):
            tr = Tree(-160, y, path_structures)
            self.trees.append(tr)
        for y in range(-360, 986, 64):
            tr = Tree(-225, y, path_structures)
            self.trees.append(tr)

        for x in range(99, 611, 64):
            tr = Tree(x, -168, path_structures)
            self.trees.append(tr)
        for x in range(99, 611, 64):
            tr = Tree(x, -104, path_structures)
            self.trees.append(tr)
        for x in range(676, 1060, 64):
            tr = Tree(x, -168, path_structures)
            self.trees.append(tr)
        for x in range(676, 1060, 64):
            tr = Tree(x, -104, path_structures)
            self.trees.append(tr)
        for x in range(99, 291, 64):
            tr = Tree(x, 730, path_structures)
            self.trees.append(tr)
        for x in range(99, 291, 64):
            tr = Tree(x, 794, path_structures)
            self.trees.append(tr)
        for x in range(99, 291, 64):
            tr = Tree(x, 858, path_structures)
            self.trees.append(tr)
        for x in range(99, 291, 64):
            tr = Tree(x, 922, path_structures)
            self.trees.append(tr)

        for x in range(99, 291, 64):
            tr = Tree(x, 730, path_structures)
            self.trees.append(tr)
        for x in range(99, 291, 64):
            tr = Tree(x, 794, path_structures)
            self.trees.append(tr)
        for x in range(99, 291, 64):
            tr = Tree(x, 858, path_structures)
            self.trees.append(tr)
        for x in range(99, 291, 64):
            tr = Tree(x, 922, path_structures)
            self.trees.append(tr)
        for x in range(99, 291, 64):
            tr = Tree(x, 986, path_structures)
            self.trees.append(tr)

        for x in range(804, 1060, 64):
            tr = Tree(x, 730, path_structures)
            self.trees.append(tr)
        for x in range(804, 1060, 64):
            tr = Tree(x, 794, path_structures)
            self.trees.append(tr)
        for x in range(804, 1060, 64):
            tr = Tree(x, 858, path_structures)
            self.trees.append(tr)
        for x in range(804, 1060, 64):
            tr = Tree(x, 922, path_structures)
            self.trees.append(tr)
        for x in range(804, 1060, 64):
            tr = Tree(x, 986, path_structures)
            self.trees.append(tr)

        self.flowers = []
        for x in range(190, 400, 32):
            flower = Flower(x, 410, path_structures)
            self.flowers.append(flower)
        for x in range(190, 400, 32):
            flower = Flower(x, 440, path_structures)
            self.flowers.append(flower)
        for x in range(190, 400, 32):
            flower = Flower(x, 470, path_structures)
            self.flowers.append(flower)
        for x in range(190, 400, 32):
            flower = Flower(x, 500, path_structures)
            self.flowers.append(flower)

        self.white_fence_N = []
        for x in range(190, 446, 32):
            fn = WhiteFence(x, 376, 1, path_structures)
            self.white_fence_N.append(fn)
        for x in range(600, 952, 32):
            fn = WhiteFence(x, 622, 1, path_structures)
            self.white_fence_N.append(fn)
        for x in range(524, 812, 32):
            fn = WhiteFence(x, 780, 1, path_structures)
            self.white_fence_N.append(fn)
        for x in range(276, 372, 32):
            fn = WhiteFence(x, 780, 1, path_structures)
            self.white_fence_N.append(fn)

        for x in range(99, 611, 32):
            fn = WhiteFence(x, -266, 1, path_structures)
            self.white_fence_N.append(fn)
        for x in range(675, 1059, 32):
            fn = WhiteFence(x, -266, 1, path_structures)
            self.white_fence_N.append(fn)

        self.white_fence_E = []
        for y in range(810, 1098, 30):
            fe = WhiteFence(340, y, 2, path_structures)
            self.white_fence_E.append(fe)
        for y in range(810, 1098, 30):
            fe = WhiteFence(746, y, 2, path_structures)
            self.white_fence_E.append(fe)
        for y in range(-234, -138, 30):
            fe = WhiteFence(579, y, 2, path_structures)
            self.white_fence_E.append(fe)

        self.white_fence_W = []
        for y in range(-234, -138, 30):
            fw = WhiteFence(675, y, 4, path_structures)
            self.white_fence_W.append(fw)

        self.white_fence_NE = [WhiteFence(340, 780, 3, path_structures), WhiteFence(746, 780, 3, path_structures),
                               WhiteFence(579, -266, 3, path_structures)]
        self.white_fence_NW = [WhiteFence(675, -266, 5, path_structures)]

        self.path_C = [Path(972, 309, 1, path_structures), Path(970, 564, 1, path_structures),
                       Path(970, 554, 1, path_structures),
                       Path(970, 652, 1, path_structures), Path(548, 550, 1, path_structures),
                       Path(548, 563, 1, path_structures),
                       Path(515, 560, 1, path_structures), Path(124, 556, 1, path_structures),
                       Path(548, 658, 1, path_structures)]
        self.path_NW = [Path(100, -15, 2, path_structures), Path(600, -84, 2, path_structures)]
        self.path_N = []
        self.path_NE = [Path(657, -84, 4, path_structures), Path(1010, -12, 4, path_structures)]
        self.path_W = []
        self.path_E = []
        self.path_SW = [Path(100, 636, 7, path_structures)]
        self.path_S = []
        self.path_SE = [Path(1010, 704, 9, path_structures)]

        for y in range(-10, 650, 30):
            pathw = Path(100, y, 5, path_structures)
            self.path_W.append(pathw)
        for y in range(60, 240, 30):
            pathw = Path(507, y, 5, path_structures)
            self.path_W.append(pathw)
        for y in range(-68, -20, 30):
            pathw = Path(602, y, 5, path_structures)
            self.path_W.append(pathw)
        for y in range(378, 548, 30):
            pathw = Path(507, y, 5, path_structures)
            self.path_W.append(pathw)
        for y in range(343, 543, 30):
            pathw = Path(969, y, 5, path_structures)
            self.path_W.append(pathw)
        for y in range(60, 240, 30):
            pathw = Path(964, y, 5, path_structures)
            self.path_W.append(pathw)
        for y in range(597, 657, 30):
            pathw = Path(964, y, 5, path_structures)
            self.path_W.append(pathw)

        for y in range(30, 240, 30):
            pathe = Path(132, y, 6, path_structures)
            self.path_E.append(pathe)
        for y in range(60, 240, 30):
            pathe = Path(550, y, 6, path_structures)
            self.path_E.append(pathe)
        for y in range(340, 550, 30):
            pathe = Path(555, y, 6, path_structures)
            self.path_E.append(pathe)
        for y in range(-68, -20, 30):
            pathe = Path(655, y, 6, path_structures)
            self.path_E.append(pathe)
        for y in range(375, 555, 30):
            pathe = Path(132, y, 6, path_structures)
            self.path_E.append(pathe)
        for y in range(-10, 710, 30):
            pathe = Path(1010, y, 6, path_structures)
            self.path_E.append(pathe)
        for y in range(597, 657, 30):
            pathe = Path(555, y, 6, path_structures)
            self.path_E.append(pathe)

        for x in range(157, 507, 30):
            paths = Path(x, 36, 8, path_structures)
            self.path_S.append(paths)
        for x in range(575, 965, 30):
            paths = Path(x, 36, 8, path_structures)
            self.path_S.append(paths)
        for x in range(580, 970, 30):
            paths = Path(x, 320, 8, path_structures)
            self.path_S.append(paths)
        for x in range(158, 518, 30):
            paths = Path(x, 350, 8, path_structures)
            self.path_S.append(paths)
        for x in range(120, 370, 30):
            paths = Path(x, 635, 8, path_structures)
            self.path_S.append(paths)
        for x in range(580, 950, 30):
            paths = Path(x, 570, 8, path_structures)
            self.path_S.append(paths)
        for x in range(520, 1010, 30):
            paths = Path(x, 705, 8, path_structures)
            self.path_S.append(paths)

        for x in range(125, 580, 30):
            pathn = Path(x, -12, 3, path_structures)
            self.path_N.append(pathn)
        for x in range(158, 278, 30):
            pathn = Path(x, 228, 3, path_structures)
            self.path_N.append(pathn)
        for x in range(331, 501, 30):
            pathn = Path(x, 228, 3, path_structures)
            self.path_N.append(pathn)
        for x in range(582, 732, 30):
            pathn = Path(x, 228, 3, path_structures)
            self.path_N.append(pathn)
        for x in range(785, 965, 30):
            pathn = Path(x, 228, 3, path_structures)
            self.path_N.append(pathn)
        for x in range(682, 1012, 30):
            pathn = Path(x, -12, 3, path_structures)
            self.path_N.append(pathn)
        for x in range(612, 672, 30):
            pathn = Path(x, -85, 3, path_structures)
            self.path_N.append(pathn)
        for x in range(580, 760, 30):
            pathn = Path(x, 544, 3, path_structures)
            self.path_N.append(pathn)
        for x in range(820, 970, 30):
            pathn = Path(x, 544, 3, path_structures)
            self.path_N.append(pathn)
        for x in range(156, 516, 30):
            pathn = Path(x, 557, 3, path_structures)
            self.path_N.append(pathn)
        for x in range(580, 950, 30):
            pathn = Path(x, 655, 3, path_structures)
            self.path_N.append(pathn)

        for y in range(10, 40, 20):
            pathc = Path(125, y, 1, path_structures)
            self.path_C.append(pathc)
        for y in range(-65, 5, 20):
            pathc = Path(630, y, 1, path_structures)
            self.path_C.append(pathc)
        for y in range(62, 242, 20):
            pathc = Path(530, y, 1, path_structures)
            self.path_C.append(pathc)
        for y in range(60, 560, 20):
            pathc = Path(990, y, 1, path_structures)
            self.path_C.append(pathc)
        for y in range(242, 312, 20):
            pathc = Path(965, y, 1, path_structures)
            self.path_C.append(pathc)
        for y in range(552, 702, 20):
            pathc = Path(990, y, 1, path_structures)
            self.path_C.append(pathc)
        for y in range(380, 670, 20):
            pathc = Path(535, y, 1, path_structures)
            self.path_C.append(pathc)
        for y in range(640, 680, 20):
            pathc = Path(520, y, 1, path_structures)
            self.path_C.append(pathc)

        for x in range(150, 930, 30):
            pathc = Path(x, 5, 1, path_structures)
            self.path_C.append(pathc)
        for x in range(150, 930, 30):
            pathc = Path(x, 15, 1, path_structures)
            self.path_C.append(pathc)
        for x in range(607, 627, 20):
            pathc = Path(x, -6, 1, path_structures)
            self.path_C.append(pathc)
        self.path_C.append(Path(650, -6, 1, path_structures))
        for x in range(519, 559, 20):
            pathc = Path(x, 28, 1, path_structures)
            self.path_C.append(pathc)
        self.path_C.append(Path(543, 28, 1, path_structures))
        for x in range(130, 960, 20):
            pathc = Path(x, 260, 1, path_structures)
            self.path_C.append(pathc)
        for x in range(130, 960, 20):
            pathc = Path(x, 290, 1, path_structures)
            self.path_C.append(pathc)
        for x in range(130, 560, 20):
            pathc = Path(x, 320, 1, path_structures)
            self.path_C.append(pathc)
        for x in range(920, 1000, 20):
            pathc = Path(x, 20, 1, path_structures)
            self.path_C.append(pathc)
        for x in range(966, 996, 20):
            pathc = Path(x, 26, 1, path_structures)
            self.path_C.append(pathc)
        for x in range(520, 1000, 20):
            pathc = Path(x, 686, 1, path_structures)
            self.path_C.append(pathc)
        for x in range(130, 530, 20):
            pathc = Path(x, 590, 1, path_structures)
            self.path_C.append(pathc)
        for x in range(130, 530, 20):
            pathc = Path(x, 610, 1, path_structures)
            self.path_C.append(pathc)
        self.path_C.append(Path(126, 241, 1, path_structures))
        self.path_C.append(Path(120, 350, 1, path_structures))
        self.path_C.append(Path(126, 350, 1, path_structures))
        self.path_C.append(Path(505, 240, 1, path_structures))
        self.path_C.append(Path(550, 235, 1, path_structures))
        self.path_C.append(Path(520, 245, 1, path_structures))
        self.path_C.append(Path(517, 354, 1, path_structures))
        self.path_C.append(Path(527, 354, 1, path_structures))

        self.we_C = []
        self.we_NW = [WaterEdge(372, 644, 2, path_structures)]
        self.we_N = []
        self.we_NE = [WaterEdge(492, 644, 4, path_structures)]
        self.we_W = []
        self.we_E = []
        self.we_SW = []
        self.we_S = []
        self.we_SE = []

        for x in range(372, 492, 30):
            wen = WaterEdge(x, 644, 3, path_structures)
            self.we_N.append(wen)
        for y in range(674, 1094, 30):
            wee = WaterEdge(492, y, 6, path_structures)
            self.we_E.append(wee)
        for y in range(674, 1094, 30):
            wew = WaterEdge(372, y, 5, path_structures)
            self.we_W.append(wew)
        for y in range(674, 1094, 30):
            wec = WaterEdge(404, y, 1, path_structures)
            self.we_C.append(wec)
        for y in range(674, 1094, 30):
            wec = WaterEdge(434, y, 1, path_structures)
            self.we_C.append(wec)
        for y in range(674, 1094, 30):
            wec = WaterEdge(464, y, 1, path_structures)
            self.we_C.append(wec)

        # self.NPC_1 = NPC1(110, 330, path_NPC)
        # self.NPC_2 = NPC2(525, 675, path_NPC)

    def draw_and_update(self, screen, player):
        screen.fill((0, 0, 0))
        self.bacground1_PT.draw(screen)
        self.bacground1_PT.update(player)
        self.bacground2_PT.draw(screen)
        self.bacground2_PT.update(player)
        self.bacground3_PT.draw(screen)
        self.bacground3_PT.update(player)
        self.bacground4_PT.draw(screen)
        self.bacground4_PT.update(player)
        self.bacground5_PT.draw(screen)
        self.bacground5_PT.update(player)
        self.bacground6_PT.draw(screen)
        self.bacground6_PT.update(player)
        self.bacground7_PT.draw(screen)
        self.bacground7_PT.update(player)
        self.bacground8_PT.draw(screen)
        self.bacground8_PT.update(player)
        self.bacground9_PT.draw(screen)
        self.bacground9_PT.update(player)
        self.bacground10_PT.draw(screen)
        self.bacground10_PT.update(player)
        self.bacground11_PT.draw(screen)
        self.bacground11_PT.update(player)
        self.bacground12_PT.draw(screen)
        self.bacground12_PT.update(player)
        self.bacground13_PT.draw(screen)
        self.bacground13_PT.update(player)
        self.bacground14_PT.draw(screen)
        self.bacground14_PT.update(player)
        self.bacground15_PT.draw(screen)
        self.bacground15_PT.update(player)

        for path in self.path_W:
            path.draw(screen)
            path.update(player)
        for path in self.path_E:
            path.draw(screen)
            path.update(player)
        for path in self.path_NW:
            path.draw(screen)
            path.update(player)
        for path in self.path_NE:
            path.draw(screen)
            path.update(player)
        for path in self.path_S:
            path.draw(screen)
            path.update(player)
        for path in self.path_N:
            path.draw(screen)
            path.update(player)
        for path in self.path_C:
            path.draw(screen)
            path.update(player)
        for path in self.path_SW:
            path.draw(screen)
            path.update(player)
        for path in self.path_SE:
            path.draw(screen)
            path.update(player)

        for gr in self.grasses:
            gr.draw(screen)
            gr.update(player)

        for fence in self.white_fence_N:
            fence.draw(screen)
            fence.update(player)
        for fence in self.white_fence_E:
            fence.draw(screen)
            fence.update(player)
        for fence in self.white_fence_NE:
            fence.draw(screen)
            fence.update(player)
        for fence in self.white_fence_NW:
            fence.draw(screen)
            fence.update(player)
        for fence in self.white_fence_W:
            fence.draw(screen)
            fence.update(player)

        for flow in self.flowers:
            flow.draw(screen)
            flow.update(player)

        for tr in self.trees:
            tr.draw(screen)
            tr.update(player)

        for we in self.we_N:
            we.draw(screen)
            we.update(player)
        for we in self.we_NE:
            we.draw(screen)
            we.update(player)
        for we in self.we_NW:
            we.draw(screen)
            we.update(player)
        for we in self.we_E:
            we.draw(screen)
            we.update(player)
        for we in self.we_W:
            we.draw(screen)
            we.update(player)
        for we in self.we_C:
            we.draw(screen)
            we.update(player)
        for pe in self.path_e_NW:
            pe.draw(screen)
            pe.update(player)
        for pe in self.path_e_NE:
            pe.draw(screen)
            pe.update(player)

        self.house_PT.draw(screen)
        self.house_PT.update(player)
        self.house2_PT.draw(screen)
        self.house2_PT.update(player)
        self.mailbox_PT.draw(screen)
        self.mailbox_PT.update(player)
        self.mailbox2_PT.draw(screen)
        self.mailbox2_PT.update(player)
        self.lab_PT.draw(screen)
        self.lab_PT.update(player)
        self.white_sign_PT.draw(screen)
        self.white_sign_PT.update(player)
        self.white_sign2_PT.draw(screen)
        self.white_sign2_PT.update(player)
        self.brown_sign_PT.draw(screen)
        self.brown_sign_PT.update(player)
