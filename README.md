YOZAKURA
========

京都大学メカトロニクス研究室メンバー
SHINOBI遠隔班
YOZAKURA

#Settings
##Contec  
**CONTEC access point (opstn side)     admin:pass**  
IP Address: 192.168.54.225  
IEEE802.11n (5 GHz)  44 channels  
コンパチブルインフラストラクチャ  
ESSID rrl_44ch_shinobi_tele  
WPA2-PSK(AES)  
1:8  

**CONTEC station (YOZAKURA side)     blank**  
IP Address: 192.168.54.220  
IEEE802.11n (5GHz)  
コンパチブルインフラストラクチャ  
ESSID rrl_44ch_shinboi_tele  
WPA2-PSK(AES)  
1:8  

##PC  
**Operator Station PC**  
IP Address: 192.168.54.200

**Robot PC (Jetson TK1)**  
IP Address: 192.168.54.210  

##Camera
**Video Server for RICOH THETA S**  
IP Address: 192.168.54.150  

## Others  
**URG(UST-10LX)**  
IP Address: 192.168.54.170  
ref:  
https://www.hokuyo-aut.co.jp/02sensor/07scanner/ust_10lx_20lx.html  
https://www.hokuyo-aut.co.jp/02sensor/07scanner/download/ust-10lx_spec.pdf  
http://www.hokuyo-aut.co.jp/02sensor/07scanner/download/pdf/UST_protocol_ja.pdf
http://www.hokuyo-aut.co.jp/02sensor/07scanner/download/data/UrgBenri_ja.htm  

##mbed
<img src="http://nora66.com/mbed/pinout.png" alt="mbedLPC1768 Pinout Diagram" width="400x" align="right">
**Arm mbed**
* p5:mosi SPI
* p6:miso SPI
* p7:sck SPI
* p11:mosi SPI
* p12:miso SPI
* p18:sck SPI

**Body mbed**
* p23: Left baek PWM
* p24: Right back PWM
* p25: left front PWM
* p26: Right front motor PWM
* p26: Right front motor DIR
* p25: left front DIR
* p24: Right back DIR
* p23: Left baek DIR

#Jetson Setup
See SHINOBI page for more references
