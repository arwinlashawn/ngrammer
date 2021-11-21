# ngrammer
Some NLP stuff.

# Usage
The API takes a body as follows:
```
{
    "order": 2,
    "text": "This is a beautiful world."
}
```

# Expected performance of the API with respect to the payload size
The API performance degrades with increasing payload size. Did a bit of time profiling to see how the API slows down as text length increases by 10x, 100x, 1000x, and so on. Here are the results:

```
text1 = "This is a beautiful world. "
text2 = text1*10 # 0.66x slower than text1 processing time
text3 = text1*100 # 3.5x slower than text1 processing time
text4 = text1*1000 # 86x slower than text1 processing time
text5 = text1*10000 # 1200x slower than text1 processing time
text6 = text1*100000 # 4400x slower than text1 processing time
```

# Ways to improve the response time of the API considering inputs will mostly be long essays
* Implement caching of API response
* Increase memory allocation for Lambda, which increases compute speed
* Consider the use of `colibricore` library for faster n-gram sequence determination

