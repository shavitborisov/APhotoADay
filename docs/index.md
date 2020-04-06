**a Photo a Day Diary**
Project by Jacob Sela and Shavit Borisov
Supervised by Elad Richardson

Code for this project can be found on GitHub

As the new Spring semester started, we have spent most of the first 2 months on studying the material we would later use in this project. Specifically the Stanford convolutional neural network course and the original paper.

Next, we started tool-building and data collecting. We developed a method of downloading and cutting videos; Downloading was based on the youtube-dl tool, and cutting the video into frames was done using opencv.

We tried building a tool for image comparison. This tool, however, was rather rudimentary, using the L0 norm, and was set aside.

Troubleshooting has been a major issue during this time since we have run into technical difficulties quite a few times. These problems mostly had to do with setting up the environment in the lab for the tools we were building.

The next objective is to find a more robust and accurate path for aging in StyleGAN’s latent space. In order to gain some basic intuition, we start by comparing ground truth to an already learned latent direction by Puzer and a simple linear interpolation.

Figure 1
Top row is ground truth, second row is Puzer’s latent direction, and the bottom row is linear interpolation between the first and last photo. Photos were taken at equal intervals over roughly a 2 year period (based on a 10 year time period for the video, first photo is at 2:10, last is at 3:00, the whole video takes 4:20) from age 18 and 5 months to 20 and 5 months.

This shows that on some scale, aging can be approximated linearly, though this proof is a bit contrived, more results are needed, specifically over a larger timescale.

In order to continue experimenting we need more data in the latent space. We downloaded the full video that was used yesterday and cut it into frames. Due to time and computational power limitations, we are only encoding every tenth frame (about every 5 days); even under this limitation the runtime for encoding is currently projected to be 31 hours (after 3 hours of runtime), as of 4:25 pm. The final result will be 780 evenly spaced photos over a 10 year period.

As the photos start trickling in an issue is arising. It seems the encoder has a difficult time handling child and adolescent photos. A few of the results were a bit unsettling. This will narrow down the useable data to that of adults.



Fig 2.1 Original image, frame 1290, age 15
Fig 2.2 Generated image

The next step once all of the latent representations are done is to plot the path of the vectors and to check if and where linearity crumbles on a longer timeframe.


Fig 3 Proposed experiments for linearity of aging. The black path is ground truth, the blue dots would be actual frames encoded into the latent space. The colored paths are possible linear models. A ratio has to be found between the distance of the original points used for interpolation and the accuracy of it.

In order to do this we need to find an empirical tool that decides how good the linear approximation is.

Before beginning developing a tool to carry out the experiments, we first built an automated pipeline for data collection, cleaning, and processing.

Our pipeline downloads a video, chops it into frames, catalogues them, then throws them into the encoder. This tool has made it significantly easier to try new experiments, as most of the manual work that was done beforehand to get usable data has been automated away.

Once this was done, we built a tool to actually carry out the experiments, and to present them nicely. Given a data set, a start age, and an end age, we create a linear interpolation between the two photos in the latent space. In order to test the fidelity of the interpolation, we see how close it gets to various real data points using the formula d=(a-p)-((a-p)⋅n)n, where a is the starting point in the interpolation, p is the point being approximated, and n is the normalized vector between the start and end of the interpolation. Under this formula, p+d is the point on the interpolation line closest to p and is considered to be the interpolation’s approximation for the real value at that age. d’s magnitude (in L2) is the error in the interpolation. Once this is done for all of the data points in the set, we can maybe start to gain some intuition for how reliable of an interpolation we have.


When we carried out experiments, we got strange results that were consistent, but not very precise:



Fig 3.1 The real aging video, subject ages from 16 to almost 22.
Figure 3.2 The generated video


Fig 3.3 The error for every age in the interpolation range. Interpolation started at 5840 days old, and ends at 7940 days old. The error is 0 in the edge cases because the interpolation is based off those points.

The constant nature of the interpolation threw us off, so we conducted another experiment to verify the results, this time with fewer samples as per Elad’s advice.



Fig 4.1 Real aging video. Starts at 15 and ends at 23.
Fig 4.2 Generated video



Fig 4.3 Similar results for the second experiment.

After this we considered that maybe we didn’t detect a bug in the code, but after thorough review, no bug has been found.

These results are unituitive because it doesn’t really make sense that the same point is the closest to all the data points. Additionally, it implies that aging is not at all linear in the latent space.

Further experiments were needed to verify this conjecture and the validity of the tools used. We have added an option to average frames, meaning that given an average ratio, we would use one frame per each set of frames of the average ratio's size. We got similar results here as well (for different ratios).

Next, we checked Puzer's age direction to see its behaviour compared to our interpolation. We used his direction as our interpolator function and got similar results to the previous ones.

This kept repeating over all possible combinations of data, granularity, start age, end age, averaging ratio and interpolation method.

Our conclusion is that there simply is too much noise and/or the feature is still entangled, therefore our next step will be to use a neural network.



We attempted to fit a linear regression model to the problem. We used the regression library from scikit learn. The input/output pairs were of the form:

(start age, latent representation of start image, target age)/latent representation of target image

Giving equal weight to each of the components (i.e. each of the 512*18 + 2 components from the latent vector and the ages). This is most likely not optimal, and greater weight should be given to the age components, but has not yet been.

We decided to train the model as follows; pick the youngest photo for each person and create pairs with that photo as the start photo and any later photo as the target photo (at the end we need to be able to interpolate continuously onto every age so we thought it would be more helpful to show lots of different target results from a single start photo).

Again, likely not the optimal set of data to train on but other options have not been tested. Maybe a different subset of the combinations is superior (or maybe even training on all combinations).

We did the process above for three videos, and then tested the model on one of the videos that we trained on (but different target ages then the ones trained on). The results can be seen below:



Fig 5.1 Real video
Fig 5.2 Generated video (aged from 12 to 24)


Fig 6 MSE over the test data (Same people, different ages from the training data)
The results do look lifelike and are relatively close to what happened in reality but the interpolation fails in aging past what was shown in the video and just continues to grow out the man’s beard.

We then tested the model on brand new cases (namely our own faces). The results can be seen here:


Fig 7.1 Original photo taken
Fig 7.2 Generated video

The model can’t seem to be able to interpolate on faces it hasn’t seen before, instead trying to match them to something learned. We think this is because of a lack of examples and that the solution would be to train the model on many different types of faces (ranging in age, ethnicity, gender, etc.).
