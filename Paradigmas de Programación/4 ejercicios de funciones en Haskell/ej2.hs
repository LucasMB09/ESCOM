ej2 :: (Num a, Ord a) => a -> a -> String
ej2 x y 
    | x < y = "1er numero es menor que el 2ndo numero"
    | x == y = "1er numero es igual que el 2ndo numero"
    | otherwise = "1er numero es mayor que el 2ndo numero"