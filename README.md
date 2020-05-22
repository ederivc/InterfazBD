# **INTERFAZ DE BASE DE DATOS**

Este programa es una aplicacion de usuario el cual le ayudará a tener un mejor control sobre sus empleados, proveedores, productos y ventas. Teniendo la opción de poder agregar y modificar, asi como realizar ventas. De igual manera se podrá consultar todo tipo de dato introducido o modificado en el programa.
___

## Inicio de sesion

En el primer apartado se cuenta con un inicio de sesion, el cual lo llevará a la base de datos al momento de introducir el usuario y la contraseña correctamente, en caso conrtario, no lo dejará avanzar y marcará error.

___

## Página Principal

La pagina principal cuenta con diferentes apartados los cuales nos podran ayudar a interactuar con la base de datos como con la tienda. 

| Campo | Accion |
| ------ | ------ |
| Agregar | Empleados, Proveedores y Productos |
| Mostrar | Empleado, Proveedor, Producto, Ventas, Conceptos, Productos a ordenar|
| Modificar o eliminar | Empleado, Proveedores y Productos |
| Categorias | Formas de pago y Productos |
| Ventas | Registrar ventas |

___

## Agregar

En la seccion de agregar encontramos tres apartados: *Empleado*, *Proveedor* *y* *Producto*

- **Empleado**

    - ID: En este apartado se tiene que introducir el ID o clave del empleado la cual es numerica.
    - Nombre: Nombre del empleado
    - Apellido Paterno: Apellido paterno del empleado
    - Apellido Materno: Apellido materno del empleado
    - RFC: RFC del empleado
    - Fecha de Nacimiento: Fecha en la que nació el empleado
    - Fecha de Ingreso: Fecha en la que comienza a trabajar el empleado
    - Ciudad: Ciudad de nacimiento
    - Estado: Estado donde nació
    - País: País de origen 
    - Calle: Calle del domicilio del empleado
    - Colonia: Colonia donde recide
    - CP: Código postal de su domicilio
    - Telefono: Telefono del empleado
    - Sueldo: Sueldo que tendra el empleado
***En caso de introducir datos incorrecto o un empleado ya existente, el programa marcará error y no dejará registrar al empleado.***

- **Proveedor**

    - Clave: En este apartado se tiene que introducir la clave del proveedor la cual es numerica.
    - Nombre: Nombre del proveedor
    - Apellido Paterno: Primer apellido del proveedor
    - Apellido Materno: Segundo Apellido de proveedor
    - RFC: RFC del proveedor
    - Teléfono: Teléfono del proveedor
    - Nombre Empresa: Nombre de la empresa donde el proveedor trabaja
    - Ciudad: Ciudad de nacimiento
    - Calle: Calle de su domicilio
    - Colonia: Colonia donde recide
    - CP: Código postal de su colonia
***En caso de introducir datos incorrectos o un proveedor ya existente, el programa marcará error y no dejará registrar al proveedor.***

- **Productos**
    - Código de barras: Codigo del producto a registrar, el cual debe ser numerico
    - Nombre: Nombre del producto
    - Marca: Marca del producto
    - Existencia: Cantidad con la que se contara inicialmente
    - Costo: Costo de compra
    - Precio Venta: Precio de venta al publico
    - Punto de Reorden: Cantidad en la que se tiene que ordenar nuevamente el producto
    - Proveedor: Proveedor de este producto 
    - Categoria: Categoria a la que pertenece el producto, *Refrescos, Cerveza, Botana o Abarrotes*
***En caso de introducir datos incorrectos o un producto ya existente, el programa marcará error y no dejará registrar al producto.***

___

## Mostrar

En esta parte de la interfaz el usuario podrá ver las diferentes tablas con su respectiva información.

| Tabla | Datos mostrados |
| ------ | ------ |
| Empleado | *Todos sus datos* |
| Proveedor | *Todos sus datos*|
| Producto | *Todos sus datos* |
| Ventas | Clave de venta, importe total, fecha de venta, forma de pago, clave de empleado |
| Concepto | Clave de venta, código del producto, cantidad, precio unitario, importe |
| Productos a ordenar | Todos los datos de los productos debajo de su punto de reorden |

***En el caso de las ventas, se podrán consultar por día, semana, mes o todas las ventas***

___

## Modificar o eliminar

En este apartado el usuario podrá encontrar un diseño bastante similar al de **Agregar**, el cual el programa le permitirá modificar o eliminar *Empleados, Proveedores o Productos*.
Para poder modificar o eliminar, solo bastara con introducir el código o ID del *Empleado, Proveedor o Producto*, y presionar *Enter*, y automaticamente el programa llenará todos los demás campos.
Se podra modificar desde uno o todos los atributos, con excepción del código o ID.

***En caso de introducir un código o ID que no exista en la base de datos, o introducir datos incorrectos, el programa marcará error y no permitirá modificar o eliminar.***

## Categorías

Este apartado permite al usuario visualizar el contenido de dos tablas con sus respectivos datos.

| Tabla| Datos mostrados |
| ------ | ------ |
| Formas de Pago| Clave de venta, forma de pago de la venta  |
|  Productos | ID del producto, categoría a la que pertenece |

***Este apartado es una manera sencilla de poder visualizar las ventas ordenadas por formas de pago y los productos ordenados por categorías.***

___

## Ventas

En este apartado se encuentra una opción llamada **Realizar venta** en la cual, como indica su nombre, se podran realizar ventas de los productos que existen en la base de datos. Las ventas podrán ser por un solo producto o por varios.
Esta opcion cuenta de con diferentes apartados.

- Clave venta: Clave de venta la cual es numerica
- Código de barras producto: ID del producto que se venderá
- Cantidad: Cantidad que se desea vender
- Precio Unitario: Precio unitario del producto
- Importe: Importe venta del producto
- Fecha venta: Fecha en la que se realizará la venta
- Forma pago: Forma de pago 
- Clave empleado: Clave del empleado que realiza la venta

Al momento de que el usuario introduzca la clave del producto y la cantidad, y a continuación presione *Tabulador*, automaticamente el precio unitario y el importe se actualizaran.
Para poder realizar una venta primeramente se tendra que añadir el producto o producto al carrito, y posteriormente hacer click en *Realizar venta*.

***En caso de introducir datos incorrectos, clave de venta repetida o un producto que no existe, el programa marcará error y no podrá realizar la venta.***
