# Comparación entre Motores

En este experimento se realizó una comparación entre dos motores: Google y Microsoft.

Para el mismo, se comprueba el mantenimiento del contexto y de la estructura del texto cuándo es traducido a otro idioma y luego se vuelve a traducir a su idioma original.

Cabe aclarar que este experimento se realizara con un **texto corto**, por lo que los resultados pueden variar dependiendo de la longitud del texto.

### Texto Original
```
No dejes para mañana lo que puedas hacer hoy.
Al mal tiempo, buena cara. 
Más vale tarde que nunca.
```

## Google - Google Translator
**Resultado en _Inglés_:**
```
Don't put off until tomorrow what you can do today.
In bad weather, a good face.
Better late than never.
```

**Resultado en _Español_:**
```
No dejes para mañana lo que puedes hacer hoy.
Cuando hace mal tiempo, buena cara.
Más vale tarde que nunca.
```

### Análisis - Google
Google logra conservar gran parte de la estructura y el significado del texto original. La única diferencia notable se encuentra en la segunda línea.

Oración original:

`Al mal tiempo, buena cara.`

Pasó a:

`Cuando hace mal tiempo, buena cara.`

A pesar del cambio en las palabras utilizadas, se conserva el contexto y el significado general de la oración.

Las otras dos frases mantienen prácticamente la misma estructura y significado que el texto original.

## Microsoft - MyMemory
**Resultado en _Inglés_:**
```
Don't put off until tomorrow what you can do today.
In bad weather, good face.
Better late than never.
```

**Resultado en _Español_:**
```
No dejes para mañana lo que puedes hacer hoy.
Con mal tiempo, buena cara.
Más vale tarde que nunca.
```

### Análisis - Microsoft

La primera y tercera oración mantienen prácticamente la misma estructura y significado que el texto original.

En la segunda oración se observa un cambio más notable:

Oración original:

`Al mal tiempo, buena cara.`

Pasó a:

`Con mal tiempo, buena cara.`

Aunque cambia la preposición de _al_ a _con_, se mantiene el significado general de la expresión.

Por lo tanto, Microsoft logra conservar el contexto de la oración, aunque modifica ligeramente su estructura.

## Conclusión
Ambos motores muestran alta capacidad para reconocer y construir refranes de manera correcta en su viaje de ida (al inglés) a vuelta (al español).

Aunque **Google** optó más por una reconstrucción más descriptiva, **Microsoft** se mantuvo más fiel al texto original.

En conclusión, ambos motores garantizar la preservación del significado y el contexto, pero no recuperar a su totalidad la estructura original al regresar al idioma de origen.
