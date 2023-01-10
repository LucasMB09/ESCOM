tablas :: Int -> [Int] -> [Int]
tablas _ [] = []
tablas n (x:xs) = a * x : tablas n xs