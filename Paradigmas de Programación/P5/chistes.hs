import System.Random

chistes :: [String]
chistes = ["Cual es el ultimo animal que subio al arca de Noe? El del-fin."
        ,"Como se dice panuelo en japones? Saka-moko."
        ,"Como se dice disparo en arabe? Ahi-va-la-bala."
        ,"Que le dice un gusano a otro gusano? Voy a dar una vuelta a la manzana."
        ,"Cual es el colmo de Aladdin? Tener mal genio."
        ,"Si se muere una pulga, a donde va? Al pulgatorio."
        ,"Como se dice pelo sucio en chino? Chin cham pu."
        ,"Habia una vez un nino tan, tan, tan despistado que... da igual, me he olvidado del chiste!"
        ,"Estas obsesionado con la comida, de verdad. Que dices croquetamente?"
        ,"Por que las focas miran siempre hacia arriba? Porque ahi estan los focos!"
        ,"Camarero, ese filete tiene muchos nervios. Pues normal, es la primera vez que se lo comen."
        ,"Como se llama el primo de Bruce Lee? Broco Lee"
        ,"Si los zombies se deshacen con el paso del tiempo zombiodegradables?"
        ,"Que le dice un techo a otro? Techo de menos."
        ,"Como se queda un mago despues de comer? Magordito."
        ,"Me da un cafe con leche corto? Se ha roto la maquina, cambio."
        ,"Que es un pez en el cine? Pues un mero espectador..."
        ,"Que le dice un espagueti a otro? El cuerpo me pide salsa!"
        ,"Habia un perro de goma que cuando se rascaba se borraba."
        ,"Como maldice un pollito a otro? Caldito seas"]

randomList :: StdGen ->Double ->Int -> [Int]
randomList g m n = map truncate (map (*m) (take n (randoms (g) :: [Double])))

juega :: StdGen -> String
juega g = 
         let xs = randomList g 2 1       
         in (chistes !! (xs!!0) )
            
main = do
  g <- newStdGen

  print $ juega g