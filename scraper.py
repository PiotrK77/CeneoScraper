import requests
from bs4 import BeautifulSoup
import os
import json
import numpy as np
from translate import Translator
import os

def get_element(dom_tree, selector, attribute = None, return_list = False):
     try:
        if return_list:
             return ", ".join(tag.text.strip() for tag in dom_tree.select(selector))
        if attribute:
            if selector:
                return dom_tree.select(selector)[attribute].text.strip()
            return dom_tree(attribute)
        return dom_tree.select(selector).text.strip()
     except AttributeError:
          recomendation = None


def clean_text(text):
     return '  '.join(text.replace(r"\s", " ").split())

selectors = {
     "opinion_id": "data-entry-id",
     "author": "span.user-post__author-name",
     "recomendation": "span.user-post__author-recomendation",
     "score": "span.user-post__score-count",
     "description": "div.user-post__text",
     "pros": "div.review-feature__col:has( > div.review-feature__title--positives) > div.review-feature__item",
     "cons": "div.review-feature__col:has( > div.review-feature__title--negatives) > div.review-feature__item",
     "like": "button.vote-yes > span",
     "dislike": "button.vote-no > span",
     "publish_date": "span.user-post__published > time:nth-child(1)",
     "purchase_date": "span.user-post__published > time:nth-child(2)"
}

from_lang = "pl"
to_lang = "eng"


product_code = "133748381"        #input("Please enter product code: ")

print(product_code)

url = f"https://www.ceneo.pl/{product_code}#tab=reviews"
all_opinions = []

while url:
    response = requests.get(url)
    if response.status_code == requests.codes.ok:
        page_dom = BeautifulSoup(response.text, "html.parser")
        opinions = page_dom.select("div.js_product-review")

        if len(opinions) > 0:
            #all_opinions = []

            for opinion in opinions:
                single_opinion = []
                for key, value in selectors:
                     single_opinion[key] = get_element(opinion, *value)
                single_opinion["recommendation"] = True if single_opinion["redommendation"] == "Polecam" else False if single_opinion["recommendation"] == "Nie polecam" else None
                single_opinion["score"] = np.divide(*[float(score.replace(",", ".")) for score in single_opinion["score"].split("/")])
                single_opinion["like"] = int("single_opinion"["like"])
                single_opinion["dislike"] = int("single_opinion"["dislike"])
                single_opinion["description"] = clean_text(single_opinion)
                single_opinion["description_en"] = translator.translate(single_opinion["description"])


                all_opinions.append(single_opinion)


            try:
                url = "https://ceneo.pl" + page_dom.select_one("a.pagonation__next")["href"]
            
            except TypeError:
                url = None

                if not os.path.exists("opinions"): 
                    os.mkdir("opinions")

        
        else:
            print(f"There are no opinions about product with {product_code} code")
            url = None
    
if len(opinions) > 0:
    if not os.path.exists("./opinions"):
         os.mkdir("./opinions")
    with open(f"./opinions/{product_code}.json", "w",encoding="UTF-8") as jf:
                json.dump(all_opinions,jf,indent=4,ensure_ascii=False)



'''
                opinion_id = opinion["data-entry-id"]
                author = opinion.select_one("span.user-post__author-name").text.strip()
                try:
                    recomendation = opinion.select_one("span.user-post__author-recomendation").text.strip()
                except AttributeError:
                    recomendation = None
                score = get_element(opinion, "span.user-post__score-count")
                #score = opinion.select_one("span.user-post__score-count").text.strip()
                description = get_element(opinion, "div.user-post__text")
                #description = opinion.select_one("div.user-post__text").text.strip()
                pros = get_element(opinion, "div.review-feature__col:has( > div.review-feature__title--positives) > div.review-feature__item", return_list = True)
                #pros = opinion.select("div.review-feature__col:has( > div.review-feature__title--positives) > div.review-feature__item")
                #pros = [p.text.strip() for p in pros]
                cons = get_element(opinion, "div.review-feature__col:has( > div.review-feature__title--negatives) > div.review-feature__item", return_list = True)
                #cons = opinion.select("div.review-feature__col:has( > div.review-feature__title--negatives) > div.review-feature__item")
                #cons = [c.text.strip() for c in cons]
                like = opinion.select_one("button.vote-yes > span").text.strip()
                dislike = opinion.select_one("button.vote-no > span").text.strip()
                publish_date = opinion.select_one("span.user-post__published > time:nth-child(1)")["datetime"].strip()
                purchase_date = opinion.select_one("span.user-post__published > time:nth-child(2)")


                single_opinion = {
                    "opinion_id": opinion_id,
                    "author": author,
                    "recomendation": recomendation,
                    "score": score,
                    "description": description,
                    "pros": pros,
                    "cons": cons,
                    "like": like,
                    "dislike": dislike,
                    "publish_date": publish_date,
                    "purchase_date": purchase_date["datetime"].strip() if purchase_date != None else None
                }

                all_opinions.append(single_opinion)
'''