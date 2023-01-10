import System.Random

randomList :: StdGen ->Double ->Int -> [Int]
randomList g m n = map truncate (map (*m) (take n (randoms (g) :: [Double])))

main = do
  g <- newStdGen
  print $ randomList g 6 2
  