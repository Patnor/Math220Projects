import numpy as np
import pandas as pd
from glob import glob
import matplotlib.pyplot as plt
import cv2
from PIL import Image, ImageDraw, ImageFont


felixArray = np.array([
    [1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1],
    [1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1],
    [1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,1,1,0,0,1,1,1,1,1],
    [1,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,0,0,1,1,1,1],
    [1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,0,0,1,1,1],
    [1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,0,1,1,1],
    [1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1,1],
    [1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,0,1,0,0,1],
    [1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,0,1,1,1,0,0,0,1,0,1],
    [1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,0,1,1,1,0,0,0,1,0,0],
    [1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,0,0,1,1,0,0,0,1,0,0],
    [1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,0,0,1,1,0,0,0,1,0,0],
    [1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,0,0,1,1,1,0,0,1,1,0],
    [1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,1,1,1,0,0,0,1,1,1,1,1,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,0,1,1,1,1,1,1,0],
    [1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,0,0,0,0,1,0,0],
    [1,1,0,0,0,0,0,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,1,0,0,0,0,0,0,0,1,0],
    [1,1,1,0,0,0,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,0,0,1,1,0,0,0,0,0,0,1,0,0],
    [1,1,0,0,0,0,1,1,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,1,1,1,0,0,0,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0],
    [1,1,1,1,0,0,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1],
    [1,1,1,1,1,0,0,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,0,0,1],
    [1,1,1,1,1,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,1,1,0,1,1],
    [1,1,1,1,1,1,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,1],
    [1,1,1,1,1,1,1,0,0,1,1,1,1,1,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,1,0,0,1,1,1],
    [1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,1,0,0,1,0,0,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,0,0,1,1,1,1,1,1,1,0,0,1,0,0,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1]
    ])

felixArray255 = felixArray * 255

# # Set the font (replace 'arial.ttf' with the actual font file and 24 with the font size)
font = ImageFont.truetype('arial.ttf', 36)

# Set the position and text for the label
label_position = (10, 10)  # Adjust the position where you want to place the label
# Set the color for the label text (optional)
label_color = (1)  # RGB values for white

# Original Felix ===============================================================
label_text = 'A - Original Felix'
originalFelix = felixArray255.copy()

originalFelixImage = Image.fromarray(originalFelix.astype('uint8'))

originalFelixImage = originalFelixImage.resize((700, 700))
draw = ImageDraw.Draw(originalFelixImage)

# Draw the label on the image
draw.text(label_position, label_text, font=font, fill=label_color )

originalFelixImage.show()

# Transposed Felix =============================================================
label_text = 'B - Transposed Felix'
transposedFelix = felixArray255.copy()
transposedFelix = np.transpose(transposedFelix)
transposedFelixImage = Image.fromarray(transposedFelix.astype('uint8'))

resizedFelix = transposedFelixImage.resize((700, 700))

draw = ImageDraw.Draw(resizedFelix)


# Draw the label on the image
draw.text(label_position, label_text, font=font, fill=label_color )

resizedFelix.show()


# swap columns of felix ========================================================

# Determine the number of columns
num_columns = felixArray255.shape[1]

columnSwappedFelix = felixArray255.copy()

# Swap pairs of columns
for i in range(num_columns // 2):
    column_index1 = i
    column_index2 = num_columns - 1 - i

    # Swap the columns
    columnSwappedFelix[:, [column_index1, column_index2]] = columnSwappedFelix[:, [column_index2, column_index1]]


label_text = 'C - Column Swapped Felix'

columnSwapFelixImage = Image.fromarray(columnSwappedFelix.astype('uint8'))

columnSwapFelixImage = columnSwapFelixImage.resize((700, 700))
draw = ImageDraw.Draw(columnSwapFelixImage)

# Draw the label on the image
draw.text(label_position, label_text, font=font, fill=label_color )

columnSwapFelixImage.show()

# swap rows of felix ===========================================================

num_rows = felixArray255.shape[0]
rowSwappedFelix = felixArray255.copy()
label_text = 'D - Row Swapped Felix'

for i in range(num_rows // 2):
    row_index1 = i
    row_index2 = num_rows - 1 - i

    # Swap the rows
    rowSwappedFelix[[row_index1, row_index2], :] = rowSwappedFelix[[row_index2, row_index1], :]

rowSwapFelixImage = Image.fromarray(rowSwappedFelix.astype('uint8'))
rowSwapFelixImage = rowSwapFelixImage.resize((700, 700))
draw = ImageDraw.Draw(rowSwapFelixImage)

draw.text(label_position, label_text, font=font, fill=label_color )

rowSwapFelixImage.show()


# swap rows and columns of felix ================================================
num_rows = felixArray255.shape[0]
num_columns = felixArray255.shape[1]
rowColSwappedFelix = felixArray255.copy()
label_text = 'E - Row - Col\n Swapped Felix'

for i in range(num_rows // 2):
    row_index1 = i
    row_index2 = num_rows - 1 - i

    # Swap the rows
    rowColSwappedFelix[[row_index1, row_index2], :] = rowColSwappedFelix[[row_index2, row_index1], :]

    # Swap pairs of columns
for i in range(num_columns // 2):
    column_index1 = i
    column_index2 = num_columns - 1 - i

    # Swap the columns
    rowColSwappedFelix[:, [column_index1, column_index2]] = rowColSwappedFelix[:, [column_index2, column_index1]]

rowColSwapFelixImage = Image.fromarray(rowColSwappedFelix.astype('uint8'))
rowColSwapFelixImage = rowColSwapFelixImage.resize((700, 700))
draw = ImageDraw.Draw(rowColSwapFelixImage)

draw.text(label_position, label_text, font=font, fill=label_color )

rowColSwapFelixImage.show()

# Original Felix ===============================================================
label_text = 'F - Original Felix'
originalFelix = felixArray255.copy()

originalFelixImage = Image.fromarray(originalFelix.astype('uint8'))

originalFelixImage = originalFelixImage.resize((700, 700))
draw = ImageDraw.Draw(originalFelixImage)

# Draw the label on the image
draw.text(label_position, label_text, font=font, fill=label_color )

originalFelixImage.show()

# G - Transposed and Column Swapped Felix ======================================
label_text = 'G - Transposed and \n Column Swapped Felix'
transposColSwapFelix = felixArray255.copy()
transposColSwapFelix = np.transpose(transposColSwapFelix)

# Swap pairs of columns
for i in range(num_columns // 2):
    column_index1 = i
    column_index2 = num_columns - 1 - i

    # Swap the columns
    transposColSwapFelix[:, [column_index1, column_index2]] = transposColSwapFelix[:, [column_index2, column_index1]]

transposColFelixImage = Image.fromarray(transposColSwapFelix.astype('uint8'))
transposColFelixImage = transposColFelixImage.resize((700, 700))
draw = ImageDraw.Draw(transposColFelixImage)


# Draw the label on the image
draw.text(label_position, label_text, font=font, fill=label_color )
transposColFelixImage.show()

# H - Transposed and Row Swapped Felix =========================================
label_text = 'H - Transposed and \n Row Swapped Felix'
transposRowSwapFelix = felixArray255.copy()
transposRowSwapFelix = np.transpose(transposRowSwapFelix)

# Swap pairs of rows    
num_rows = transposRowSwapFelix.shape[0]


for i in range(num_rows // 2):
    row_index1 = i
    row_index2 = num_rows - 1 - i

    # Swap the rows
    transposRowSwapFelix[[row_index1, row_index2], :] = transposRowSwapFelix[[row_index2, row_index1], :]

transposRowFelixImage = Image.fromarray(transposRowSwapFelix.astype('uint8'))
transposRowFelixImage = transposRowFelixImage.resize((700, 700))
draw = ImageDraw.Draw(transposRowFelixImage)

draw.text(label_position, label_text, font=font, fill=label_color )
transposRowFelixImage.show()