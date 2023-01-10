menorDiez :: (Num a, Ord a) => a -> Maybe a
menorDiez a
 | a < 10 = Just a
 | otherwise = Nothing