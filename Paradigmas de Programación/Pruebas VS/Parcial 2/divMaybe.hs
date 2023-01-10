divMaybe :: Int -> Int -> Maybe Int
divMaybe _ 0 = Nothing
divMaybe a b = Just (a `div` b)