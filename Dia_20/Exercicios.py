# Read this url and find the 10 most frequent words. romeo_and_juliet = 'https://www.gutenberg.org/cache/epub/1513/pg1513-images.html'
import requests
url = 'https://www.gutenberg.org/cache/epub/1513/pg1513-images.html'
response = requests.get(url)
text = response.text
def most_frequent_words(text, n):
    splited_string = text.split()
    most_common_words_dict = {}
    for word in splited_string:
        if word not in most_common_words_dict:
            most_common_words_dict[word] = 1
        else:
            most_common_words_dict[word] += 1
    sorted_most_common_words = sorted(most_common_words_dict.items(), key=lambda kv:kv[1], reverse=True)[:n]
    return sorted_most_common_words
print(most_frequent_words(text, 10))

# Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find :
    # the min, max, mean, median, standard deviation of cats' weight in metric units.
    # the min, max, mean, median, standard deviation of cats' lifespan in years.
    # Create a frequency table of country and breed of cats
url = 'https://api.thecatapi.com/v1/breeds'
response = requests.get(url)
breeds = response.json()
def weight(breeds):
    all_weight = []
    for breed in breeds:
        for key,value in breed.items():
            if key == 'weight':
                weight_unedited = value.get('metric')
                part = weight_unedited.split(' - ')
                total = int(part[0])+ int(part[1])
                all_weight.append(total)
    return all_weight
def median(all_metrics):
    soma = 0
    for n in all_metrics:
        soma += n
    return soma/len(all_metrics)

all_weight = weight(breeds)
print(min(all_weight))
print(max(all_weight))
print(median(all_weight))
def lifespan(breeds):
    all_lifespan = []
    for breed in breeds:
        for key,value in breed.items():
            if key == 'life_span':
                lifespan_unedited = value
                part = lifespan_unedited.split(' - ')
                total = int(part[0])+ int(part[1])
                all_lifespan.append(total)
    return all_lifespan
all_lifespan = lifespan(breeds)
print(min(all_lifespan))
print(max(all_lifespan))
print(median(all_lifespan))