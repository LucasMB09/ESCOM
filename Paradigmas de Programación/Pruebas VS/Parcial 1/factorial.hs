--Calcula el factorial de un número
factorial :: (Integral a) => a -> a
factorial 0 = 1
factorial n = n * factorial (n - 1)