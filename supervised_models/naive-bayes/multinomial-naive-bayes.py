import math
from collections import defaultdict
class MultinomialNB:
    def __init__(self, articles_per_tag):
        self.articles_per_tag = articles_per_tag
        self.tags = self.articles_per_tag.keys()
        self.probability_per_tag = {}
        self.probabilty_of_given_article_per_tag = {}
        self.train()

    def train(self):
        tag_count_map = {tag: len(self.articles_per_tag[tag]) for tag in self.tags}
        self.probability_per_tag = {tag: tag_count_map[tag] / sum(tag_count_map.values()) for tag in self.tags}
        self.probabilty_of_given_article_per_tag = self._get_probabilty_of_given_article_per_tag()

    def _get_probabilty_of_given_article_per_tag(self):
        word_frequencies_per_tag = defaultdict(lambda: {tag: 0 for tag in self.tags})
        total_words_per_tag = defaultdict(int)

        for tag in self.tags:
            for article in self.articles_per_tag[tag]:
                for word in article:
                    word_frequencies_per_tag[word][tag] += 1
                    total_words_per_tag[tag] += 1

        word_likelyhood_per_tag = defaultdict(lambda: {tag: 0.5 for tag in self.tags})

        for word, count_of_word_per_tag in word_frequencies_per_tag.items():
            for tag in count_of_word_per_tag.keys():
                word_likelyhood_per_tag[word][tag] = (word_frequencies_per_tag[word][tag] + 1) / (total_words_per_tag[tag] + 2)
        
        return word_likelyhood_per_tag
        
    def predict(self, article):
        probability_of_article_per_tag = {tag: math.log(prob) for tag, prob in self.probability_per_tag.items()}

        for word in article:
            for tag in self.tags:
                probability_of_article_per_tag[tag] += math.log(self.probabilty_of_given_article_per_tag[word][tag])
            
        return probability_of_article_per_tag
