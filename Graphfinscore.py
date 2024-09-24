import matplotlib.pyplot as plt

# image scores
image_scores = [
    30, 30, 30, 10, 10, 40, 40, 10,  # Image scores for 101_1.tif to 101_8.tif
    30, 30, 20, 20, 10, 40, 10, 10,  # Image scores for 102_1.tif to 102_8.tif
    30, 30, 30, 20, 30, 30, 30, 10,  # Image scores for 103_1.tif to 103_8.tif
    30, 30, 30, 30, 30, 30, 40, 10,  # Image scores for 104_1.tif to 104_8.tif
    40, 20, 20, 20, 30, 20, 40, 10,  # Image scores for 105_1.tif to 105_8.tif
    30, 40, 30, 30, 40, 30, 30, 20,  # Image scores for 106_1.tif to 106_8.tif
    20, 20, 20, 20, 20, 40, 40, 10,  # Image scores for 107_1.tif to 107_8.tif
    20, 20, 20, 30, 10, 30, 30, 20,  # Image scores for 108_1.tif to 108_8.tif
    10, 10, 10, 10, 10, 10, 30, 10,  # Image scores for 109_1.tif to 109_8.tif
    10, 10, 10, 10, 10, 10, 30, 10,  # Image scores for 110_1.tif to 110_8.tif
]

# x-axis labels for images
image_labels = [f"Image {i+1}" for i in range(len(image_scores))]

# bar chart
plt.figure(figsize=(10, 6))
plt.bar(image_labels, image_scores)
plt.xlabel("Image")
plt.ylabel("Total Score")
plt.title("Total Score of Images")
plt.xticks(rotation=90)
plt.tight_layout()

# the chart
plt.show()
