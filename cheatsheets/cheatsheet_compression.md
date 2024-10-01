| algorithme | algo sous-jacent | perte | avantages / inconvenients                      |format         |
|:----------:|:----------------:|:-----:|:----------------------------------------------:|:-------------:|
|deflate     |lz77+huffman      |non    |compatibilité, aucun brevet                     |defaut zip/gzip|
|lzw         |                  |       |breveté mais brevet expiré. -deflate            |legacy gif/tiff|
|jpeg        |                  | oui   |                                                |               |
|lzma        |                  |       |                                                |               |
|bzip2       |                  |       |                                                |               |
|lz4         |lz77              |non    |+rapidité comp/decomp -ratio compression        |               |
|snappy      |dictionnaire lz77 |non    |+rapidité comp/decomp -ratio compression. ouvert|               |
|zstd        |lz77 + xxhash     |non    |+rapidité comp/decomp =ratio deflate            |               |
|brotly      |lz77+huffman      |non    |idem en ouvert                                  |               |
|lerc        |                  |oui mais defini par l'utilisateur       |s'ajoute au zstd ou deflate                     |               |

[Benchmark compression avec Gdal](https://kokoalberti.com/articles/geotiff-compression-optimization-guide)
