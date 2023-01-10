edad :: (Num a, Ord a) => a -> String
edad x
    | x >= 18 = "mayor de edad"
    | otherwise = "menor de edad"