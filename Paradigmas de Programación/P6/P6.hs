import Control.Monad.Random 

removeAt :: Int->[a]->(a, [a])
removeAt i items = ( items!!i , take i items ++ drop (1+i) items)

rnd_select :: (MonadRandom m, Eq a) => [a] -> Int -> m[a]
rnd_select [] _ = return []
rnd_select _ 0 = return []
rnd_select ys n = do
    rnd_index <- getRandomR (1, lenght ys)
    let(x,xs) = removeAt rnd_index ys
    xs' <- rnd_select xs (n-1)
    return (x:xs')

main = do
  l<-rnd_select["1. ¿Quién pintó Las meninas? a) Francisco de Goya b) Diego Velázquez c) Salvador Dalí", "2. ¿Cuál es la capital de Hungría? a) Viena b) Praga c)Budapest", "3. Aproximadamente, ¿cuántos huesos tiene el cuerpo humano? a)40 b)390 c)208", "4. Seleccione la fecha y el turno que prefiere para cursar la materia a)Lunes – Turno de la mañana b)Lunes – Turno de la tarde c)Miércoles – Turno de la mañana", "5. ¿Cómo le resultó la atención dada por el personal de nuestra empresa? a)Muy buena b)Buena c)Mala", "6. a)En el mesencéfalo se ubican: Colículos superiores e inferiores b)El cuarto ventrículo Deriva de la vesícula terciaria c)Las pirámides bulbares", "7. Si P = M+N, ¿cuál de las siguientes fórmulas es correcta? a)M = P + N b)N = P + M c) M = P – N", "8. ¿Qué animales son mamíferos? a) Un gato b) Un perro c) Un perico d) Una higuana e) Un cocodrilo","9.¿La capital de Brasil es? a) Maracaibo b) Sao paulo c) Copacabana", "10. ¿Qué ciencia o disciplina estudia la estructura y funcionamiento del cuerpo humano? a) Cardiología b) Zoología c) Anatomía d) Fisiología humana","11. ¿Cuantos continentes comienza su nombre con la letra A? a)Uno b)Dos c)Tres d)Cuatro","12. ¿Cual es tu animal favorito?a)Perros b)Gatos c)Pajaros","13. ¿La sumatoria de 7 + 7 es? a)14 b)12 c)13","14. ¿En una escuela hay 10 niños y 21 niñas cuantos alumnos hay en total? a)31 b)45 c)66","15. ¿Cuál es el nombre del río más largo del mundo? A: Río Nilo B: Río Amazonas C: Río Danubio","16. ¿Cuál es el océano más grande del mundo? A: Océano Pacífico B: Océano Índico C: Océano Atlántico","17.¿Cuál es el país más grande del mundo? A: China B: Rusia C: India","18. ¿Cuál es el país que tiene forma de bota?A: España B: Honduras C: Italia","19.  ¿Cuál es la capital de Nicaragua? A: Santiago B: Brasilia C: Managua","20. En qué continente se encuentra Surinam? A: África B: América del Sur C: Oceanía"] 10
  print $ l