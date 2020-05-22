CREATE TABLE employee(
  id INT UNIQUE,
  nombreEmp VARCHAR(45),
  apPatEmp VARCHAR(45),
  apMatEmp VARCHAR(45),
  rfcEmp VARCHAR(13),
  fechaNacEmp DATE,
  fechaIngEmp DATE,
  ciudadEmp VARCHAR(25),
  estadoEmp VARCHAR(25),
  paisEmp VARCHAR(25),
  calleEmp VARCHAR(25),
  coloniaEmp VARCHAR(25),
  cpEmp INT,
  telEmp INT,
  sueldoEmp FLOAT(20,4)
);

CREATE TABLE product(
  codigoProd INT UNIQUE,
  nombre VARCHAR(45),
  marca VARCHAR(45),
  existencia INT,
  costo FLOAT(20,4),
  precioventaProd FLOAT(20,4),
  reordenProd INT,
  proveedor VARCHAR(45),
  categoria VARCHAR(45)
);


CREATE TABLE supplier(
  claveProv INT UNIQUE,
  nombreProv VARCHAR(45),
  apPatProv VARCHAR(45),
  apMatProv VARCHAR(45),
  rfcProv VARCHAR(13),
  telefonoProv INT,
  empresaProv VARCHAR(45),
  ciudadProv VARCHAR(25),
  calleProv VARCHAR(25),
  coloniaProv VARCHAR(25),
  cpProv INT
);

CREATE TABLE sales(
  clave INT UNIQUE,
  importeT FLOAT(20,4),
  fecha DATE,
  fPago VARCHAR(20),
  claveEmp INT
);


CREATE TABLE transaction(
  clave INT,
  codigoProd INT,
  cantidad INT, 
  precioUni FLOAT(20,4),
  importe FLOAT(20,4)
);
