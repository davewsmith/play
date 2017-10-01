# Madlib Spam

A spammer's blog comment script [made the rounds](http://alexking.org/blog/2013/12/22/spam-comment-generator-script) a few years back.
Out of curiosity, I wrote a parser/evaluator to generate output from the script.
The script parses into a sequence of parts, which can be text blocks or sequences.
Recursive descent is a natural fit.

## Why?

The general technique is useful for frivolous fun, or it can be put to evil use.

The spammer's game is to get a few innocent-looking comments past a moderation queue in the hopes of getting whitelisted.
Then they can start landing spam payloads into blog comments.

You can still see remnants of this approach by searching for phrases from the output:

> [Howdy! I could have sworn I've been to this site before](https://www.google.com/search?q="Howdy!+I+could+have+sworn+I%27ve+been+to+this+site+before&oq=Howdy!+I+could+have+sworn+I%27ve+been+to+this+site+before") but after looking at some of the articles I realized it's new to me. Nonetheless, I'm certainly delighted I discovered it and I'll be book-marking it and checking back often!

> [What's up, just wanted to tell you, I enjoyed this article.](https://www.google.com/search?q="What%27s+up%2C+just+wanted+to+tell+you%2C+I+enjoyed+this+article."&oq="What%27s+up%2C+just+wanted+to+tell+you%2C+I+enjoyed+this+article.") It was helpful. Keep on posting!

> I am curious to find out what blog system you are working with? I'm experiencing some minor security problems with my latest site and I would like to find something more safe. Do you have any suggestions?

And this, for chutzpah:

> Howdy, i read your blog from time to time and i own a similar one and i was just curious if you get a lot of spam responses? If so how do you prevent it, any plugin or anything you can suggest? I get so much lately it's driving me insane so any support is very much appreciated. 

