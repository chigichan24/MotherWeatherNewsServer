from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

client = language.LanguageServiceClient()

text_list = [
    u'ありがとう。とても嬉しいです。',
    u'つらい'
]

for text in text_list:
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT,
        language="ja"
    )
    sentiment = client.analyze_sentiment(document=document).document_sentiment
    print('Text: {}'.format(text))
    print(sentiment)
    print()
