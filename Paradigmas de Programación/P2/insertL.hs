insertL :: Int -> Int -> [Int] -> [Int]
insertL new old(a:b) = if a==old then new:a:b else
    a:insertL new old b