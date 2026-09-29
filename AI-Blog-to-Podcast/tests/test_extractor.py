from src.article.extractor import extract_article


url = "https://en.wikipedia.org/wiki/Artificial_intelligence"

result = extract_article(url)

print("TITLE:")
print(result["title"])

print("\nARTICLE:")
print(result["text"][:2000])