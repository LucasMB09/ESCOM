import System.Random

caras :: [String]
caras = ["Aguila","Sol"]

randomList :: StdGen ->Double ->Int -> [Int]
randomList g m n = map truncate (map (*m) (take n (randoms (g) :: [Double])))

juega :: StdGen -> String
juega g = 
         let xs = randomList g 2 1       
         in (caras !! (xs!!0) )
            
main = do
  g <- newStdGen

  print $ juega g
  --print $ randomList g 6 2
  
