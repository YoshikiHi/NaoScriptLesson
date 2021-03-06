# NaoScriptLesson
## About this repository
These Python scripts for running on "**Choregraphe PythonBox**".

## About File information
**Please Check your local environment and change IP Address , Port Number**<br>
※ IP Address is **string** / Port Number is **Number**<br>
=============================================<br>
def \_\_init\_\_(self):<br>
　  ...<br>
　  ALProxy("〜〜〜","***RobotIPAddr***",***RobotPort***)<br>
　  ...<br>
=============================================<br>

The following is a description of the file.
- SpeakHello<span>.</span>py<br>
    This script is the easiest script in NaoProgramming.
    When you run this script, Nao greets you.<br>
    Nao talks in the language of the default setting.

    This script uses 「ALTextToSpeach」API.

- Postures<span>.</span>py<br>
    It is a simple script that changes the attitude of Nao.
    First, If your Nao Robot is not sitting , Nao will sit ground.
    If Nao can sit down, Nao waits 1 seconds.
    Finaly,Nao will stand up.

    This script uses 「ALRobotPosture」API.<br>
    I used *Predefined postures* this time. If you want to change the others posture,the following pages will be helpful.<br>
    http://doc.aldebaran.com/2-1/family/robots/postures_robot.html#robot-postures

- ArmMove<span>.</span>py<br>
    It is a script to easily adjust the position of the right arm.<br>
    I am assuming handshake between NAO and you.

    This script uses 「ALMotion」API.<br>
    For this example script, I applied motion to the right arm as an example. (Use **RShoulderPitch** and **RShoulderRoll**)<br>
    If you want to moving the others part of NAO, the following pages will be helpful.<br>
    http://doc.aldebaran.com/2-1/family/nao_dcm/actuator_sensor_names.html#actuator-sensor-list-nao

# Supplement
## Install Choregraphe
Please refer to the following,how to install Choregraphe.<br>
https://www.softbank.jp/robot/consumer/support/trouble/data/choregraphe/

## API Information
Please check the APIs and functions you want to use from the following.<br>
http://doc.aldebaran.com/2-1/naoqi/index.html


