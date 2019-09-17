# EDA-using-MapReduce

This project - Data Aggregation, Big Data Analysis and Visualization - involves: <br>
1. Data Aggregation from multiple sources using the APIs exposed <br>
2. Applying classical big data analytic method of MapReduce to the unstructured data collected <br>
3. Store the data collected on WORM infrastructure Hadoop <br>
4. Build a visualization data product <br>


### Goals

1. Source data from Twitter, NYT and CommonCrawl <br>
2. Use MapReduce for word count and word co-occurrence <br>
3. Data visualization using Tableau


### Directory Structure

. <br>
|- part 1 <br>
|--- code : codes for souring twitter,nyt,commmoncrawl data. <br>
|--- data : <br>
|----- twitter <br>
|----- nyt <br>
|----- commoncrawl <br>
| <br>
|- part 2 <br>
|--- code : MapReduce code for word count <br>
|--- result : output of MapReduce output <br>
| <br>
|- part 3 <br>
|--- Twitter <br>
|----- code : <br>
|------- wordcount : MR code for word count <br>
|------- topN : MR code for listing top 10 words <br>
|------- word Cooccurence : MR code <br>
|------- topN word Cooccurence : MR code for listing top 10 word pairs <br>
|----- images : images of tableau visualization of twitter data <br>
|--- NYT	<br>
|----- code: <br>
|------- wordcount : MR code for word count <br>
|------- topN : MR code for listing top 10 words <br>
|------- word Cooccurence : MR code <br>
|------- topN word Cooccurence : MR code for listing top 10 word pairs <br>
|----- images : images of tableau visualization of NYT data <br>
|--- Commoncrawl	<br>
|----- code: <br>
|------- wordcount : MR code for word count <br>
|------- topN : MR code for listing top 10 words <br>
|------- word Cooccurence : MR code <br>
|------- topN word Cooccurence : MR code for listing top 10 word pairs <br>
|----- images : images of tableau visualization of Common crawl data data <br>
| <br>
|- ReadMe.txt <br>
| <br>
|- Report.pdf <br>
| <br>
|- video.mp4 <br>

<br>

### Wordcloud generated with Tableau
![](part3/Commoncrawl/Images/cc_coo.png)
