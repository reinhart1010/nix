---
layout: page
title: linux/asciiart (Deutsch)
description: "Konvertiere Bilder zu ASCII."
content_hash: b24c4ee44a9741a969cac99091dd96485e98865b
related_topics:
  - title: English version
    url: /en/linux/asciiart.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/asciiart.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/asciiart.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/asciiart.html
    icon: bi bi-globe
---
# asciiart

Konvertiere Bilder zu ASCII.
Weitere Informationen: <https://github.com/nodanaonlyzuul/asciiart>.

- Lese ein Bild aus einer Datei und zeige es als ASCII:

`asciiart `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zur/datei.jpg</span>

- Lese ein Bild aus einer URL und zeige es als ASCII:

`asciiart `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">www.example.com/bild.jpg</span>

- Wähle die Breite der Ausgabe (standardmäßig 100):

`asciiart -width `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">50</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zum/bild.jpg</span>

- Zeige die Ausgabe in Farbe:

`asciiart --color `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zum/bild.jpg</span>

- Wähle das Ausgabeformat (standardmäßig text):

`asciiart --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">text|html</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zum/bild.jpg</span>

- Invertiere die Zeichentabelle:

`asciiart --invert-chars `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zum/bild.jpg</span>
