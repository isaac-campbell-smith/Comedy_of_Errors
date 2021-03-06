# Comedy of Errors
<img src="https://raw.githubusercontent.com/isaac-campbell-smith/Comedy_of_Errors/master/figs/75610744_1145056039031910_2648101896400666624_o.jpg" width="600">

#### Text Classification for better understanding genre of stand up comedy specials



Data sources: https://scrapsfromtheloft.com/stand-up-comedy-scripts/ | https://imdb.com

---
## Sections:
 |  **[Introduction](#introduction)**  |
 **[Data Scraping & Exploration](#data-scraping-&-exploration)**  |
 **[Transforming the Corpus](#transforming-the-corpus)**  |
 **[Recommender Algorithms](#recommender-algorithms)**  |
 **[Web App](#web-app)**  |
 |  **[Takeaways](#takeaways)**  |
 
---
## Introduction




Stand up comedy is one of the youngest living artforms and I think people still struggle how to talk about it or capture the breadth of what it is. When I first started performing stand up almost 10 years ago, I voraciously consumed as many specials as I could to learn what I liked and study what worked for others. But I noticed a problem in how the platforms I was on were recommending specials to me...

> <i>‘Because you checked out Patton Oswalt’s special about nerd culture and the Bush administration, here’s more stand up to watch - it’s mostly a guy complaining about not getting laid!’ </i>

While Netflix has made some attempts at sub-classifying stand up content on their platform, to me it leaves a lot to be desired and I wanted to see if I could use Natural Language Processing and Machine Learning to gain deeper insights about style and genre in an attempt to improve recommendations.



---
## Data Scraping & Exploration

#### The Transcripts
To start, I scraped about 330 comedy special transcripts from scrapsfromtheloft using the <b>Requests</b> and <b>Beautiful Soup</b> libraries (these scripts can be found in the src folder). After removing a handful of speeches, talk show appearances, and Italian translations, I narrowed my working corpus down to 280 performances. I wasn’t able to obtain solid meta-data to get hard numbers on this but they’re mostly from the last 20 years with the exception of several specials by George Carlin, Richard Pryor, Bill Hicks, Lenny Bruce and Eddie Murphy. There is actually a pretty diverse racial makeup within the collection, but it has only about 30 specials by women, which I unfortunately think is owing more to an historic disparity in comedy than an intentional choice by the website.

The transcriptions are very meticulous which was very appreciated, however there was a lot of tinkering I had to do with word tokenization and choosing what vocabulary to include due to the level precision and amount of speaking 'ticks' that are captured. Here's an excerpt from Patton Oswalt's latest special 'I Love Everything' as an example:

><i>Guys, thank you. Thank you. Please, now just… Everyone. Okay. Oh. Pace yourselves. There’s gonna be some trouble spots later, you can’t just use it up now. I’m gonna need you to fake it hard about three-fourths of the way in. Thank you, guys. Thank you, Charlotte, so much for coming out. All of you guys, thank you. Oh, my God. Whoo! Ah. It’s what… You know, I turned 50 this year and it’s not… And it… You know, I’m not upset about it or… I can’t… Look, I can’t wait to be 90. It’s not that I’m sad that I’m 50. I’m just… This is… These next few decades… Let me just go to 90 now. I wanna be 90, and sit in a chair, and do crossword puzzles, and slowly become racist and die. Like that’s… This is all… I’ve done what I need to do, I’m done. You don’t get to sit down when you’re 50. Now, when you turn 50 in 2019, forget it. People are like,”You’re 50! Well, here’s your mountain bike, you silver fox. Let’s get you out there. We got goji berries and alkaline water. You’ll never die.” Like, let me just… Please, God, sit down. And I thought, “Oh, when I turn 50, there’s gonna be some emotional epiphany, or a physical upheaval, some huge change.” Nothing. You know what happened when I was 50? It was Sunday. That’s what happened, and I had to… go to work the next day. There was… Nothing changed. The one… There was one big change. I will give 50 this. There… The one big change for me was, all of a sudden, my breakfast cereal became deadly serious. Like I… Like, overnight. I remember… Recently, my breakfast cereal was fun. The boxes were bright and there words like “sugar” and “pow” and “crisp” in the name. And then there was, like, an animal mascot… screaming next to a bowl, full of colors insulting to nature. Nothing… Nothing in the visual spectrum went into my body in my 20s and 30s. And you turn the box over, and the fun didn’t stop! You turn the box over, and there was a word find or a maze. A maze! “Help Sugar Bat get to his insulin.” And now… all… of… All of my breakfast cereal… First off, the box… is white. Hospital… white. And there’s a beige bowl. A color of beige I like to call… “bargaining beige.” Like, how many bowls of this do I have to eat, so I can have… one Cool Ranch Dorito at three o’clock today? How many? That many? And inside the beige bowl, brown cereal. Not chocolaty brown. Not fudge brown. As brown as the dirt in the grave that awaits you! And there’s no “sugar” or “pow” or “crisp” in the name. The name is very serious. Sorghum Farms. Sorghum Farms… amaranth flakes. And you turn the box over. Is there a word find? Is there a maze? No. But… there is a short novel about the hippie organic cult farm where they’re growing my amaranth flakes. Paragraph after paragraph of everything you never wanted to know about Sorghum Farms. “At Sorghum Farms, we believe in three simple things: farm-to-table eating, locally sourced ingredients, and giving back to the earth three times what we take away. The idea for Sorghum Farms happened outside of a Phish concert in 1990. We were both… selling tie-dye in the parking lot, and we wondered out loud at the same time why our gorp couldn’t be tastier. And that’s when we both said, ‘Jinx, I owe you a kombucha.’ And we bought a little farm upstate that was built in 15…”</i>

#### The Reviews
I knew I'd need some review data on these specials to flesh out a recommender system. I turned to IMDB for this as it was the only site I could find some. On side note, comedians have been in agreement for years that the traditional long format of a special is somewhat broken and perhaps a better metric to explore would be time spent watching the special. Hopefully I get picked up by Netflix to do that in the future!

I needed to add in <b>Selenium</b> to my initial web-scraping pipeline for this task as there was quite a lot of 'load more' link clicking on some pages to get all the reviews. Suffice to say, I wound up with a very sparse ratings matrix - the density came in at 0.004! 
<br><br>
<img src="https://raw.githubusercontent.com/isaac-campbell-smith/Comedy_of_Errors/master/figs/reviewcounts.png" width="550">
<img src="https://raw.githubusercontent.com/isaac-campbell-smith/Comedy_of_Errors/master/figs/specialcounts.png" width="550">

<br><br>

As far as the actual makeup of these reviews, there are quite a few quirks that I have at least never observed in this area of study, which honestly didn't surprise me. People have very polarized feelings about stand up comedy which made for some interesting trends in recommendation models. 
<br><br>
<img src="https://raw.githubusercontent.com/isaac-campbell-smith/Comedy_of_Errors/master/figs/ratings_distribution.png" width="610">
<img src="https://raw.githubusercontent.com/isaac-campbell-smith/Comedy_of_Errors/master/figs/loved.png" width="315">
<img src="https://raw.githubusercontent.com/isaac-campbell-smith/Comedy_of_Errors/master/figs/hated.png" width="300">
<br>


---
<sub>[  **[Back to Sections](#sections)** ]</sub>

## Transforming the Corpus
After hours of tweaking stopwords and model parameters, the final steps I took to categorize these specials was to tokenize, lemmatize, apply a tfidf vectorizer and a k-means clustering algorithm. I even had to write a script to pull out title information to avoid data leakage - but it's very much a work in progress and merits further experimentation. Choosing which swear words to drop was probably the most tricky to decide, but in the end I only left out 'fuck'. Check out the Clustering Analysis notebook vocabulary section and play around with it if you want to though - to my eye it was the only curse word that didn't bring any meaningful distinguishing characteristics to the clusters.

The success of the results from this process are probably not as apparent without a lot of domain knowledge - as a data sceince peer said when I showed him some of my silhouette plots during this phase of the project, it is not a very good knife plot! But there is actually quite a lot to say about these clusters and it's to be expected that what typically qualifies as 'good' is not going to be obtainable on a project like this owing to the distinct creativity and word count of each performance.

![Knife](https://raw.githubusercontent.com/isaac-campbell-smith/Comedy_of_Errors/master/figs/KnifePlot.png)

As you might expect from those results, there is a lot of overlap in top feature words throughout these clusters, but there are enough degrees of signifance in common words and unique words to make some interpretations about them. Having seen a lot of these specials was probably more helpful though. Here is a snapshot of my current working classification of the corpus (*note I highlighted groups on a 3 point scale indicating the similarity power of these groups - red being strong, orange being somewhat, and yellow being weak):

![Text Clusters](https://raw.githubusercontent.com/isaac-campbell-smith/Comedy_of_Errors/master/figs/text%20analysis.png)


---

## Recommender Algorithms
The recommendation algorithms I looked at were Item Cosine Similarity based on both tfidf and count vectors, User Cosine Similarity, and PySpark’s Alternating Least Squares. As with many recommender systems, this data set struggles to resolve how to recommend specials for users it knows nothing about and for users who have only negatively rated a comedy special.

### Item-Item 
Good at identifying similar specials but has no consideration for quality. I did play around with this model to tweak how it would recommend dissimilar content.

### User-User
Seems to make recommendations across very different genres in general. The cold-start problem is obvious as testing on the dataset produces a lot of null values due to how many users have only rated 1 special. The more interesting problem I discovered was what I call the negative-start problem, which is how to recommend stuff to users that have only rated something negatively. The model does a great job of telling users that they would also rate certain specials poorly, but this isn't all that useful!

### Spark ALS
Similar to User-User in it's weakness but more accurate it seems. This would be a great model to deploy in a live application environment if I had a better working knowledge of managing and updating a database of users.

### Dissimilarity Zombie!
This is the model that I deployed on a live website. It essentially combines the strengths of the User-based recommendations, and fills in its weaknesses based on the different genres I created and recommends dissimilar specials if you did not like a particular show.


---
<sub>[  **[Back to Sections](#sections)** ]</sub>

## Web App

My unscientifically-founded and in-progress solution to these problems is a web app I build using Flask and deployed on AWS, which may or may not be live at the time of reading this. There, you can get some recommendations as a 'first-time user' in IMDB's comedy consumer community based on a comedy special you've seen, regardless of how you liked it. I haven’t had much time to sit down and watch much comedy or get others to engage with the app at the time of this README draft but I strongly believe that it is at least no worse than how suggestions are generated now. Check it out!

http://ec2-54-186-155-75.us-west-2.compute.amazonaws.com/

---

<sub>[  **[Back to Sections](#sections)** ]</sub>


## Takeaways

After all this work, I like the genre groups I've clustered these performances into more than how Netflix groups their stand-up content. The UK comedic tradition is obviously much different than what we're exposed to in America and it's good that they have that tag for related content in their library. As this study shows, the Black American voice in stand-up is also quite a bit different than its White cousin. Our lived experiences lead to differences in creative expression which makes for a much different experience for consumers and these differences are very relevant to what we decide to watch. That Netflix does not include this category in their stand-up content is perplexing, though the variety that consumers are open to as long as the comedian makes them laugh is potentially endless, so it may not ultimately matter. I know I personally have favorite comics falling within every genre I marked. The Anne-Frank and Dirty/Dating groups are probably the weakest conceptually. From a style and voice stand point they're not bad, but in terms of content it's pretty murky. This all goes to show the general weakness of the model though, however I think it's a good starting point of discussion for further analysis of what stand-up comedy is and how we consume it. 