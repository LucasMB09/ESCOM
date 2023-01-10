serie :: (Integral a) => a -> a -> a
serie _ 0 = 1
serie a n = a^n + serie a (n-1)