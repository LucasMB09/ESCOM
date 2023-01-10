data Vector a = Vector a a a deriving Show

sumaV :: (Num a) => Vector a -> Vector a -> Vector a
(Vector i j k) `sumaV` (Vector l m n) = Vector (i+l) (j+m) (k+n)

restaV :: (Num a) => Vector a -> Vector a -> Vector a
(Vector i j k) `restaV` (Vector l m n) = Vector (i-l) (j-m) (k-n)

dotProdV :: (Num a) => Vector a -> Vector a -> a
(Vector i j k) `dotProdV` (Vector l m n) = i*l + j*m + k*n

prodEsc :: (Num a) => Vector a -> a -> Vector a
(Vector i j k) `prodEsc` a = Vector (i*a) (j*a) (k*a)

magnitud :: (Num a) => Vector a -> Float
magnitud (Vector i j k)  = sqrt(i^2 + j^2 + k^2)
