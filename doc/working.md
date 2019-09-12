# Shabdakosh [शब्दकोष]

The goal of this project is to convert the pdf into configurable database.

## FAQ

### What has been done so far?

Not much! A lot of time was spent trying to figure out how to extract the text with their font associated. This took a long time to figure out and now we have a working procedure to do that.

We use `pdfminer.six` library to extract the text and its font.

Currently the `readpdf.py` reads the words from the pdf file and its font associated and yields back the tuple of word and its font. In principle we should be able to use this information and the fact that the meaning are numbered to be able to identify words, its meaning and part of speech and everything there is in the pdf about the word. Its sub words their meaning and composition etc.

Part of the code initially intended to be here has now moved to a different project, sampadak. That will handle nepali word conversion edition and standardarization.

### Is pdfminer.six working perfectly?

No, when reading the pdf the library is not reading the newline characters. The result of which is that when there is a word following the newline it is interpreted as a single word because we don't have any way of discerning this. For now, I think we can live with this. This will only affect joined words in meaning and shouldn't impact discering between words meaning and parts of speech.

### What is, in principle, the  algorithm for figuring out the dictionary.

We get a stream of words and their fonts. Now, it is known that all the major words are in a bold ~HimalayaBold~ font. So this font information gives us the word. The composition of words [प्रकृति प्रत्यय उपसर्ग इत्यादि] is always in a pair of [] which are in ~Times new roman~ font.  New meaning always start with number. like [१. छाँया परेको। २. ढाकिएको; छोपिएको।].

### How do we save the words?

I think saving the words can be done in another project. Lets just focus on separating the stream of words and fonts into meaningful dictionary first. We can use this project as a library on another project to use it in a database or searialized file or whatever.

### How about user interface?

Well this project is not going to be targed to the user. Its just figuring words and meaning. Saving and user interface will be in another project which uses this as a library. My I ideas is, we will make a django project and its ORM for database and web interface and host it somewhere and let the user interact with it and possibly allow them to suggest error correction and add new information.
