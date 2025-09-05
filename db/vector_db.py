import json
import numpy as np

class VectorDB():
    def __init__(self):
        self.id = 0
        self.content = []
        self.vector_storage = []

    def _normalize_vecs(self, vecs):
        return vecs / np.linalg.norm(vecs)

    def _consine_similarity(self, vector_a, vector_b):
        dot = np.dot(vector_a, vector_b)
        norm_a = np.sqrt(np.dot(vector_a, vector_a))
        norm_b = np.sqrt(np.dot(vector_b, vector_b))

        return dot / norm_a * norm_b

    def get_docs_size(self):
        return len(self.vector_storage)

    def add(self, vecs, content):
        vecs = np.array(vecs)
        vecs = self._normalize_vecs(vecs)

        self.vector_storage.append(vecs)
        self.content.append({"id": self.id, "content": content})
        self.id += 1

    def search(self, query_vector, k=5):
        query_vector = self._normalize_vecs(query_vector)

        cosine_sim = [ self._consine_similarity(query_vector, vector) for vector in self.vector_storage ]
        sorted_index = np.argsort(cosine_sim[::-1])[:k]

        return [ (self.content[index], cosine_sim[index]) for index in sorted_index ]
    
    def init_seed_data(self):
        with open("./data/init_emb_data.json", 'r') as file:
            seed_data = json.load(file)
        
        for doc in seed_data:
            self.add(vecs=doc['embedding'], content=doc['content'])