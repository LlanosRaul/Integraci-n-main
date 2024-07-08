![logo](https://www.ferreteriavillamor.com/uploads/v3kjz6zp/766x0_2560x0/banner-ferreteria.jpg)

<!-- SECCION ¿QUE ES FERRAMAS? -->

<h1 align="center">Ferramas</h1>
<h3>¿Que es Ferramas?</h3>
<p>FERREMAS es una distribuidora de productos de construcción y ferretería establecida en la comuna de Santiago desde la década de los 80. Con 4 sucursales en la región metropolitana y 3 en regiones, FERREMAS ofrece una amplia gama de productos, incluyendo herramientas manuales y eléctricas, pinturas, materiales eléctricos, y artículos de seguridad.
</p>
<p>En FERREMAS trabajamos con marcas reconocidas como Bosch, Makita, Stanley y Sika, garantizando la calidad y variedad de nuestros productos.
</p>
<p>Contamos con una estructura organizativa clara, con roles definidos para administradores, vendedores, bodegueros y contadores, cada uno con responsabilidades específicas en la gestión de ventas, pedidos, inventario y finanzas.

FERREMAS está comprometida con la expansión y evolución constante para ofrecer un mejor servicio a nuestros clientes en todo Chile.
</p>

<br>

<!-- FIN SECCION ¿QUE ES FERRAMAS? -->


<!-- SECCION NUESTRO EQUIPO -->

<h1 align="center">Nuestro Equipo</h1>

<p>Este repositorio contiene el código fuente de FERREMAS, una aplicación web desarrollada como parte del curso de Integración de Plataformas. FERREMAS está diseñada para facilitar la gestión eficiente de datos a través de una interfaz intuitiva y moderna. Nos enfocamos en integrar tecnologías avanzadas para asegurar una plataforma robusta y escalable que cumpla con las demandas actuales del desarrollo web.</p>

<img align="right" alt="Coding" width="400" src="https://user-images.githubusercontent.com/74038190/229223263-cf2e4b07-2615-4f87-9c38-e37600f8381a.gif">

<h3 align="left" style="font-size: 21px;">Integrantes del Equipo:</h3>
<br>

- **👨‍💻 Raul Llanos / [LinkedIn](https://www.linkedin.com/in/raul-patricio-llanos-vergara-b22aa1252)**
- **👨‍💻 Matias Muñoz / [LinkedIn](https://www.linkedin.com/in/matias-ignacio-munoz-lillo-69b253250/)**
- **👨‍💻 Felipe Vaccaro / [LinkedIn](https://www.linkedin.com/in/felipe-vaccaro-miranda-2b1a541ba/)**
<br>

<!-- FIN SECCION NUESTRO EQUIPO -->

<br><br><br>
<br><br><br>
<br><br><br>
<br><br><br>


<!-- SECCION ARQUITECTURA UTILIZADA -->

<h1 align="center">Arquitectura Utilizada</h1>
<br>

<p>Para nuestro proyecto se basa en la arquitectura MVC (Modelo-Vista-Controlador), utilizando como framework principal Django, en conjunto con Python para la la lógica de negocio y sus controladores. Con esta arquitectura nos separa la lógica de negocio, controladores y las vistas. La persistencia de datos se gestiona a través de MySQL, integrando Django ORM para facilitar la interacción con la base de datos de manera eficiente.</p>

<!-- FIN SECCION ARQUITECTURA UTILIZADA -->

<br><br>
<img src="https://i.imgur.com/dBaSKWF.gif" height="20" width="100%">
<img src="https://i.imgur.com/dBaSKWF.gif" height="20" width="100%">


<!-- SECCION TECNOLOGIAS UTILIZADAS -->

<h3 align="center" style="font-size: 24px;">Lenguajes / Frameworks:</h3>
<br>

<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=html,python,django,js,css" />
  </a>
</p>

<h3 align="center" style="font-size: 24px;">Tecnologías Utilizadas:</h3>
<br>

<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=git,github,vscode" />
  </a>
      <img src="https://cdn2.iconfinder.com/data/icons/pack1-baco-flurry-icons-style/512/XAMPP.png" style="width: 50px; height: 50px;" />
</p>

<h3 align="center" style="font-size: 24px;">Base de Datos Utilizada:</h3>
<br>

<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=mysql" style="width: 50px; height: 50px;" />
  </a>
</p>


<!-- FIN SECCION TECNOLOGIAS UTILIZADAS -->

<img src="https://i.imgur.com/dBaSKWF.gif" height="20" width="100%">
<img src="https://i.imgur.com/dBaSKWF.gif" height="20" width="100%">


<!-- SECCION PASOS DE IMPLEMENTACION -->

# Pasos de Implementación

## Pre-requisitos

Asegúrate de tener instaladas las siguientes herramientas:

- Visual Studio Code
- Python
- Setuptools actualizado
- Django
- XAMPP
- MySQL Workbench 8.0 CE

## Paso a Paso

### 1. Abrir Visual Studio Code

Navega a la raíz de la aplicación y abre Visual Studio Code desde allí.

### 2. Instalar dependencias

Ejecuta el siguiente comando para instalar las herramientas necesarias para el proyecto:

```bash
pip install -r requirements.txt
```

(Opcional) Puedes usar un entorno virtual ejecutando:

```bash
env\Scripts\activate
```

### 3. Iniciar MySQL con XAMPP

Abre XAMPP y haz clic en "Start" en el módulo de MySQL.

### 4. Conectar MySQL Workbench con XAMPP

Abre MySQL Workbench y crea una nueva conexión para conectarla con el servidor MySQL iniciado por XAMPP.

### 5. Crear una nueva base de datos en MySQL Workbench

Una vez conectado, crea una nueva base de datos donde se almacenarán las tablas del proyecto.

### 6. Actualizar la base de datos

Haz un "Refresh" en MySQL Workbench para asegurarte de que la nueva base de datos aparezca en la lista de bases de datos.

### 7. Cargar el script de categoría en MySQL Workbench

En Visual Studio Code, abre el archivo de script de categoría que se encuentra en la carpeta Scripts. Copia el contenido completo del archivo (CTRL+A, CTRL+C). Pega el script en el área de consulta (Query) de MySQL Workbench y ejecútalo para crear la tabla producto_categoria.

### 8. Cargar el script de productos en MySQL Workbench

En Visual Studio Code, abre el archivo de script de productos que se encuentra en la carpeta Scripts. Copia el contenido completo del archivo (CTRL+A, CTRL+C). Pega el script en el área de consulta (Query) de MySQL Workbench y ejecútalo para crear la tabla producto_producto.

### 9. Migrar la base de datos con Django

Abre la consola desde la raíz de la aplicación y ejecuta el siguiente comando para aplicar las migraciones y poblar las tablas:

```bash
python manage.py migrate
```

### 10. Iniciar el servidor Django

Abre la consola y ejecuta el siguiente comando para iniciar el servidor:

```bash
python manage.py runserver
```
<br>
<!-- FIN SECCION PASOS DE IMPLEMENTACION -->
<br>

<img src="https://i.imgur.com/dBaSKWF.gif" height="20" width="100%">
<img src="https://i.imgur.com/dBaSKWF.gif" height="20" width="100%">

<!-- SECCION ACTIVIDAD DE LOS INTEGRANTES  -->

<h3 align="left" style="font-size: 21px;">Actividad de los Integrantes:</h3>
<br>

### Raul Llanos

<p align="center">
  <a href="https://github.com/LlanosRaul">
    <img src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=LlanosRaul&theme=radical" alt="Raul Llanos's GitHub Contribution"/>
  </a>
</p>


### Matias Muñoz

<p align="center">
  <a href="https://github.com/KEKEKEKEW">
    <img src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=KEKEKEKEW&theme=radical" alt="Matias Muñoz's GitHub Contribution"/>
  </a>
</p>


### Felipe Vaccaro

<p align="center">
  <a href="https://github.com/FelipeVaccaro">
    <img src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=FelipeVaccaro&theme=radical" alt="Felipe Vaccaro's GitHub Contribution"/>
  </a>
</p>


<!-- FIN SECCION ACTIVIDAD DE LOS INTEGRANTES -->


<img src="https://i.imgur.com/dBaSKWF.gif" height="20" width="100%">
<img src="https://i.imgur.com/dBaSKWF.gif" height="20" width="100%">


<!-- SECCION LICENCIA -->

<h3 align="center" style="font-size: 24px;">Licencia</h3>
 
<h3 align="center" style="font-size: 15px;">Este proyecto está licenciado bajo la Licencia MIT. Para más detalles, consulta el archivo LICENSE.</h3>
<br>

<!-- FIN SECCION LICENCIA -->

<img src="https://i.imgur.com/dBaSKWF.gif" height="20" width="100%">
<img src="https://i.imgur.com/dBaSKWF.gif" height="20" width="100%">

