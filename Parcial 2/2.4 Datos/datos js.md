
# Tipos de Datos en JavaScript



## Tipos Primitivos

Los **tipos primitivos** son inmutables y se acceden directamente por su valor.

### 1. `String`
Representa texto. Se define entre comillas simples, dobles o invertidas.

```js
let nombre = "Juan";
let saludo = `Hola ${nombre}`;
```

---

### 2. `Number`
Representa valores numéricos, tanto enteros como decimales.

```js
let edad = 25;
let precio = 99.99;
```

Incluye valores especiales:
- `Infinity`
- `-Infinity`
- `NaN` (Not a Number)

---

### 3. `BigInt`
Permite manejar números enteros muy grandes (mayores que `2^53 - 1`).

```js
let grande = 1234567890123456789012345678901234567890n;
```

---

### 4. `Boolean`
Solo puede tener dos valores: `true` o `false`.

```js
let esMayor = true;
let tienePermiso = false;
```

---

### 5. `Undefined`
Una variable declarada pero no inicializada tiene el valor `undefined`.

```js
let x;
console.log(x); // undefined
```

---

### 6. `Null`
Representa la ausencia intencional de un valor.

```js
let usuario = null;
```

>  `typeof null` devuelve `"object"` por compatibilidad histórica.

---

### 7. `Symbol`
Usado para crear identificadores únicos.

```js
let id = Symbol("id");
let otroId = Symbol("id");
console.log(id === otroId); // false
```

---

## Tipos No Primitivos (Objetos)

Los **objetos** son estructuras más complejas que pueden contener múltiples valores.

### 1. `Object`
Estructura clave-valor.

```js
let persona = {
  nombre: "Juan",
  edad: 25
};
```

---

### 2. `Array`
Colección ordenada de elementos.

```js
let numeros = [1, 2, 3, 4, 5];
```

---

### 3. `Function`
Las funciones también son objetos.

```js
function saludar() {
  return "Hola mundo";
}
```

---

### 4. `Date`
Representa fechas y horas.

```js
let hoy = new Date();
```

---

### 5. `RegExp`
Expresiones regulares para coincidencias de texto.

```js
let patron = /abc/;
```

---

### 6. `Map` y `Set`
Estructuras de datos modernas:

```js
let mapa = new Map();
mapa.set("clave", "valor");

let conjunto = new Set([1, 2, 3]);
```

---

## Tipado Dinámico

JavaScript es un lenguaje **de tipado dinámico**, lo que significa que el tipo de una variable puede cambiar en tiempo de ejecución:

```js
let dato = 42;      // Number
dato = "cuarenta";  // String
```

