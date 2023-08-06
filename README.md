# MapReduce-приложение, вычисляющее отчет на каждый месяц по [данным желтого такси](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)
## Описание проекта
MapReduce-приложение, использующее скопированные на HDFS [данные](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page) и вычисляющееотчет на каждый месяц 2020 года вида:

| Month   	| Payment type 	| Tips average amount 	|
|---------	|--------------	|---------------------	|
| 2020-01 	| Credit card  	| 999.99              	|

## Использованные инструменты
Hadoop, Python

## Файлы
**mapper.py** - мэппер

**reducer.py** - редьюсер

**run.sh** - скрипт для запуска приложения
