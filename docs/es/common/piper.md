---
layout: page
title: common/piper (español)
description: "Un sistema neural rápido y local de conversión de texto a voz."
content_hash: 67637e3c03b16ed95ea2a3834772091486ac245c
last_modified_at: 2024-07-31
related_topics:
  - title: English version
    url: /en/common/piper.html
    icon: bi bi-globe
tldri18n_status: 2
---
# piper

Un sistema neural rápido y local de conversión de texto a voz.
Descarga y prueba modelos de habla desde <https://rhasspy.github.io/piper-samples>.
Más información: <https://github.com/rhasspy/piper>.

- Genera un archivo WAV utilizando un modelo de texto a voz (suponiendo un archivo de configuración en model_path + .json):

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Cosa a decir</span>` | piper -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/modelo.onnx</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo_de_salida.wav</span>

- Genera un archivo WAV utilizando un modelo y especificando su archivo de [c]onfiguración JSON:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'Lo que hay que decir'</span>` | piper -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/modelo.onnx</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/modelo.onnx.json</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo_de_salida.wav</span>

- Selecciona un locutor concreto en una voz con varios locutores especificando el número de identificación del locutor:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'Warum?'</span>` | piper -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">de_DE-thorsten_emotional-medium.onnx</span>` --speaker `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">enojado.wav</span>

- Transmite la salida al reproductor multimedia mpv:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'Hello world'</span>` | piper -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">en_GB-northern_english_male-medium.onnx</span>` --output-raw -f - | mpv -`

- Habla el doble de rápido, con grandes espacios entre frases:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'Hablando el doble de rápido. Con más drama!'</span>` | piper -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo.onnx</span>` --length_scale `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.5</span>` --sentence_silence `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">drama.wav</span>
