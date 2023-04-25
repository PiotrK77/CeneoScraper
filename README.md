# CeneoScraper

as CSS selectors of the components of opinions in [Ceneo.pl](https://www.ceneo.pl/)
service

|Components|Variable/Dictionary key|Data type|Selector|
| :- | :- | :- | :- |
|opinion|opinion/single\_opinion|Tag, dictionary|div.js\_product-review|
|opinion ID|opinion\_id|string|["data-entry-id"]|
|opinion’s author|author|string|'span.user-post__author-name'|
|author’s recommendation|recommendation|bool|'span.user-post__author-recomendation > em'|
|score expressed in number of stars|score|float|'span.user-post__score-count'|
|opinion’s content|description|string|'div.user-post__text'|
|list of product advantages|pros|string|'div.review-feature__col:has( > div.review-feature__title--positives) > div.review-feature__item'|
|list of product disadvantages|cons|string|'div.review-feature__col:has( > div.review-feature__title--negatives) > div.review-feature__item'|
|how many users think that opinion was helpful|like|int|<p>button.vote-yes["data-total-vote"]</p><p>button.vote-yes > span</p><p>span[id^=votes-yes]</p>|
|how many users think that opinion was unhelpful|dislike|int|<p>button.vote-no["data-total-vote"]</p><p>button.vote-no > span</p><p>span[id^=votes-no]</p>|
|publishing date|publish\_date|string|span.user-post\_\_published > time:nth-child(1) ["datetime"]|
|purchase date|purchase\_date|string|span.user-post\_\_published > time:nth-child(2) ["datetime"]|

## Python libraries used in project
1. Requests
2. BeautifulSoup
3. Json
4. Os
5. Translate
6. Numpy