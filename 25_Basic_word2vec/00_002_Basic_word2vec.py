from gensim.models import word2vec

data = word2vec.LineSentence("toji.wakati")
model = word2vec.Word2Vec(data, size=200, window=10, hs=1, min_count=2, sg=1)
model.save("toji.model")

model = word2vec.Word2Vec.load("toji.model")
print("positive=[\"서울\"]: ", model.most_similar(positive=["서울"])[:3])
print("positive=[\"많다\", \"보통\", \"조금\"]: ", model.most_similar(positive=["많다", "보통", "조금"])[:1])