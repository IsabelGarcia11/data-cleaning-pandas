# data-cleaning-pandas

<img src = "FOTOS/ok.jpeg" width="600" height="200">

**OBJETIVO**

El objetivo del proyecto es el análisis y limpieza de una base de datos que contiene registros de los ataques de tiburón a lo largo del tiempo obtenidos en [kaggle.](https://www.kaggle.com/teajay/global-shark-attacks)

**HIPÓTESIS**

De cara al análisis de los datos me he centrado en tres hipótesis que quería contrastar.

* Los registros se concentran periodos y en meses determinados.
* La edad y el sexo influyen en la posibilidad de que el ataque sea fatal.
* Los ataques de tiburón se concentran en determinados países y la letalidad es diferente en cada uno de ellos.

Para llevarlo a cabo he utilizado dos Jupiter Noteboook, uno el que he llevado a cabo la limpieza de los datos (pandas-cleaning) y otro en el que he contrastado mis hipótesis mediante gráficos(Vis-pandas).

### Pandas-cleaning

<img src = "FOTOS/panda.jpg" width="500" height="200">

Una vez descargado el CSV de los ataques de tiburón, he eliminado aquellas filas en los que todos los valores eran NaN. 
Posteriormente he seleccionado aquellas columnas que tenía que analizar para contrastar mis hipótesis y las he limpiado unificando su contenido para poder tratar los datos. En el jupiter está detallado los pasos que he ido siguiendo.

### Vis-pandas

Con los datos ya analizados, he utilizado las librerias de Seaborn y Matplotlib para hacer los diferentes gráficos que constatan mis diferentes hipótesis.

**LINKS & RESOURCES**
* https://www.kaggle.com/teajay/global-shark-attacks
* https://numpy.org/doc/1.18/
* https://pandas.pydata.org/
* https://docs.python.org/3/library/functions.html
* https://matplotlib.org/
* https://seaborn.pydata.org/
* https://pandas.pydata.org/docs/

