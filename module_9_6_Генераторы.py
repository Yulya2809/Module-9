def all_variants(text):
    text = text.lower()
    for value in text:
        yield value
    for i in range(len(text) - 1):
        el1 = text[i]
        el2 = text[i + 1]
        result = el1 + el2
        yield result
    yield text


a = all_variants("abc")
for i in a:
    print(i)
    