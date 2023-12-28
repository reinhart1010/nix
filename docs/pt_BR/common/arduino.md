---
layout: page
title: common/arduino (português (Brasil))
description: "Arduino Studio - Ambiente de Desenvolvimento Integrado para a plataforma Arduino."
content_hash: decd00726cffb535229f4fc1f030416048297ef8
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/common/arduino.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/arduino.html
    icon: bi bi-globe
tldri18n_status: 2
---
# arduino

Arduino Studio - Ambiente de Desenvolvimento Integrado para a plataforma Arduino.
Mais informações: <https://github.com/arduino/Arduino/blob/master/build/shared/manpage.adoc>.

- Compila um sketch:

`arduino --verify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.ino</span>

- Compila e envia sketch:

`arduino --upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.ino</span>

- Compila e envia sketch para um Arduino Nano com uma CPU Atmega328p, conectada na porta `/dev/ttyACM0`:

`arduino --board `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arduino:avr:nano:cpu=atmega328p</span>` --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/ttyACM0</span>` --upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.ino</span>

- Define a preferência `nome` para um determinado `valor`:

`arduino --pref `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valor</span>

- Compila um sketch, coloca o resultado da compilação no diretório de compilação, e reutiliza qualquer resultado pre-existente neste diretório:

`arduino --pref build.path=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório</span>` --verify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.ino</span>

- Salva todas as preferências (alteradas) para `preferences.txt`:

`arduino --save-prefs`

- Instala a última placa SAM:

`arduino --install-boards "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arduino:sam</span>`"`

- Instala bibliotecas Bridge e Servo:

`arduino --install-library "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Bridge:1.0.0,Servo:1.2.0</span>`"`
