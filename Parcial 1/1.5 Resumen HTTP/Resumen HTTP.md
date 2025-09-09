# Resumen HTTP

## Que es HTTP?
HTTP (HyperText Transfer Protocol) es el protocolo de comunicación que se utiliza en la web para la transferencia de información entre un cliente (como un navegador) y un servidor web.

## Estructura de una peticion
Método Ruta Versión  
Encabezados  
(Cuerpo, opcional)

Ej.   
GET /index.html HTTP/1.1  
Host: www.ejemplo.com  
User-Agent: Chrome/104  

## Metodos mas usados
**GET**: Solicita datos del servidor (leer).  
**POST**: Envía datos al servidor (crear).  
**PUT**: Actualiza un recurso existente.  
**DELETE:** Elimina un recurso.  
**PATCH**: Modifica parcialmente un recurso.  
**HEAD** Similar a GET pero solo trae encabezados.  
**OPTIONS**: Consulta los métodos permitidos para un recurso.

## Codigos de estado
Algunos comunes:

### 1xx (Informativos): 
Ej. 100 Continue.

### 2xx (Éxito):
200 OK  
201 Created

### 3xx (Redirección):
301 Moved Permanently  
302 Found

### 4xx (Errores del cliente):
400 Bad Request  
401 Unauthorized  
403 Forbidden  
404 Not Found

### 5xx (Errores del servidor):     
500 Internal Server Error  
502 Bad Gateway

## Encabezados 
Los encabezados HTTP son pares clave-valor que proporcionan información adicional sobre la petición o la respuesta.

Ejemplo:  
Content-Type: application/json  
Authorization: Bearer token123

## Estructura de una URL

protocolo://host:puerto/ruta?query#fragmento

Ej.  
https://www.ejemplo.com:443/productos?id=5#descripcion  

**Protocolo**: https  
**Host**: www.ejemplo.com
**Puerto**: 443 (opcional)  
**Ruta**: /productos  
**Query**: ?id=5  
**Fragmento**: #descripcion