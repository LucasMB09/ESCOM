ej1 :: (Num a, Ord a) => a -> String
ej1 x
    | x < 0 = "Menor que 0"
    | x == 0 = "Igual que 0"
    | otherwise = "Mayor que 0"