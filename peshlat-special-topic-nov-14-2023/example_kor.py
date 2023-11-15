import spacy

# BEFORE COOKING! On the command line, install package before running: python -m spacy download ko_core_news_lg 
nlp = spacy.load("ko_core_news_lg")

# Efforts to improve health insurance benefits are in full swing. The government recently announced new policies to provide more comprehensive and accessible coverage of health services. The new system is designed to ensure that more people receive reliable and effective medical services.
doc = nlp("의료 보험 혜택 개선을 위한 노력이 본격화되고 있습니다. 정부는 최근 의료 서비스에 대한 보다 포괄적이고 접근 가능한 보험 혜택을 제공하기 위해 새로운 정책을 발표했습니다. 새로운 제도는 보다 많은 국민들이 안정적이고 효과적인 의료 서비스를 받을 수 있도록 설계되었습니다.") 

for i, w in enumerate(doc):
    print(i, w.text, '\t', w.lemma_, '\t', w.tag_, w.pos_, '\t')