data Vector = Vector {
    x :: Int
    , y :: Int
    , z :: Int
    } 
(deriving Show)

sumaV :: Vector -> Vector
sumaV v1 v2 = Vector (x1+x2) (y1+y2) (z1+z2)