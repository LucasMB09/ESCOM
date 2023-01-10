rember::Eq a=>[a]->a->[a]
rember [] e = []
rember (x:xs) e 
    | x == e = rember xs e
    | otherwise = x:( rember xs e )