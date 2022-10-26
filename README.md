
# Asignación: Oro Ninja

## Objetivos

* Practicar el uso de sesiones
* Hacer que el servidor use los datos enviados por un cliente con un formulario
* Practicar el uso de entradas ocultas

---

Crea un juego simple para probar tu comprensión de Flask e implementa la funcionalidad a continuación.

Para esta tarea, ¡vas a crear un minijuego que ayudará a un ninja a ganar algo de dinero! Cuando comiences el juego, tu ninja debería tener 0 de oro. El ninja puede ir a diferentes lugares (granja, cueva, casa, casino) y ganar diferentes cantidades de oro. En el caso de un casino, tu ninja puede ganar *o perder* hasta 50 de oro. Tu trabajo consiste en crear una aplicación web que le permita a este ninja ganar oro y mostrar sus actividades pasadas.


* Crear un nuevo proyecto Flask llamado oro_ninja
* Crea la plantilla como se muestra en el wireframe de arriba, con 4 formularios separados
* Haz que la ruta raíz renderice esta página
* Haz que la ruta POST "/process_money" aumente/disminuya el oro del usuario en una cantidad adecuada y redirija a la ruta raíz
* BONUS NINJA: muestra todas las actividades realizadas por el usuario en un registro en el HTML, como se muestra en el wireframe.
* BONUS NINJA: haz que las actividades estén codificadas por colores como se muestra arriba (+ dinero es verde, - dinero es rojo)
* BONUS NINJA: agregar un botón de reinicio para reiniciar el juego
* BONUS SENSEI: haz que las actividades se muestren en orden descendente, con la actividad más reciente primero
* BONUS SENSEI: proporciona parámetros ganadores al juego; por ejemplo, un usuario debe obtener 500 de oro en menos de 15 movimientos. Solo muestra el botón de reinicio una vez que el usuario haya ganado o perdido.
* BONUS SENSEI: Completa la ruta "/process_money" sin 4 sentencias condicionales (es decir, sin hacer if farm..., elif cave..., etc.).
