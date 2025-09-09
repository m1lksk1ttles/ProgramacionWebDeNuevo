# Unidades de Medida en CSS

Las unidades de medida en CSS se dividen principalmente en absolutas (como px, cm, mm) y relativas (como em, rem, %), y también existen las unidades de ventana gráfica (vw, vh, vmin, vmax).   
Las unidades absolutas son fijas, mientras que las relativas se basan en un valor de referencia (como el tamaño de fuente o del viewport) para crear diseños más adaptables. 

## Unidades Absolutas

Estas aunque le muevas al diseno o tamano de la pagina, este no se vera afectado  

|Unidad | Nombre| Equivale A |
|------------|------------|------------|  
|cm 	|Centímetros 	|1cm = 96px/2,54  
|mm 	|Milímetros 	|1mm = 1/10 de 1cm  
|Q 	|Cuartos de milímetros 	|1Q = 1/40 de 1cm  
|in 	|Pulgadas 	|1in = 2,54cm = 96px  
|pc 	|Picas 	|1pc = 1/6 de 1in  
|pt 	|Puntos 	|1pt = 1/72 de 1in  
|px 	|Píxeles 	|1px = 1/96 de 1in  

Te sirven mas cuando hay datos o elementos que no quieras que se muevan.

## Unidades Relativas 

Las unidades de longitud relativa son relativas a algo más, por ejemplo, al tamaño de letra del elemento principal o al tamaño de la ventana gráfica. 

| Unidad | Equivale A |  
|--------|------------|
em 	| Tamaño de letra del elemento padre, en el caso de propiedades tipográficas como font-size, y tamaño de la fuente del propio elemento en el caso de otras propiedades, como width.
ex 	| Altura x de la fuente del elemento.
ch 	| La medida de avance (ancho) del glifo "0" de la letra del elemento.
rem 	| Tamaño de la letra del elemento raíz.
lh 	| Altura de la línea del elemento.

## Unidades Graficas

Estas tecnicamente son relativas porque representan una parte de algo, pero es diferente.

| Unidad | Equivale A |  
|--------|------------|
vw 	|1% del ancho de la ventana gráfica.
vh 	|1% de la altura de la ventana gráfica.
vmin 	|1% de la dimensión más pequeña de la ventana gráfica.
vmax 	|1% de la dimensión más grande de la ventana gráfica.