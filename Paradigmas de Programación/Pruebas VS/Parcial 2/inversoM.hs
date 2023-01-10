inverso :: (Double a) => a -> Maybe a
inverso 0 = Nothing
inverso a = Just (1 `div` a)