raiz :: Double -> Maybe Double
raiz x
    | x < 0 = Nothing
    | otherwise = Just (sqrt x)