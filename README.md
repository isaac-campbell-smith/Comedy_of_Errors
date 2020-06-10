# Comedy of Errors

#### Text Classification for better understanding genre of stand up comedy specials

Data sources: https://scrapsfromtheloft.com/stand-up-comedy-scripts/ | https://imdb.com

---
## Sections:
 |  **[Introduction](#introduction)**  |
 **[Data Scraping & Exploration](#data-scraping-&-exploration)**  |
 **[Transforming the Corpus](#transforming-the-corpus)**  |
 **[Cost Benefit & Scoring Metrics](#cost-benefit-&-scoring-metrics)**  |
 **[The Models](#the-models)**  |
 **[Analysis](#analysis)**  |
 |  **[Takeaways](#takeaways)**  |
 
---
## Introduction
Stand up comedy is one of the youngest living artforms and I think people still struggle how to talk about it or capture the breadth of what it is. When I first started performing stand up almost 10 years ago, I voraciously consumed as many specials as I could to learn what I liked and study what worked for others. But I noticed a problem in how the platforms I was on were recommending specials to me...

> <i>‘Because you checked out Patton Oswalt’s special about nerd culture and the Bush administration, here’s more stand up to watch - it’s mostly a guy complaining about not getting laid!’ </i>

While Netflix has made some attempts at sub-classifying stand up content on their platform, to me it leaves a lot to be desired and I wanted to see if I could use Natural Language Processing and Machine Learning to gain deeper insights about style and genre in an attempt to improve recommendations.


![ME](https://raw.githubusercontent.com/isaac-campbell-smith/BernoulliTrials_and_Tribulations/master/visuals/FraudvsNot.png)

---
## Data Scraping & Exploration

#### The Transcripts
To start, I scraped about 330 comedy special transcripts from scrapsfromtheloft using the <b>Requests</b> and <b>Beautiful Soup</b> libraries (these scripts can be found in the src folder). After removing a handful of speeches, talk show appearances, and Italian translations, I narrowed my working corpus down to 280 performances. I wasn’t able to obtain solid meta-data to get hard numbers on this but they’re mostly from the last 20 years with the exception of several specials by George Carlin, Richard Pryor, Bill Hicks, Lenny Bruce and Eddie Murphy. There is actually a pretty diverse racial makeup within the collection, but it has only about 30 specials by women, which I unfortunately think is owing more to an historic disparity in comedy than an intentional choice by the website.

The transcriptions are very meticulous which was very appreciated, however there was a lot of tinkering I had to do with word tokenization and choosing what vocabulary to include due to the level precision and amount of speaking 'ticks' that are captured. Here's an excerpt from Patton Oswalt's latest special 'I Love Everything' as an example:

><i>Guys, thank you. Thank you. Please, now just… Everyone. Okay. Oh. Pace yourselves. There’s gonna be some trouble spots later, you can’t just use it up now. I’m gonna need you to fake it hard about three-fourths of the way in. Thank you, guys. Thank you, Charlotte, so much for coming out. All of you guys, thank you. Oh, my God. Whoo! Ah. It’s what… You know, I turned 50 this year and it’s not… And it… You know, I’m not upset about it or… I can’t… Look, I can’t wait to be 90. It’s not that I’m sad that I’m 50. I’m just… This is… These next few decades… Let me just go to 90 now. I wanna be 90, and sit in a chair, and do crossword puzzles, and slowly become racist and die. Like that’s… This is all… I’ve done what I need to do, I’m done. You don’t get to sit down when you’re 50. Now, when you turn 50 in 2019, forget it. People are like,”You’re 50! Well, here’s your mountain bike, you silver fox. Let’s get you out there. We got goji berries and alkaline water. You’ll never die.” Like, let me just… Please, God, sit down. And I thought, “Oh, when I turn 50, there’s gonna be some emotional epiphany, or a physical upheaval, some huge change.” Nothing. You know what happened when I was 50? It was Sunday. That’s what happened, and I had to… go to work the next day. There was… Nothing changed. The one… There was one big change. I will give 50 this. There… The one big change for me was, all of a sudden, my breakfast cereal became deadly serious. Like I… Like, overnight. I remember… Recently, my breakfast cereal was fun. The boxes were bright and there words like “sugar” and “pow” and “crisp” in the name. And then there was, like, an animal mascot… screaming next to a bowl, full of colors insulting to nature. Nothing… Nothing in the visual spectrum went into my body in my 20s and 30s. And you turn the box over, and the fun didn’t stop! You turn the box over, and there was a word find or a maze. A maze! “Help Sugar Bat get to his insulin.” And now… all… of… All of my breakfast cereal… First off, the box… is white. Hospital… white. And there’s a beige bowl. A color of beige I like to call… “bargaining beige.” Like, how many bowls of this do I have to eat, so I can have… one Cool Ranch Dorito at three o’clock today? How many? That many? And inside the beige bowl, brown cereal. Not chocolaty brown. Not fudge brown. As brown as the dirt in the grave that awaits you! And there’s no “sugar” or “pow” or “crisp” in the name. The name is very serious. Sorghum Farms. Sorghum Farms… amaranth flakes. And you turn the box over. Is there a word find? Is there a maze? No. But… there is a short novel about the hippie organic cult farm where they’re growing my amaranth flakes. Paragraph after paragraph of everything you never wanted to know about Sorghum Farms. “At Sorghum Farms, we believe in three simple things: farm-to-table eating, locally sourced ingredients, and giving back to the earth three times what we take away. The idea for Sorghum Farms happened outside of a Phish concert in 1990. We were both… selling tie-dye in the parking lot, and we wondered out loud at the same time why our gorp couldn’t be tastier. And that’s when we both said, ‘Jinx, I owe you a kombucha.’ And we bought a little farm upstate that was built in 15…”</i>

#### The Reviews
I knew I'd need some review data on these specials to flesh out a recommender system. I turned to IMDB for this as it was the only site I could find some. On side note, comedians have been in agreement for years that the traditional long format of a special is somewhat broken and perhaps a better metric to explore would be time spent watching the special. Hopefully I get picked up by Netflix to do that in the future!

I needed to add in <b>Selenium</b> to my initial web-scraping pipeline for this task as there was quite a lot of clicking links on pages to get all the reviews. 
![Original Dataset](https://raw.githubusercontent.com/isaac-campbell-smith/BernoulliTrials_and_Tribulations/master/visuals/head.png)

![Original Describe](https://raw.githubusercontent.com/isaac-campbell-smith/BernoulliTrials_and_Tribulations/master/visuals/Describe.png)


---
<sub>[  **[Back to Sections](#sections)** ]</sub>

## Transforming the Corpus
After hours of tweaking stopwords and model parameters, the final steps I took to categorize these specials was to tokenize, lemmatize, apply a tfidf vectorizer and a k-means clustering algorithm. I even had to write a script to pull out title information to avoid data leakage. Choosing which swear words to drop was probably the most tricky to decide, but in the end I only left out 'fuck'. Check out the Clustering Analysis notebook vocabulary section and play around with it if you want to though - to my eye it was the only curse word that didn't bring any meaningful distinguishing characteristics to the clusters.

The success of these results from this process are probably not as apparent without a good amount of domain knowledge - as a data ssaid when I showed him some of my silhouette plots during the project, this is not a very good knife plot! But there is actually quite a lot to say about these clusters.

![Knife](https://raw.githubusercontent.com/isaac-campbell-smith/Comedy_of_Errors/master/figs/KnifePlot.png)

#### FEATURES
Better features make for better predictions. That isn't the most sophisticated statement but building a reliable model with this data is extremely challenging because we can't say for sure what these variables are and how they interact without a lot of highly idividualized regression analysis (which I have not done a lot of!). I took 2 wildly different approaches to varying results.

1. OneHotEncode Field1. This seemed to me the most likely non-binary categorical feature. I applied a MinMaxScaler to Field3 to account for negative and zero values. I squared and took the log of field4 because it seemed to have a strong influence on classification and I think it needed to be mellowed out. I also took the log of zip, account ID, and the square root of amount.

2. OneHotEncode everything. Literally everything. This was super computationally expensive and I could only get it to run through an XGBoosting algorithm. 


---

## The Models
### Random & Isolated Forest Classifiers
Random Forests are great out of the box generally but they only performed OK in this case! Isolated Forests are a bit different because it uses unsupervised learning algorithms to look for outliers and scales it's probability from -1, 1. While I did find that this performed better than a normal Random Forest, I could not figure out how to use them in a 

### Apriori
I spent way more time than I am willing to admit on an incorrectly labeled dataset and my predictions were all horrible. Nothing was working. So I turned to the model that the aforementioned paper used in their experiment. The tl;dr of their method was to only train on accounts occuring multiple times so to establish a dataset of fraud transactions and legal transactions, look at a bunch of combinations of features with a specific level of support for that group, and classify testing data based on the max support between both groups. They reported a nearly 100% accuracy rate but at the cost of not even attempting to flag novel transactions.

### Logistic Regression


### XGBoost
This the model that seemed to perform the best overall on it's own and I took 2 very different approaches to using it. Given enough time or greater processing speed I could have been a bit more scientifically methodical with how I fed it features. 
On the untransformed data set it did pretty well. 
The main benefit of XGBoost over the traditional Gradient Boosting algorithm is computational speed (it's a lot faster). My understanding is that it benefits from working with OneHotEncoded sparse matrices, which was my first approach 




## Analysis
![ROC Curves]()
Parameters!
---
<sub>[  **[Back to Sections](#sections)** ]</sub>

## Cost Benefit & Scoring Metrics

Business problems require business solutions and while it would be great to just shoot for a perfect 100% accuracy, that's not super plausible. In the case of this dataset, it's likely impossible. Instead I'd like to explore a business scenario and the various cost/benefit outcomes of adopting vs. not adopting a model.

>*NOTE: The original competition guidelines specified results at a 20% lift. I'd imagine this is because 11 years ago, implementing a model was a lot more computationally expensive so they were looking for a strong confidence interval around a subgroup. I went with traditional ROC metrics to evaluate my models' performance.

#### The Scenario!
Our dataset consists of 99999 transactions over 98 days. This means we typically see about 1020 transactions per day, 26 of which are fraudulent. The typical transaction is about $27.50 (interestingly, fraudsters typically pull out only $23.00). Let's assume an employee can review and determine whether 1 transaction was fraudulent in 45 minutes, or 10 per day. Of course there are companies with a more robust tech and employee infrastructures to do this more quickly -- we'll circle back to that.

Let's now imagine a world where we correctly flag all fraudulent cases and only fraudulent cases for review. This would require the labor of 3 employees, who we pay $18 an hour. This set of assumptions is problematic because we typically see 7 cases of fraud between 5pm and 8am vs 19 cases during working hours. Most people who have done online shopping before would not expect an order to process until the following business day, and since we typically see 2 cases of fraud per hour during work hours, it's reasonable to conclude that a 4 person fraud investigation team can keep up with the daily backlog with time leftover. Unfortunately though, nobody wants to work on weekends, and if they did, we'd have to pay them time and a half, making it more cost effective to just let fraud happen on weekends. This means we'll lose about $1,196.00 to fraud per weekend and $1,950 during a typical work week (or 97.5 employee hours). 

Under this story we've told for ourselves, incorrectly flagging fraud as not fraud costs us $23.00, while incorrectly flagging a legal transaction as fraud costs us $18.00 -- 13.5 for employee time + the opportunity loss of reviewing actual fraud. If we correctly flag fraud we only have our $13.50 employee time while correctly flagging legal transactions incurs no loss. 

There's a great irony to me in top-level fraud detection work. At high end firms where the cost of reviewing false positives is probably going to be much lower, you can afford to skew your predictions towards a perfect recall with a lot of false positives. 

![Cost]
---

<sub>[  **[Back to Sections](#sections)** ]</sub>




## Takeaways
