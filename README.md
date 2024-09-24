This repository consists the files for Fingerprint Quality evaluation project.

The contents are-

Quality2.py
Figure_1.png
Figure_2.png
Fin_score_fig.png
FinalScoreDB1.txt
Graph.py
Graphfinscore.py
Graphmin.py
Minutia points info.txt


The code lies in Quality2.py

We used two functions, one for each parameter(blur and minutia points). The functions are to calculate respective values. We used opencv library for image processing.

The blur function uses the laplacian kernel or matrix to calculate the variance between edges. The Laplacian kernel is multiplied with every pixel in the image to 
give The result is a black and white image with variance between edges. The var() calculates the average variance in the image. The higher the variance the clearer the
image and vice-versa. It returns the blur value or the laplacian value for each image.

The Minutia detection function uses thresholding to seperate the foreground(edges or ridges in the image) and the background. Otsu's method is used for thresholding. 
it maximizes variance between the foreground and background. The ridges become black and the background becomes white as a result. Then we reverse the values, making 
white as black and black as white. The image is also converted to a binary image beofre the process. 

Both these functions return their respective values. These values are then given a rating as per the clarity and quality in the third function which calculates the score.

We used a sample size of  80 fingreprint samples. The scores of which are present in FinalScoreDB1.txt.

The individual and final scores of each image have been plotted as graphs for easy and better understanding of the results. 

Graph.py contains code for Laplcian values or blur values, the graph is in Figure_1.png
Graphmin.py contains code for the no. of minutia points for each image, the graph is Figure_2.png
The final score is plotted as per the code in Graphfinscore.png and the graph is in Fin_score_fig.png

Entire project was done using python and existing open libraries. Most of the information pertaining to the project such as the concepts for the codes, fingerprint samples 
and so on were sourced from the net and from sources from the professor incharge of the project. The code was written to be simple and as precise as can be possible by students.

