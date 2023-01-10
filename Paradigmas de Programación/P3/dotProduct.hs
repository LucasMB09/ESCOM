dotProduct :: Num a => [a] -> [a] -> a
dotProduct x y = doT $ zipWith (*) x y

doT :: (Num a) => [a] -> a
doT = foldl (\acc x -> acc + x) 0 