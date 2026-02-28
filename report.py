import pandas as pd
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Image

# Load summaries
category_summary = pd.read_csv("category_summary.csv")
region_summary = pd.read_csv("region_summary.csv")
subcategory_summary = pd.read_csv("subcategory_summary.csv")

# Create PDF
doc = SimpleDocTemplate("Superstore_Report.pdf", pagesize=A4)
elements = []
styles = getSampleStyleSheet()

# Custom Centered Title
centered_title = ParagraphStyle(
    name="CenteredTitle",
    parent=styles["Heading1"],
    alignment=1)

# Title
elements.append(Paragraph("<b>Sales & Profit Analysis Report</b>", styles['Title']))
elements.append(Spacer(1, 20))

#insight 
elements.append(Paragraph("<b>Key Business Insights</b>", styles['Heading2']))
elements.append(Spacer(1, 10))

elements.append(Paragraph(
    "1. Technology category generates the highest overall profit.",
    styles['Normal']
))
elements.append(Spacer(1, 5))

elements.append(Paragraph(
    "2. Furniture has high sales but comparatively low profit margins.",
    styles['Normal']
))
elements.append(Spacer(1, 20))





#chart section 


elements.append(Paragraph("<b>Category Profit Chart</b>", styles['Heading2']))
elements.append(Spacer(1, 10))
elements.append(Image("category_profit.png", width=400, height=250))
elements.append(Spacer(1, 20))

elements.append(Paragraph("<b>Region Profit Chart</b>", styles['Heading2']))
elements.append(Spacer(1, 10))
elements.append(Image("region_profit.png", width=400, height=250))
elements.append(Spacer(1, 20))

# Category Section
elements.append(Paragraph("<b>Category Performance</b>", styles['Heading2']))
elements.append(Spacer(1, 10))
elements.append(Spacer(1,20))


cat_data = [category_summary.columns.tolist()] + category_summary.values.tolist()
cat_table = Table(cat_data)
cat_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.grey),
    ('TEXTCOLOR',(0,0),(-1,0),colors.whitesmoke),
    ('GRID', (0,0), (-1,-1), 1, colors.black),
    ('ALIGN',(1,1),(-1,-1),'RIGHT')
]))

elements.append(cat_table)
elements.append(Spacer(1, 20))
elements.append(Paragraph(
"Insight: Technology leads in profit generation while Furniture shows weaker margins.",
styles["Normal"]
))
elements.append(Spacer(1, 20))

# Region Section
elements.append(Paragraph("<b>Region Performance</b>", styles['Heading2']))
elements.append(Spacer(1, 10))

reg_data = [region_summary.columns.tolist()] + region_summary.values.tolist()
reg_table = Table(reg_data)
reg_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.grey),
    ('TEXTCOLOR',(0,0),(-1,0),colors.whitesmoke),
    ('GRID', (0,0), (-1,-1), 1, colors.black),
    ('ALIGN', (1,1), (-1,-1), 'RIGHT')
]))

elements.append(reg_table)
elements.append(Spacer(1, 20))

elements.append(Paragraph(
"Insight: West region generates the highest overall profit contribution.",
styles["Normal"]
))
elements.append(Spacer(1, 20))



# Sub-Category Section
elements.append(Paragraph("<b>Sub-Category Performance</b>", styles['Heading2']))
elements.append(Spacer(1, 10))

sub_data = [subcategory_summary.columns.tolist()] + subcategory_summary.values.tolist()
sub_table = Table(sub_data)
sub_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.grey),
    ('TEXTCOLOR',(0,0),(-1,0),colors.whitesmoke),
    ('GRID', (0,0), (-1,-1), 1, colors.black),
    ('ALIGN', (1,1), (-1,-1), 'RIGHT')
]))

elements.append(sub_table)
elements.append(Spacer(1, 10))

elements.append(Paragraph(
"Insight: Copiers and Phones are highly profitable sub-categories.",
styles["Normal"]
))

# Build PDF
doc.build(elements)

print("Report generated successfully!")