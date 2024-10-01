| algorithme | algo sous-jacent | perte | avantages / inconvenients                      |format         |
|:----------:|:----------------:|:-----:|:----------------------------------------------:|:-------------:|
|jpeg        |                  |oui    |                                                |               |
|deflate     |lz77+huffman      |non    |compatibilité, aucun brevet                     |defaut zip/gzip|
|lzw         |                  |       |breveté mais brevet expiré. -deflate            |legacy gif/tiff|
|bzip2       |                  |       |+ ratio compression -rapidite (avantage sur lzma:parallelisation|               |
|lzma        |                  |       |+ ratio compression -rapidite (mais plus que bzip2)|7z          |
|lz4         |lz77              |non    |+rapidité comp/decomp -ratio compression        |               |
|snappy      |dictionnaire lz77 |non    |+rapidité comp/decomp -ratio compression. ouvert|               |
|zstd        |lz77 + xxhash     |non    |+rapidité comp/decomp +ratio deflate (a partir compression level 2)|               |
|brotly      |lz77+huffman      |non    |idem en ouvert                                  |               |
|lerc        |                  |oui mais defini par l'utilisateur|peut s'ajouter au zstd ou deflate|               |

[Benchmark compression avec Gdal](https://kokoalberti.com/articles/geotiff-compression-optimization-guide)
