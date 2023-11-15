import spacy

# BEFORE COOKING! On the command line, install package before running: python -m spacy download pt_core_news_sm
nlp = spacy.load("pt_core_news_sm")

doc = nlp("Esforços significativos estão sendo direcionados para a melhoria dos benefícios de seguros de saúde no país. Recentemente, o governo anunciou novas políticas com o objetivo de proporcionar benefícios de seguro de saúde mais abrangentes e acessíveis para os cidadãos. Essa mudança visa garantir que mais pessoas tenham acesso a serviços de saúde estáveis e eficazes.")

for i, w in enumerate(doc):
    print(i, w.text, '\t', w.lemma_, '\t', w.tag_, w.pos_, '\n')