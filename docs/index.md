<span class="c11 c20"></span>

<span class="c11 c20"></span>

<span class="c11 c20"></span>

<span class="c11 c20"></span>

<span class="c11 c20"></span>

<span class="c11 c20">a Photo a Day Diary</span>

<span class="c4">Project by Jacob Sela and Shavit Borisov</span>

<span class="c4">Supervised by Elad Richardson</span>

<span class="c4"></span>

<span class="c7">Code for this project can be found on GitHub</span><sup class="c7">[[1]](#ftnt1)</sup>

* * *

<span class="c7">As the new Spring semester started, we have spent most of the first 2 months on studying the material we would later use in this project. Specifically the Stanford convolutional neural network course</span><sup class="c7">[[2]](#ftnt2)</sup><span class="c7"> and the original paper</span><sup class="c7">[[3]](#ftnt3)</sup><span class="c4">.</span>

<span class="c11 c7"></span>

<span class="c7">Next, we started tool-building and data collecting. We developed a method of downloading and cutting videos; Downloading was based on the youtube-dl</span><sup class="c7">[[4]](#ftnt4)</sup><span class="c7"> tool, and cutting the video into frames was done using opencv</span><sup class="c7">[[5]](#ftnt5)</sup><span class="c4">.</span>

<span class="c4"></span>

<span class="c4">We tried building a tool for image comparison. This tool, however, was rather rudimentary, using the L0 norm, and was set aside.</span>

<span class="c7 c11"></span>

<span class="c4">Troubleshooting has been a major issue during this time since we have run into technical difficulties quite a few times. These problems mostly had to do with setting up the environment in the lab for the tools we were building.</span>

<span class="c4"></span>

<span class="c7">The next objective is to find a more robust and accurate path for aging in StyleGAN’s latent space. In order to gain some basic intuition, we start by comparing ground truth to an already learned latent direction by Puzer</span><sup class="c7">[[6]](#ftnt6)</sup><span class="c7"> and a simple linear interpolation.</span>

* * *

<span class="c4"></span>

<a id="t.3b66e767568ab90736b15999d80047ccc6a03f88"></a><a id="t.0"></a>

<table class="c12">

<tbody>

<tr class="c22">

<td class="c25" colspan="1" rowspan="1">

<span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 578.00px; height: 298.00px;">![](images/image20.png)</span>

</td>

</tr>

<tr class="c22">

<td class="c25" colspan="1" rowspan="1">

<span class="c15">Figure 1</span><sup class="c15">[[7]](#ftnt7)</sup>

<span class="c4">Top row is ground truth, second row is Puzer’s latent direction, and the bottom row is linear interpolation between the first and last photo. Photos were taken at equal intervals over roughly a 2 year period (based on a 10 year time period for the video, first photo is at 2:10, last is at 3:00, the whole video takes 4:20) from age 18 and 5 months to 20 and 5 months.</span>

</td>

</tr>

</tbody>

</table>

<span class="c4"></span>

<span class="c4">This shows that on some scale, aging can be approximated linearly, though this proof is a bit contrived, more results are needed, specifically over a larger timescale.</span>

<span class="c4"></span>

<span class="c4">In order to continue experimenting we need more data in the latent space. We downloaded the full video that was used yesterday and cut it into frames. Due to time and computational power limitations, we are only encoding every tenth frame (about every 5 days); even under this limitation the runtime for encoding is currently projected to be 31 hours (after 3 hours of runtime), as of 4:25 pm. The final result will be 780 evenly spaced photos over a 10 year period.</span>

<span class="c4"></span>

<span class="c4">As the photos start trickling in an issue is arising. It seems the encoder has a difficult time handling child and adolescent photos. A few of the results were a bit unsettling. This will narrow down the useable data to that of adults.</span>

<span class="c4"></span>

<a id="t.6dc9ecd1f05997084a3b78f8e52604ebe08bbf17"></a><a id="t.1"></a>

<table class="c28">

<tbody>

<tr class="c22">

<td class="c19" colspan="1" rowspan="1">

<span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 298.00px; height: 298.67px;">![](images/image13.png)</span>

</td>

<td class="c19" colspan="1" rowspan="1">

<span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 298.00px; height: 298.67px;">![](images/image17.png)</span>

</td>

</tr>

<tr class="c22">

<td class="c19" colspan="1" rowspan="1">

<span class="c15">Fig 2.1</span><span class="c4"> Original image, frame 1290, age 15</span>

</td>

<td class="c19" colspan="1" rowspan="1">

<span class="c15">Fig 2.2</span> <span class="c4">Generated image</span>

</td>

</tr>

</tbody>

</table>

<span class="c4"></span>

<span class="c4">The next step once all of the latent representations are done is to plot the path of the vectors and to check if and where linearity crumbles on a longer timeframe.</span>

<span class="c4"></span>

<a id="t.ae6c69e451a04bb68d280ff2886a8cfa0e4ba09c"></a><a id="t.2"></a>

<table class="c12">

<tbody>

<tr class="c22">

<td class="c30" colspan="1" rowspan="1">

<span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 298.00px; height: 278.67px;">![](images/image10.png)</span>

</td>

<td class="c31" colspan="1" rowspan="1">

<span class="c15">Fig 3</span><span class="c4"> Proposed experiments for linearity of aging. The black path is ground truth, the blue dots would be actual frames encoded into the latent space. The colored paths are possible linear models. A ratio has to be found between the distance of the original points used for interpolation and the accuracy of it.</span>

</td>

</tr>

</tbody>

</table>

<span class="c4"></span>

<span class="c4">In order to do this we need to find an empirical tool that decides how good the linear approximation is.</span>

* * *

<span class="c4"></span>

<span class="c4">Before beginning developing a tool to carry out the experiments, we first built an automated pipeline for data collection, cleaning, and processing.</span>

<span class="c4"></span>

<span class="c7">Our pipeline</span><sup class="c7">[[8]](#ftnt8)</sup><span class="c7"> downloads a video, chops it into frames, catalogues them, then throws them into the encoder. This tool has made it significantly easier to try new experiments, as most of the manual work that was done beforehand to get usable data has been automated away.</span>

<span class="c4"></span>

<span class="c7">Once this was done, we built a tool to actually carry out the experiments</span><sup class="c7">[[9]](#ftnt9)</sup><span class="c7">, and to present them nicely</span><sup class="c7">[[10]](#ftnt10)</sup><span class="c7">. Given a data set, a start age, and an end age, we create a linear interpolation between the two photos in the latent space. In order to test the fidelity of the interpolation, we see how close it gets to various real data points using the formula</span> ![](images/image1.png)<span class="c7">, where</span> ![](images/image2.png)<span class="c7">is the starting point in the interpolation,</span> ![](images/image3.png)<span class="c7">is the point being approximated, and</span> ![](images/image4.png)<span class="c7">is the normalized vector between the start and end of the interpolation. Under this formula,</span> ![](images/image5.png)<span class="c7">is the point on the interpolation line closest to</span> ![](images/image3.png)<span class="c7">and is considered to be the interpolation’s approximation for the real value at that age.</span> ![](images/image6.png)<span class="c7">’s magnitude (in</span> ![](images/image7.png)<span class="c4">) is the error in the interpolation. Once this is done for all of the data points in the set, we can maybe start to gain some intuition for how reliable of an interpolation we have.</span>

<span class="c4"></span>

* * *

<span class="c4"></span>

<span class="c4">When we carried out experiments, we got strange results that were consistent, but not very precise:</span>

<span class="c4"></span>

<a id="t.b22acf102494f0c3f596595833d36588fdf53e7c"></a><a id="t.3"></a>

<table class="c12">

<tbody>

<tr class="c22">

<td class="c16" colspan="1" rowspan="1">

<span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 1.33px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 298.00px; height: 298.67px;">![](images/image11.gif)</span>

</td>

<td class="c16" colspan="1" rowspan="1">

<span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 1.33px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 298.00px; height: 298.67px;">![](images/image8.gif)</span>

</td>

</tr>

<tr class="c22">

<td class="c16" colspan="1" rowspan="1">

<span class="c15">Fig 3.1</span><span class="c4"> The real aging video, subject ages from 16 to almost 22.</span>

</td>

<td class="c16" colspan="1" rowspan="1">

<span class="c15">Figure 3.2</span> <span class="c4">The generated video</span>

</td>

</tr>

</tbody>

</table>

<span class="c4"></span>

<a id="t.e69e8c064cbcff7f6587576c51569057b765bfd2"></a><a id="t.4"></a>

<table class="c12">

<tbody>

<tr class="c22">

<td class="c25" colspan="1" rowspan="1">

<span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 432.00px; height: 288.00px;">![](images/image16.jpg)</span>

</td>

</tr>

<tr class="c22">

<td class="c25" colspan="1" rowspan="1">

<span class="c15">Fig 3.3</span><span class="c4"> The error for every age in the interpolation range. Interpolation started at 5840 days old, and ends at 7940 days old. The error is 0 in the edge cases because the interpolation is based off those points.</span>

</td>

</tr>

</tbody>

</table>

<span class="c4"></span>

<span class="c4">The constant nature of the interpolation threw us off, so we conducted another experiment to verify the results, this time with fewer samples as per Elad’s advice.</span>

<span class="c4"></span>

<a id="t.77df8aebb9ffef7140da7f63d9fe925d5eb2257a"></a><a id="t.5"></a>

<table class="c12">

<tbody>

<tr class="c23">

<td class="c16" colspan="1" rowspan="1">

<span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 1.33px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 298.00px; height: 298.67px;">![](images/image21.gif)</span>

</td>

<td class="c16" colspan="1" rowspan="1">

<span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 1.33px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 298.00px; height: 298.67px;">![](images/image15.gif)</span>

</td>

</tr>

<tr class="c22">

<td class="c16" colspan="1" rowspan="1">

<span class="c15">Fig 4.1</span><span class="c4"> Real aging video. Starts at 15 and ends at 23.</span>

</td>

<td class="c16" colspan="1" rowspan="1">

<span class="c15">Fig 4.2</span><span class="c4"> Generated video</span>

</td>

</tr>

</tbody>

</table>

<span class="c4"></span>

<span class="c4"></span>

<a id="t.9359ce9341f649245652cf566675a56e0d8226f9"></a><a id="t.6"></a>

<table class="c12">

<tbody>

<tr class="c22">

<td class="c25" colspan="1" rowspan="1">

<span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 432.00px; height: 288.00px;">![](images/image18.jpg)</span>

</td>

</tr>

<tr class="c22">

<td class="c25" colspan="1" rowspan="1">

<span class="c15">Fig 4.3</span> <span class="c4">Similar results for the second experiment.</span>

</td>

</tr>

</tbody>

</table>

<span class="c4"></span>

<span class="c4">After this we considered that maybe we didn’t detect a bug in the code, but after thorough review, no bug has been found.</span>

<span class="c4"></span>

<span class="c4">These results are unituitive because it doesn’t really make sense that the same point is the closest to all the data points. Additionally, it implies that aging is not at all linear in the latent space.</span>

<span class="c4"></span>

<span class="c4">Further experiments were needed to verify this conjecture and the validity of the tools used. We have added an option to average frames, meaning that given an average ratio, we would use one frame per each set of frames of the average ratio's size. We got similar results here as well (for different ratios).</span>

<span class="c4"></span>

<span class="c4">Next, we checked Puzer's age direction to see its behaviour compared to our interpolation. We used his direction as our interpolator function and got similar results to the previous ones.</span>

<span class="c4"></span>

<span class="c4">This kept repeating over all possible combinations of data, granularity, start age, end age, averaging ratio and interpolation method.</span>

<span class="c4"></span>

<span class="c4">Our conclusion is that there simply is too much noise and/or the feature is still entangled, therefore our next step will be to use a neural network.</span>

<span class="c4"></span>

* * *

<span class="c4"></span>

<span class="c4"></span>

<span class="c4">We attempted to fit a linear regression model to the problem. We used the regression library from scikit learn. The input/output pairs were of the form:</span>

<span class="c4"></span>

<span class="c17 c8 c18">(start age, latent representation of start image, target age)/latent representation of target image</span>

<span class="c4"></span>

<span class="c4">Giving equal weight to each of the components (i.e. each of the 512*18 + 2 components from the latent vector and the ages). This is most likely not optimal, and greater weight should be given to the age components, but has not yet been.</span>

<span class="c4"></span>

<span class="c4">We decided to train the model as follows; pick the youngest photo for each person and create pairs with that photo as the start photo and any later photo as the target photo (at the end we need to be able to interpolate continuously onto every age so we thought it would be more helpful to show lots of different target results from a single start photo).</span>

<span class="c4"></span>

<span class="c4">Again, likely not the optimal set of data to train on but other options have not been tested. Maybe a different subset of the combinations is superior (or maybe even training on all combinations).</span>

<span class="c4"></span>

<span class="c4">We did the process above for three videos, and then tested the model on one of the videos that we trained on (but different target ages then the ones trained on). The results can be seen below:</span>

<span class="c4"></span>

<a id="t.f5a33ca31dc5cefb892dff8129b5dca3bb4e3880"></a><a id="t.7"></a>

<table class="c12">

<tbody>

<tr class="c23">

<td class="c16" colspan="1" rowspan="1">

<span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 298.00px; height: 298.67px;">![](images/image19.gif)</span>

</td>

<td class="c16" colspan="1" rowspan="1">

<span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 298.00px; height: 298.67px;">![](images/image12.gif)</span>

</td>

</tr>

<tr class="c22">

<td class="c16" colspan="1" rowspan="1">

<span class="c15">Fig 5.1</span><span class="c4"> Real video</span>

</td>

<td class="c16" colspan="1" rowspan="1">

<span class="c15">Fig 5.2</span><span class="c4"> Generated video (aged from 12 to 24)</span>

</td>

</tr>

</tbody>

</table>

<span class="c4"></span>

<a id="t.48da68647e5cbee523442ebcf5e89d72039cdaf0"></a><a id="t.8"></a>

<table class="c12">

<tbody>

<tr class="c22">

<td class="c25" colspan="1" rowspan="1">

<span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 432.00px; height: 288.00px;">![](images/image9.png)</span>

</td>

</tr>

<tr class="c22">

<td class="c25" colspan="1" rowspan="1">

<span class="c15">Fig 6</span> <span class="c4">MSE over the test data (Same people, different ages from the training data)</span>

</td>

</tr>

</tbody>

</table>

<span class="c4">The results do look lifelike and are relatively close to what happened in reality but the interpolation fails in aging past what was shown in the video and just continues to grow out the man’s beard.</span>

<span class="c4"></span>

<span class="c4">We then tested the model on brand new cases (namely our own faces). The results can be seen here:</span>

<a id="t.db51ac1696090247f3c40cf463405eeb6691e3ef"></a><a id="t.9"></a>

<table class="c12">

<tbody>

<tr class="c23">

<td class="c16" colspan="1" rowspan="1">

<span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 298.00px; height: 301.00px;">![](images/image22.jpg)</span>

</td>

<td class="c16" colspan="1" rowspan="1">

<span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 298.00px; height: 298.67px;">![](images/image14.gif)</span>

</td>

</tr>

<tr class="c22">

<td class="c16" colspan="1" rowspan="1">

<span class="c15">Fig 7.1</span><span class="c4"> Original photo taken</span>

</td>

<td class="c16" colspan="1" rowspan="1">

<span class="c15">Fig 7.2</span><span class="c4"> Generated video</span>

</td>

</tr>

</tbody>

</table>

<span class="c4"></span>

<span class="c7">The model can’t seem to be able to interpolate on faces it hasn’t seen before, instead trying to match them to something learned. We think this is because of a lack of examples and that the solution would be to train the model on many different types of faces (ranging in age, ethnicity, gender, etc.).</span>

<div>

<span class="c17 c24"></span>

</div>

* * *

<div>

[[1]](#ftnt_ref1)<span class="c8"> </span><span class="c14 c8">[https://github.com/shavitborisov/APhotoADay](https://www.google.com/url?q=https://github.com/shavitborisov/APhotoADay&sa=D&ust=1586178290855000)</span>

</div>

<div>

[[2]](#ftnt_ref2)<span class="c8"> </span><span class="c14 c8">[http://cs231n.github.io/](https://www.google.com/url?q=http://cs231n.github.io/&sa=D&ust=1586178290850000)</span>

</div>

<div>

[[3]](#ftnt_ref3)<span class="c8"> </span><span class="c21 c8">Tang, Xu, et al. “Face Aging with Identity-Preserved Conditional Generative Adversarial Networks.”</span> <span class="c8 c27">2018 IEEE/CVF Conference on Computer Vision and Pattern Recognition</span><span class="c8 c21">, 2018, doi:10.1109/cvpr.2018.00828.</span>

</div>

<div>

[[4]](#ftnt_ref4)<span class="c8"> </span><span class="c8 c14">[https://ytdl-org.github.io/youtube-dl/index.html](https://www.google.com/url?q=https://ytdl-org.github.io/youtube-dl/index.html&sa=D&ust=1586178290850000)</span>

</div>

<div>

[[5]](#ftnt_ref5)<span class="c8"> </span><span class="c14 c8">[https://opencv.org/](https://www.google.com/url?q=https://opencv.org/&sa=D&ust=1586178290854000)</span>

</div>

<div>

[[6]](#ftnt_ref6)<span class="c8"> </span><span class="c14 c8">[https://github.com/Puzer/stylegan-encoder](https://www.google.com/url?q=https://github.com/Puzer/stylegan-encoder&sa=D&ust=1586178290848000)</span><span class="c8">, in</span> <span class="c29">[Play_with_latent_directions.ipynb](https://www.google.com/url?q=https://github.com/Puzer/stylegan-encoder/blob/master/Play_with_latent_directions.ipynb&sa=D&ust=1586178290849000)</span>

</div>

<div>

[[7]](#ftnt_ref7)<span class="c8">Original video:</span> <span class="c14 c8">[https://www.youtube.com/watch?v=zuRd_Eneuk8](https://www.google.com/url?q=https://www.youtube.com/watch?v%3DzuRd_Eneuk8&sa=D&ust=1586178290849000)</span>

</div>

<div>

[[8]](#ftnt_ref8)<span class="c8"> </span><span class="c14 c8">[https://github.com/shavitborisov/APhotoADay/blob/master/True_vs_Learned/dataCreator.ipynb](https://www.google.com/url?q=https://github.com/shavitborisov/APhotoADay/blob/master/True_vs_Learned/dataCreator.ipynb&sa=D&ust=1586178290856000)</span>

</div>

<div>

[[9]](#ftnt_ref9)<span class="c8"> </span><span class="c14 c8">[https://github.com/shavitborisov/APhotoADay/blob/master/True_vs_Learned/plotLinearityOfAging.ipynb](https://www.google.com/url?q=https://github.com/shavitborisov/APhotoADay/blob/master/True_vs_Learned/plotLinearityOfAging.ipynb&sa=D&ust=1586178290856000)</span>

</div>

<div>

[[10]](#ftnt_ref10)<span class="c8"> </span><span class="c14 c8">[https://github.com/shavitborisov/APhotoADay/blob/master/True_vs_Learned/gifLinearityOfAging.ipynb](https://www.google.com/url?q=https://github.com/shavitborisov/APhotoADay/blob/master/True_vs_Learned/gifLinearityOfAging.ipynb&sa=D&ust=1586178290857000)</span>

</div>
