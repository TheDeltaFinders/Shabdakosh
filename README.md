# शब्दकोष

>यो  नेपाली भाषाको अत्यन्त बृहत र पूर्ण शब्दकोष निर्माण गर्ने अभियान अन्तर्गतको परियोजना हो।


## स्थापना
पहिला यो रिपोलाई क्लोन गर्नुहोस
```
~$ git clone https://github.com/thedeltafinders/shabdakosh
```

त्यो फोल्डरमा जानुहोस् र  स्थापना गर्नुहोस्।

```
~$ cd shabdakosh
~/shabdakosh$ python3 setup.py install

```

# परनिर्भरता
यो परियोजना प्रिति लगाएतका फन्टहरूलाई देवनागरी यूनिकोडमा लान सहयोग गर्ने अर्को परियोजनामा निर्भर गर्छ। त्यसैले पहिला त्यो [`sampadak`](https://github.com/pranphy/sampadak) लाई त्यो परियोजनामा भएको जानकारी अनुरूप स्थापना गर्नुहोस् अनि यसलाई प्रयोग गर्न सक्नुहुनेछ।

```
~ $ git clone https://github.com/pranphy/sampadak
~ $ cd sampadak
~/sampadak$ python3 setup.py install
```


अनि अर्को भनेको [`pdfminer.six`](https://github.com/pdfminer/pdfminer.six) हो। यसलाई पनि सजिलै स्थापना गर्न सकिनेछ।

```
~$ python3 -m pip install pdfminer.six
```

## प्रयोग

स्थापना भइसकेपछि तपाईँले आफ्नो पाथमा `shabdakosh` नामको एउटा स्वचालक प्रोग्राम पाउनुहुनेछ। त्यसको प्रयोग गरी मजा लिनुहोस्।


```
~$ shabdakosh 

```

हाल यसले यसको `res` फोल्डरमा भएको एउटा फाइलबाट शब्दहरू निकाल्छ र त्यस सँग सम्बन्धित फन्टहरू पनि देखाउँछ।

## विषेशता
थपिँदै जाने

