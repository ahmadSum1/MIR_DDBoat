

Librairies arduino IDE :
- FlashStorage
- SparkFun_MPU-9250-DMP_Arduino_Library-master

Le dossier script_ddboat_rapberry contient tous les scripts python qui s'exécute sur la raspberry et
permettent de manipuler le gps, l'imu ou encore les moteurs.
Dans ce dossier nous avons : 
- arduinodriver.py : qui permet de commander les moteurs via l'arduino
- gps_drivers_py3.py : driver permettant de manipuler le GPS
- imu_drivers_py3_V2.py : driver permettant de manipuler l'imu, avec ce driver, on obtient toutes les 9 valeurs de l'imu
- imu_drivers_py3.py : driver permettant de manipuler l'imu, avec ce driver, on obtient que trois valeurs de l'imu

De meme le dossier script_ddboat_arduino, contient le script qui a été téléversé sur l'arduino à savoir script_arduino.ino.

De plus dans le dossier courant on :

- Dossier razor: dossier contenant les scripts arduino téléversés sur l'imu.
- rapport_technique.pdf qui est le rapport résumant les manipulations éffetuées sur le ddboat.
- script_arduino_commente.pdf : la version bien commenté su script script_arduino.ino
- script_raspberry_commente.pdf : la version bien commenté su script arduinodriver.py
