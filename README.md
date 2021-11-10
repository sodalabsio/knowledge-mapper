# knowledge-mapper
Project  for developing knowledge maps via deep text embeddings.

### Getting started
To start a development server
```
pip install -r requirements.txt
gunicorn --bind 0.0.0.0:8000 wsgi:app
```

### Contents
- `static`: contains core files (data, config and html) for app
- `notebooks`: contain preprocessor for extracting text embeddings using BERT 

> Note: Use any port as available.

### TODO
- [ ] Create pre-trained map configs for UMAP and t-SNE (update app to new version)
- [ ] Add text bar to automagically match top-k units (in vector space) as per query

### Acknowledgements and References
- [Official TensorFlow Embedding Projector](https://github.com/tensorflow/embedding-projector-standalone)