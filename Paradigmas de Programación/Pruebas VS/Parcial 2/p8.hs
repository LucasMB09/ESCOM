cuenta :: [a] -> a
cuenta (x:xs)
    | (x:xs) == [] = 0
    | x == xs = 1 + cuenta xs
    | otherwise = cuenta xs