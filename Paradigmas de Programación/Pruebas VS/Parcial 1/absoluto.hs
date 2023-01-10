absoluto :: (Num a, Ord a) => a -> a
absoluto x 
    | x > 0 = x
    | otherwise = -x