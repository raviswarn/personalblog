Title: Popularity of Baby Names Since 1880
Date: 2016-08-16 16:13
Authors: Michael Toth
Modified:2016-08-16 16:13 
Category: R
Tags: R, Shiny
Slug: popularity-of-baby-names-since-1880 
author_gplusid: 103836786232018210272
Summary: In this post, I will present an interactive analysis on the popularity of baby names since 1880. The analysis was built in R, with interactivity provided with Shiny

[A while back]({filename}./shiny_server_setup.md) I spent some time figuring out how to serve shiny apps through my personal website, but I haven't had a chance to build any apps until recently. I set out to create a few simple shiny apps in R that I could use as a sort of test run, and I'm writing those up here.

I'm going to be analyzing some open data provided by the Social Security Administration on the popularity of baby names over the years--specifically, since 1880. 
Data comes from [Social Security Administration](https://www.ssa.gov/oact/babynames/limits.html)  

In the graphic below, you can investigate the 10 most popular baby names for any year since 1880, either for males or females. You can also click the play icon directly below the year slider to view an animated history of the most popular names.
<br>
<br>

<iframe src="http://www.michaeltoth.me/shiny/census_names/top10/" style="border: none; width: 100%; height: 400px"></iframe>


In the second graphic, you can enter any name, and the graph will display how the popularity of that name has changed over time. Be sure to also select whether the name is for males or females, or you'll likely see some unexpected results!
<br>
<br>

<iframe src="http://www.michaeltoth.me/shiny/census_names/tracer/" style="border: none; width: 100%; height: 400px"></iframe>

Finally, below I present an interesting graphic that displays how the popularity of names changes over time. Something about gganimate.

<INCLUDE GRAPHIC HERE>

For the full code behind the shiny applications and the animation produced above, check out my [Github](https://github.com/michaeltoth/shiny-projects/tree/master/census_names)
