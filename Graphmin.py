import matplotlib.pyplot as plt

# Define the image names and corresponding minutiae points
image_names = [
    '101_1.tif', '101_2.tif', '101_3.tif', '101_4.tif', '101_5.tif',
    '101_6.tif', '101_7.tif', '101_8.tif', '102_1.tif', '102_2.tif',
    '102_3.tif', '102_4.tif', '102_5.tif', '102_6.tif', '102_7.tif',
    '102_8.tif', '103_1.tif', '103_2.tif', '103_3.tif', '103_4.tif',
    '103_5.tif', '103_6.tif', '103_7.tif', '103_8.tif', '104_1.tif',
    '104_2.tif', '104_3.tif', '104_4.tif', '104_5.tif', '104_6.tif',
    '104_7.tif', '104_8.tif', '105_1.tif', '105_2.tif', '105_3.tif',
    '105_4.tif', '105_5.tif', '105_6.tif', '105_7.tif', '105_8.tif',
    '106_1.tif', '106_2.tif', '106_3.tif', '106_4.tif', '106_5.tif',
    '106_6.tif', '106_7.tif', '106_8.tif', '107_1.tif', '107_2.tif',
    '107_3.tif', '107_4.tif', '107_5.tif', '107_6.tif', '107_7.tif',
    '107_8.tif', '108_1.tif', '108_2.tif', '108_3.tif', '108_4.tif',
    '108_5.tif', '108_6.tif', '108_7.tif', '108_8.tif', '109_1.tif',
    '109_2.tif', '109_3.tif', '109_4.tif', '109_5.tif', '109_6.tif',
    '109_7.tif', '109_8.tif', '110_1.tif', '110_2.tif', '110_3.tif',
    '110_4.tif', '110_5.tif', '110_6.tif', '110_7.tif', '110_8.tif'
]

minutiae_points = [
    480, 409, 517, 59, 44, 708, 760, 192, 435, 540,
    384, 382, 196, 781, 166, 105, 578, 566, 458, 356,
    401, 575, 429, 155, 445, 581, 501, 576, 467, 498,
    645, 167, 602, 384, 350, 285, 418, 326, 718, 106,
    575, 602, 542, 473, 625, 530, 519, 225, 239, 272,
    243, 346, 358, 650, 626, 47, 343, 323, 298, 448,
    191, 580, 420, 348, 82, 162, 44, 68, 79, 20,
    422, 20, 134, 136, 88, 97, 140, 178, 532, 104
]

# Create the graph
plt.bar(range(len(minutiae_points)), minutiae_points, align='center')
plt.xticks(range(len(minutiae_points)), image_names, rotation=90)
plt.xlabel('Image')
plt.ylabel('Number of Minutiae Points')
plt.title('Minutiae Points for Each Image')
plt.tight_layout()
plt.show()
