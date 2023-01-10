--Recibe un numero y regresa una cadena correspondiente a cada numero
dime :: (Integral a) => a -> String
dime 1 = "Uno"
dime 2 = "Dos"
dime 3 = "Tres"
dime 4 = "Cuatro"
dime 5 = "Cinco"
dime x = "No entre 1 y 5"

