# evaluacion_final_herramientas

### Funcionamiento del código
 * El programa mainHC.py solo importa las funciones de operations.py y tiene una función main en la que éstas se usan para obtener los valores ASCII y binarios del input del usuario
 * La función get_ascii de operations.py recibe un char llamado word al que convierte en su código ASCII, mediante la función propia de Python, ord
 * La función get_binary de operations.py recibe el código ASCII obtenido de la operación get_ascii y lo convierte en formato binario, mediante un cambio en el formato con la función format
 * La función getResults recibe una lista de bytes de diferentes chars, y los concatena en un solo string, de forma que se muestre los códigos binarios de cada caracter de una palabra

### Cómo clonar el repositorio y trabajar en la rama

  * Primero, hay que tener una carpeta donde vayamos a clonar nuestro repositorio
  * Con el comando: `git clone https://github.com/JuanArias2206/evaluacion_final_herramientas.git`
  * luego, cambiamos de rama así: `git checkout parcial2`
  * Una vez ahí, ya podemos hacer cambios sobre el código
