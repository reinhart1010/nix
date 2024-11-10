---
layout: page
title: linux/rpi-eeprom-update (한국어)
description: "EEPROM을 업데이트하고 다른 EEPROM 정보를 확인합니다."
content_hash: fd5bbca29c3121e0037a6432e23771bd8d91f2e5
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/rpi-eeprom-update.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/rpi-eeprom-update.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rpi-eeprom-update

EEPROM을 업데이트하고 다른 EEPROM 정보를 확인합니다.
더 많은 정보: <https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#rpi-eeprom-update>.

- 현재 설치된 라즈베리 파이 EEPROM 정보 출력:

`sudo rpi-eeprom-update`

- 라즈베리 파이 EEPROM 업데이트:

`sudo rpi-eeprom-update -a`

- 보류 중인 업데이트 취소:

`sudo rpi-eeprom-update -r`

- 도움말 표시:

`rpi-eeprom-update -h`
