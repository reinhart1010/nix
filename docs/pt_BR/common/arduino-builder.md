---
layout: page
title: common/arduino-builder (português (Brasil))
description: "Uma ferramenta de linha de comando para compilar sketches do arduino."
content_hash: 9411b6ea5b9bc8db16bd982eab6ff0f6b7249dbf
related_topics:
  - title: English version
    url: /en/common/arduino-builder.html
    icon: bi bi-globe
---
# arduino-builder

Uma ferramenta de linha de comando para compilar sketches do arduino.
AVIDO DE OBSOLESCÊNCIA: Esta ferramenta está sendo descontinuada e substituida pelo `arduino`.
Mais informações: <https://github.com/arduino/arduino-builder>.

- Compilar um sketch:

`arduino-builder -compile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/sketch.ino</span>

- Definir o nível de debug (1 a 10, o padrão é 5):

`arduino-builder -debug-level `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nivel</span>

- Definir um diretório de compilação customizado:

`arduino-builder -build-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretorio</span>

- Usar um arquivo com as opções de compilação, em vez de especificar `--hardware`, `--tools`, etc. manualmente toda hora:

`arduino-builder -build-options-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/build.options.json</span>

- Habilitar o modo verboso:

`arduino-builder -verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>
