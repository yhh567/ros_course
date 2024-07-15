#!/bin/bash

cd /home/user/catkin_ws/src/linux_exam/this/is/my/linux/exam

# Borrar todo el contenido del fichero exam
rm /home/user/catkin_ws/src/linux_exam/this/is/my/linux/exam/*

# Crear 3 nuevos ficheros
touch exam1.py exam2.py exam3.py

# Permisos fichero 1
chmod 754 exam1.py

# Permisos fichero 2
chmod 501 exam2.py

# Permisos fichero 3
chmod 241 exam3.py