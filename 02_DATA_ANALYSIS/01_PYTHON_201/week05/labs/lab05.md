# Lab 05

Ejercicio 5
Al final de la Edad Media, en Francia, el diplomático francés Blaise de Vigenère desarrolló un algoritmo para cifrar mensajes que nadie fue capaz de romper durante aproximadamente 250 años. Este algoritmo se conoce con el nombre de cifrado de Vigenère.El cifrado de Vigenère consiste en añadir a cada una de las letras de un texto un desplazamiento a partir de una clave secreta para conseguir una nueva letra diferente del original. Veamos un ejemplo:Si asignamos el número 1 en la primera letra del abecedario, A, 2 a la siguiente, B, etc., imaginad que tenemos el siguiente mensaje:

ABC 123 y la siguiente clave secreta:

DEF 456 A cada letra del mensaje original le aplicamos un desplazamiento en función de la misma posición dentro de la clave secreta. Por lo tanto, el mensaje cifrado quedaría de la siguiente forma:

E G I (1 + 4) (2 + 5) (3 + 6) Escribid una función que, dado un mensaje y una clave secreta, calcule y devuelva el mensaje cifrado.Consideraciones: Utilizad como alfabeto de entrada el alfabeto inglés en mayúsculas.El valor predeterminado de la clave secreta será DATASCI.

```
# TODO

```