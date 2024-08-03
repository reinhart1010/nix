---
layout: page
title: common/arduino-builder (português (Brasil))
description: "Uma ferramenta de linha de comando para compilar sketches do arduino."
content_hash: 8746e9fee19fde79708228c43c657bf7ba43116e
last_modified_at: 2024-08-03
related_topics:
  - title: English version
    url: /en/common/arduino-builder.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/arduino-builder.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/arduino-builder.html
    icon: bi bi-globe
tldri18n_status: 2
---
# arduino-builder

Uma ferramenta de linha de comando para compilar sketches do arduino.
AVIDO DE OBSOLESCÊNCIA: Esta ferramenta está sendo descontinuada e substituida pelo `arduino`.
Mais informações: <https://github.com/arduino/arduino-builder>.

- Compila um sketch:

`arduino-builder -compile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/sketch.ino</span>

- Define o nível de debug (1 a 10, o padrão é 5):

`arduino-builder -debug-level `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nivel</span>

- Define um diretório de compilação customizado:

`arduino-builder -build-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretorio</span>

- Usa um arquivo com as opções de compilação, em vez de especificar `-hardware`, `-tools`, etc. manualmente toda hora:

`arduino-builder -build-options-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/build.options.json</span>

- Habilita o modo verboso:

`arduino-builder -verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>
