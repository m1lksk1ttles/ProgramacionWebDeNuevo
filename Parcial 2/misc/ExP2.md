# Guia de estudio (para no cagar la unidad 2 de nuevo)

**1. Que es el JSon y para que sirve?**  
El JSON (JavaScript Object Notation) es un formato de texto ligero y universal para el intercambio de datos. Sirve como el estándar principal para que las API transmitan información estructurada (basada en objetos y arrays) de manera eficiente entre servidores y aplicaciones.

**2. Que es el DOM?**  
El DOM (Document Object Model) es una interfaz de programación que representa los documentos HTML o XML como una estructura de árbol lógica.  
  
  Permite que JavaScript acceda, lea y modifique dinámicamente el contenido, la estructura y el estilo de una página web cargada en el navegador.

**3. Que es el ambito de una variable y cual es el ambito de las variables de declaradas con let?**  
El Ámbito (Scope) de una variable es la región del código que determina su visibilidad y accesibilidad.

El ámbito de las variables declaradas con let es de Bloque (Block Scope), lo que significa que solo son accesibles dentro del bloque de llaves {} (como un if o for) en el que fueron definidas.

**4. Cuales son los mecanismos que posee Javascript para manejar el codigo asincrono?**  
JavaScript posee tres mecanismos principales para manejar el código asíncrono:

Callbacks: Funciones de retorno, la técnica original, usada para ejecutar código tras completar una operación asíncrona.

Promesas (Promises): Objetos que representan el resultado eventual de una operación; manejan éxito y error mediante .then() y .catch().

async/await: Una sintaxis moderna (basada en Promesas) que permite escribir código asíncrono de forma más legible, haciéndolo parecer síncrono.

**5. En javascript que es un modulo? Menciona dos sistemas usados actualmente**  
Un Módulo en JavaScript es un archivo individual que encapsula código, permitiendo la reutilización y el aislamiento de variables, funciones o clases, ya que todo lo definido en él es privado por defecto a menos que se exporte explícitamente.

Actualmente, los dos sistemas de módulos más utilizados en el ecosistema JavaScript son:

Módulos ES (ESM):  
Es el estándar oficial introducido en ECMAScript 2015 (ES6).  
Utiliza la sintaxis import y export.   
Ejemplo: import { miFuncion } from './archivo.js';

CommonJS (CJS):
Es el sistema de módulos original de Node.js (entorno de servidor).  
Utiliza la sintaxis require() para importar y module.exports o exports para exportar.  
Ejemplo: const miFuncion = require('./archivo.js');

