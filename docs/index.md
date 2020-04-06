# A Photo a Day
*Project by Jacob Sela and Shavit Borisov
Supervised by Elad Richardson*

Code for this project can be found on [GitHub](https://github.com/shavitborisov/APhotoADay).

---
As the new Spring semester started, we have spent most of the first 2 months on studying the material we would later use in this project. Specifically the [*Stanford convolutional neural network course*](http://cs231n.github.io/) and the original paper[^3].

Next, we started tool-building and data collecting. We developed a method of downloading and cutting videos; Downloading was based on the [youtube-dl tool](https://ytdl-org.github.io/youtube-dl/index.html), and cutting the video into frames was done using [opencv](https://opencv.org/).

We tried building a tool for image comparison. This tool, however, was rather rudimentary, using the L0 norm, and was set aside.

Troubleshooting has been a major issue during this time since we have run into technical difficulties quite a few times. These problems mostly had to do with setting up the environment in the lab for the tools we were building.

The next objective is to find a more robust and accurate path for aging in **StyleGAN**’s latent space. In order to gain some basic intuition, we start by comparing ground truth to an already learned latent direction by [Puzer](https://github.com/Puzer/stylegan-encoder) (in `Play_with_latent_directions.ipynb`) and a simple linear interpolation.
| ![](https://lh3.googleusercontent.com/luECn19EDoDZz60YzTi2Sn4Na6zhx1cAGFIlwIM9dyYZG3ZpDKtUmY8jVDnaM6bzOIcO1PEENWJyAK2kKCLKY-bPf3wTeCXnyeRDjMefGSaf0ooK9foOJkEcsNMjN53g0Ang0tBl) |
|:---:|
| **Figure 1** Top row is ground truth, second row is Puzer’s latent direction, and the bottom row is linear interpolation between the first and last photo. Photos were taken at equal intervals over roughly a 2 year period (based on a 10 year time period for the video, first photo is at 2:10, last is at 3:00, the whole video takes 4:20) from age 18 and 5 months to 20 and 5 months. Original video can be found [here](https://www.youtube.com/watch?v=zuRd_Eneuk8). |

This shows that on some scale, aging can be approximated linearly, though this proof is a bit contrived, more results are needed, specifically over a larger timescale.

In order to continue experimenting we need more data in the latent space. We downloaded the full video that was used yesterday and cut it into frames. Due to time and computational power limitations, we are only encoding every tenth frame (about every 5 days); even under this limitation the runtime for encoding is currently projected to be 31 hours (after 3 hours of runtime), as of 4:25 pm. The final result will be 780 evenly spaced photos over a 10 year period.

As the photos start trickling in an issue is arising. It seems the encoder has a difficult time handling child and adolescent photos. A few of the results were a bit unsettling. This will narrow down the usable data to that of adults.

| ![](https://lh5.googleusercontent.com/bWx92-0oAT-mLNwyGc3Zscsje2UXfQ7UfevPDgTX9IUYvbPJjMGXnD9FKGbGeuv4zGU6tvLGmB_BeVeteIok-z-Vnb7zmjlhpjkBIVixRig38Agp2__sscamc2tAC9tOprGvZ6mM) | ![](https://lh6.googleusercontent.com/ufjAFjnM2bokYkq_T8Oh6B6T3orrmA39bBSYVHLwHP9GzITHISvTTSZRAzcZVKudETEgBD-3-q1x6MJUIiEhxIpV-bDVWnTQ2_piWwM_Keu9J2WXLCm6zctTe7UCIqd9PrklwE3j) |
|:---:|:---:|
| **Fig 2.1** Original image, frame 1290, age 15. | **Fig 2.2** Generated image. |

The next step once all of the latent representations are done is to plot the path of the vectors and to check if and where linearity crumbles on a longer timeframe.
| ![](https://lh3.googleusercontent.com/rmJUelA2b8ygnc8nJp-Jbjys9hCFIUm1cgU4lNN3xsGu64cxPuaVAx5P6UkXMtJR4KnPIDp3UNPnsLrgMDqqz7LVw2aYCSLR7AmN0aaOiDj-zw9YVVauHwvlfdezOOVDwFbYk8YX) |
|:---:|
| **Fig 3** Proposed experiments for linearity of aging. The black path is ground truth, the blue dots would be actual frames encoded into the latent space. The colored paths are possible linear models. A ratio has to be found between the distance of the original points used for interpolation and the accuracy of it. |

In order to do this we need to find an empirical tool that decides how good the linear approximation is.

Before beginning developing a tool to carry out the experiments, we first built an automated pipeline for data collection, cleaning, and processing.

Our [pipeline](https://github.com/shavitborisov/APhotoADay/blob/master/True_vs_Learned/dataCreator.ipynb) downloads a video, chops it into frames, catalogues them, then throws them into the encoder. This tool has made it significantly easier to try new experiments, as most of the manual work that was done beforehand to get usable data has been automated away.

Once this was done, we built a [tool](https://github.com/shavitborisov/APhotoADay/blob/master/True_vs_Learned/plotLinearityOfAging.ipynb) to actually carry out the experiments, and to [present them nicely](https://github.com/shavitborisov/APhotoADay/blob/master/True_vs_Learned/gifLinearityOfAging.ipynb). Given a data set, a start age, and an end age, we create a linear interpolation between the two photos in the latent space. In order to test the fidelity of the interpolation, we see how close it gets to various real data points using the formula $d=(a-p)-((a-p)⋅n)⋅n$, where $a$ is the starting point in the interpolation, $p$ is the point being approximated, and $n$ is the normalized vector between the start and end of the interpolation. Under this formula, $p+d$ is the point on the interpolation line closest to $p$ and is considered to be the interpolation’s approximation for the real value at that age. $d$’s magnitude (in *L2*) is the error in the interpolation. Once this is done for all of the data points in the set, we can maybe start to gain some intuition for how reliable of an interpolation we have.

When we carried out experiments, we got strange results that were consistent, but not very precise:

| ![](https://lh5.googleusercontent.com/KgYOKeGcuQw0lqniYhaU5j0kzHBZliq7_ab6ts_9ePQR_Mp9ckC96rl13iMvZpcYop4UQlVgt5SCODF9TcwpE0o8URmggpWU1RsMeBQMF7apuzNbO3VNCGLXfUG5Y8tw8USqs53X) | ![](https://lh5.googleusercontent.com/27rB3CfC9L_2uf1E3V-wcfDJOe8J4dl_QPT1ViypJRgzCS67PAcZkRQ-daNBw_WrZvG-pki5-xWVQHSsJPQ10Pv0jEfPxg2dsoyf291uX5ZVYl3nwUjI-E42mPM3A33RRRwY2G_r) |
|:---:|:---:|
| **Fig 3.1** The real aging video, subject ages from 16 to almost 22. | **Figure 3.2** The generated video. |

| ![](https://lh6.googleusercontent.com/l2L3klziXsTgypu_GnUgcQxQfkU-webfqAJtRzALvQCEu3VIiEtskXBpskYkS4pMyGZi1ewqfY7Z7PRSy9KJpqp5STbR1Rfa1AUkSIvvcCvEg51ECIqi7TyDJHhyZ1nr-hoJvk0U) |
|:---:|
| **Fig 3.3** The error for every age in the interpolation range. Interpolation started at 5840 days old, and ends at 7940 days old. The error is 0 in the edge cases because the interpolation is based off those points. |

The constant nature of the interpolation threw us off, so we conducted another experiment to verify the results, this time with fewer samples as per Elad’s advice.

| ![](https://lh6.googleusercontent.com/NshPkolcWTTMc7Av980urs69Ge6ZL9t8eh5IsvXUpTdDMJaAGX-s8FitQ4hkHtoH8J-rScV8-GbxmkNBIZuM1xMIz-GLaa7uDf5kiazgPx2fcqF4peeYQil5duw4nkedhUDLffkV) | ![](https://lh6.googleusercontent.com/tqji2odxhzK2ajco_kOsDIZYdwTuOPa_Q8UZ5XsGaJYXjt5TSCe3kTom3wSqy-7ZeMUgfsuWxcMxvROslOtFTU-w6cT_W4zQREmIZw7SD0i5e3OtgsnnHS5lXYPcMlrq5kxGBOUE) |
|:---:|:---:|
| **Fig 4.1** Real aging video. Starts at 15 and ends at 23. | **Fig 4.2** Generated video. |

| ![](https://lh4.googleusercontent.com/BjQdHUstfTaE9i6S2ltiL8pqblsRa0c3VOa-mMMrrKSl9YidLiaBK-6lGozV1G6kBDNP1ctZEpXceEpmPMSJ4C5SozM6nLVcvyzLL7K_oQhbcj5i30v6-N7fmUWHUT2s_IivTHlq) |
|:---:|
| **Fig 4.3** Similar results for the second experiment. |

After this we considered that maybe we didn’t detect a bug in the code, but after thorough review, no bug has been found.

These results are unituitive because it doesn’t really make sense that the same point is the closest to all the data points. Additionally, it implies that aging is not at all linear in the latent space.

Further experiments were needed to verify this conjecture and the validity of the tools used. We have added an option to average frames, meaning that given an average ratio, we would use one frame per each set of frames of the average ratio's size. We got similar results here as well (for different ratios).

Next, we checked Puzer's age direction to see its behaviour compared to our interpolation. We used his direction as our interpolator function and got similar results to the previous ones.

This kept repeating over all possible combinations of data, granularity, start age, end age, averaging ratio and interpolation method.

Our conclusion is that there simply is too much noise and/or the feature is still entangled, therefore our next step will be to use a neural network.

---

We attempted to fit a linear regression model to the problem. We used the regression library from scikit learn. The input/output pairs were of the form:
`
(start age, latent representation of start image, target age)/latent representation of target image
`.

Giving equal weight to each of the components (i.e. each of the $512*18 + 2$ components from the latent vector and the ages). This is most likely not optimal, and greater weight should be given to the age components, but has not yet been.

We decided to train the model as follows; pick the youngest photo for each person and create pairs with that photo as the start photo and any later photo as the target photo (at the end we need to be able to interpolate continuously onto every age so we thought it would be more helpful to show lots of different target results from a single start photo).

Again, likely not the optimal set of data to train on but other options have not been tested. Maybe a different subset of the combinations is superior (or maybe even training on all combinations).

We did the process above for three videos, and then tested the model on one of the videos that we trained on (but different target ages then the ones trained on). The results can be seen below:
| ![](https://lh6.googleusercontent.com/0bAkodpYtKgdmcBPjUFf2d7ji3ZxhUp-5Xzg5CT4sdiMmvrJU8cjw2WB-scpmQCnNqSR4V9U-cjOOL8f--i1m07JrWmgi_maqOdzdhL5_FF7H82QMuGR78pQZjgc1EmH019D9j10) | ![](https://lh6.googleusercontent.com/CCSlfk0ZUHSe-uj0vGZCf3r_miuyOXd-JRXJoBDWBF2WOLc6c_YxatIh9jKs2lLS7WtSAxtZXyfl0ZMoJaYxCeYiFwPgZ9cEDRuTtFQ79-M7NJe72TyL6kdtfKdNs62QWJPYAQGS) |
|:---:|:---:|
| **Fig 5.1** Real video. | **Fig 5.2** Generated video (aged from 12 to 24). |

| ![](https://lh4.googleusercontent.com/1wxVxvTzsCvb9Q4MEK30w5oU6iW825JYaZqpDVnT1xgQztmkloLDGs7NtFMlC44B7ICO1aihyHaZjtHtUeZoWhRq8-C4j3LjV5gCO-ryUTPdcilsf3TZsWITMYhK_uyho3PadmLm) |
|:---:|
| **Fig 6** MSE over the test data (Same people, different ages from the training data). |

The results do look lifelike and are relatively close to what happened in reality but the interpolation fails in aging past what was shown in the video and just continues to grow out the man’s beard.

We then tested the model on brand new cases (namely our own faces). The results can be seen here:
| ![](https://lh5.googleusercontent.com/2puTuW5CKpWJD7CHTc-E8YcgD0LlOqioCYzAS8mdDTgKo5W6uir04pcV6VsKFdRDN-M3jiW2Ydy5WlJ4S5UvmBNMZEdLytwStFpaTBN5cT6iXzYJ1dLaGGXxukA0zlj80hbksE-F) | ![](https://lh5.googleusercontent.com/gtk0al-JszOGGeojTF_Oy21gd4JX_viL1KhrBMDrSZpoRAHU_6OzcNYp7S1CVSbKpjQV66iOaEm1hJjwhLjnf1x6Pt3efWSQjRrg0LC0OMFIllLnZHDvpEMwX-DCelP9KjwmHqjG) |
|:---:|:---:|
| **Fig 7.1** Jacob's original photo taken. | **Fig 7.2** Generated video. |

The model can’t seem to be able to interpolate on faces it hasn’t seen before, instead trying to match them to something learned. We think this is because of a lack of examples and that the solution would be to train the model on many different types of faces (ranging in age, ethnicity, gender, etc.).

[^3]: Tang, Xu, et al. “*Face Aging with Identity-Preserved Conditional Generative Adversarial Networks.*” 2018 IEEE/CVF Conference on Computer Vision and Pattern Recognition, 2018, doi:10.1109/cvpr.2018.00828.
