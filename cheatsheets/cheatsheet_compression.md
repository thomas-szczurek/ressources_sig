| algorithme | algo sous-jacent | perte | avantages / inconvenients                      |format         |
|:----------:|:----------------:|:-----:|:----------------------------------------------:|:-------------:|
|deflate     |lz77+huffma       |non    |compatibilité, aucun brevet                     |defaut zip/gzip|
|lzw         |                  |       |breveté mais brevet expiré. -deflate            |legacy gif/tiff|
|lz4         |lz77              |non    |+rapidité comp/decomp -ratio compression        |               |
|snappy      |dictionnaire lz77 |non    |+rapidité comp/decomp -ratio compression. ouvert|               |
|zstd        |lz4 + xxhash      |non    |+rapidité comp/decomp =ratio deflate            |               |
|brotly      |lz77+huffman      |non    |idem en ouvert                                  |               |