from fpdf import FPDF


WIDTH = 210
HEIGHT = 297

pdf = FPDF()
pdf.add_page()
pdf.image('letterhead.png', w=WIDTH-5)
pdf.image('team_compare.png', y=60, w=WIDTH/2 - 5, h=80)
pdf.image('fifa_foot.png', x=WIDTH/2, y=60, w=WIDTH/2 - 5, h=80)
pdf.image('player_weight.png', x=WIDTH/2, y=140, w=WIDTH/2 - 5, h=80)
pdf.image('fifa_overall.png', y=140, w=WIDTH/2 - 5, h=80)

pdf.output('fifa_graphs.pdf', 'F')
