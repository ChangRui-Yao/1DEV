import pymunk
from pymunk import Vec2d
import pymunk.pygame_util

    ## Colors
White = 255, 255, 255
Red = 255, 0, 0
Green = 0, 255, 0
Purple = 65, 28, 139
Blue = 0, 0, 255
Black = 0, 0, 0

    ## Poly's body_type
b = pymunk.Body(body_type=pymunk.Body.STATIC)

    ## C'est parti ...
def drawSegments(space):
    global_walls = [pymunk.Segment(space.static_body, (250, 0), (250, 390), 2),
                    pymunk.Segment(space.static_body, (250, 384), (264, 393), 4),
                    pymunk.Segment(space.static_body, (256, 390), (256, 768), 8),
                    pymunk.Segment(space.static_body, (260, 730), (280, 745), 8),
                    pymunk.Segment(space.static_body, (278, 738), (370, 738), 4),
                    pymunk.Segment(space.static_body, (370, 738), (415, 765), 4),
                    pymunk.Segment(space.static_body, (415, 765), (750, 765), 4),
                    pymunk.Segment(space.static_body, (655, 768), (700, 753), 8),
                    pymunk.Segment(space.static_body, (700, 753), (735, 720), 8),
                    pymunk.Segment(space.static_body, (725, 768), (750, 648), 4),
                    pymunk.Segment(space.static_body, (750, 768), (750, 0), 6),
                    pymunk.Segment(space.static_body, (702, 752), (730, 752), 9),
                    pymunk.Segment(space.static_body, (265, 391), (302, 412), 2),
                    pymunk.Segment(space.static_body, (302, 411), (264, 505), 2),
                    pymunk.Segment(space.static_body, (718, 500), (678, 450), 2),
                    pymunk.Segment(space.static_body, (678, 450), (718, 400), 2),
                    pymunk.Segment(space.static_body, (718, 412), (697, 382), 2),
                    pymunk.Segment(space.static_body, (697, 382), (718, 309), 2),
                    pymunk.Segment(space.static_body, (290, 680), (290, 510), 2),
                    pymunk.Segment(space.static_body, (290, 510), (328, 425), 2),
                    pymunk.Poly(b, [(330,427),(400,495),(400,495),(300,495)]),

                    pymunk.Poly(b,[(260,768),(260,740),(370,740),(420,768)]),
                    pymunk.Poly(b,[(745,768),(745,680),(740,680),(736,720),(715,768)])]


    for line in global_walls:
        line.elasticity = 0.7
        line.group = 1
        line.color = White
    space.add(global_walls)

        ## Blue polygons
    blue_pols = [pymunk.Poly(b,[(265,392),(300,412),(265,500)]),
                pymunk.Poly(b, [(720,500),(680,450),(720,400)]),
                pymunk.Poly(b, [(720,410),(700,380),(720,310)]),
                pymunk.Segment(space.static_body, (720,0),(720,640),1)
    ]

    for pol in blue_pols:
        pol.elasticity = 0.7
        pol.color = Blue
    space.add(blue_pols)


    left_shape = [pymunk.Segment(space.static_body, (280, 258), (280, 168), 1.0),
                   pymunk.Segment(space.static_body, (280, 168), (300, 168), 1.0),
                   pymunk.Segment(space.static_body, (300, 168), (330, 100), 1.0),
                   pymunk.Segment(space.static_body, (330, 100), (375, 87), 1.0),
                   pymunk.Segment(space.static_body, (340, 248), (340, 158), 1.0),
                   pymunk.Segment(space.static_body, (340, 158), (335, 147), 1.0),
                   pymunk.Segment(space.static_body, (335, 147), (350, 118), 1.0),
                   pymunk.Segment(space.static_body, (350, 118), (385, 108), 1.0),
                   pymunk.Segment(space.static_body, (350, 118), (385, 108), 1.0),
                   pymunk.Segment(space.static_body, (385, 108), (400, 123), 1.0),
                   pymunk.Segment(space.static_body, (303, 258), (303, 228), 1.0),
                   pymunk.Segment(space.static_body, (325, 258), (325, 228), 1.0)]

    for line in left_shape:
        line.elasticity = 0.7
        line.group = 1
    space.add(left_shape)

    right_shape = [pymunk.Segment(space.static_body, (740, 118), (680, 118), 1.0),
                   pymunk.Segment(space.static_body, (680, 118), (680, 114), 1.0),
                   pymunk.Segment(space.static_body, (680, 114), (605, 86), 1.0),
                   pymunk.Segment(space.static_body, (650, 248), (660, 228), 1.0),
                   pymunk.Segment(space.static_body, (660, 228), (660, 128), 1.0),
                   pymunk.Segment(space.static_body, (660, 128), (610, 108), 1.0),
                   pymunk.Segment(space.static_body, (610, 108), (590, 133), 1.0),
                   pymunk.Segment(space.static_body, (680, 298), (690, 270), 1.0),
                   pymunk.Segment(space.static_body, (690, 270), (690, 240), 1.0),
                   pymunk.Segment(space.static_body, (690, 240), (670, 278), 1.0),
                   pymunk.Segment(space.static_body, (670, 278), (680, 298), 1.0)]

    for line in right_shape:
        line.elasticity = 0.7
        line.group = 1
    space.add(right_shape)

    # Much elasticity for that ones
    left_right_panes = [pymunk.Segment(space.static_body, (340, 248), (400, 123), 1.0),
                        pymunk.Segment(space.static_body, (650, 248), (590, 133), 1.0)]

    for line in left_right_panes:
        line.elasticity = 1.2
        line.group = 1
    space.add(left_right_panes)