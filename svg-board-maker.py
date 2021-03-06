import svgwrite
from svgwrite import cm, mm


def basic_shapes(name):
    dwg = svgwrite.Drawing(filename=name, debug=True)
    shapes = dwg.add(dwg.g(id='shapes', fill='red'))
    SquareNames = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8',
                   'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8',
                    'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8',
                    'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8',
                    'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8',
                    'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8',
                    'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8',
                    'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8']

    chess_columns = ["a", "b", "c", "d", "e", "f", "g", "h"]
    #chess_rows = ''.join(str(e) for e in range(1,9))
    chess_rows = [str(e) for e in range(1,9)]

    print (chess_rows)


    #How to join these lists into a matrix, pythonically?
    #SquareNames = [a+b for a,b in (chess_columns,chess_rows)]

    print (SquareNames)


    size = 2.0
    x = 0
    y = 0
    for t in range(64):
        x = t % 8
        y = t // 8
        if (((x+y) % 2) == 1):
            fillcolor = 'lightgray'
        else:
            fillcolor = 'white'
        shapes.add(dwg.rect(insert=(x*size*cm, y*size*cm), size=(size*cm, size*cm),
                        fill=fillcolor, stroke='black', stroke_width=1))
        dwg.add(dwg.text(SquareNames[t], insert=((0.12+x*size)*cm, (0.22+y*size)*cm), fill='black'))
    dwg.save()


if __name__ == '__main__':
    basic_shapes('basic_board.svg')


    import svgutils

    #template = svgutils.fromfile('basic_board.svg')

    #TODO: This is machine & OS dependent.  Fix it!
    Projectfolder = "C:\\Users\\alexa\\Documents\\GitHub\\Capyblanca\\Vector.Chess.Pieces\\"

    #Importing black king
    from svgutils.compose import *

    size = 2.0

    Figure("16cm", "16cm",
        Panel(
              SVG("basic_board.svg")
             ),
        Panel(
              SVG(Projectfolder+"black.bishop.svg").move(2.0,4.0).scale(size * 0.75),
              Text("Look a bishop!", 25, 400, size=12, weight='bold')
             )
        ).save("fig_final_compose.svg")
