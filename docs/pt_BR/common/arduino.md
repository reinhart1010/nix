---
layout: page
title: common/arduino (português (Brasil))
description: "Arduino Studio - Ambiente de Desenvolvimento Integrado para a plataforma Arduino."
content_hash: 91db2dba54a82a8d94385b24393d7f53b4505ac9
last_modified_at: 2023-12-17
related_topics:
  - title: English version
    url: /en/common/arduino.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/arduino.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># arduino

Arduino Studio - Ambiente de Desenvolvimento Integrado para a plataforma Arduino.
Mais informações: <https://github.com/arduino/Arduino/blob/master/build/shared/manpage.adoc>.

- Compilar um sketch:

`arduino --verify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.ino</span>

- Compilar e enviar sketch:

`arduino --upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.ino</span>

- Compilar e enviar sketch para um Arduino Nano com uma CPU Atmega328p, conectada na porta `/dev/ttyACM0`:

`arduino --board `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arduino:avr:nano:cpu=atmega328p</span>` --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/ttyACM0</span>` --upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.ino</span>

- Definir a preferência `nome` para um determinado `valor`:

`arduino --pref `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valor</span>

- Compilar um sketch, colocar o resultado da compilação no diretório de compilação, e reutilizar qualquer resultado pre-existente neste diretório:

`arduino --pref build.path=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório</span>` --verify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.ino</span>

- Salvar todas as preferências (alteradas) para `preferences.txt`:

`arduino --save-prefs`

- Instalar a última placa SAM:

`arduino --install-boards "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arduino:sam</span>`"`

- Instalar bibliotecas Bridge e Servo:

`arduino --install-library "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Bridge:1.0.0,Servo:1.2.0</span>`"`
