--Suma los elementos de una lista
sumalista :: (Num a) => [a] -> a
sumalista [] = 0
sumalista (x:xs) = x + sumalista (xs)