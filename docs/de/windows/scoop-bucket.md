---
layout: page
title: windows/scoop-bucket (Deutsch)
description: "Verwalte \"Eimer\": Git-Repositories, welche Dateien enthalten, die beschreiben, wie Scoop Programme installiert werden."
content_hash: fc64dd8356bf6677cc93ddaf93b73d8fd00deeaa
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/windows/scoop-bucket.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/scoop-bucket.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/scoop-bucket.html
    icon: bi bi-globe
tldri18n_status: 2
---
# scoop bucket

Verwalte "Eimer": Git-Repositories, welche Dateien enthalten, die beschreiben, wie Scoop Programme installiert werden.
Kennt Scoop nicht die URL eines Eimers, so muss diese angegeben werden.
Weitere Informationen: <https://github.com/lukesampson/scoop/wiki/Buckets>.

- Liste alle Eimer auf, die gerade aktiv sind:

`scoop bucket list`

- Liste alle bekannten Eimer auf:

`scoop bucket known`

- Aktiviere einen bekannten Eimer:

`scoop bucket add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Aktiviere einen unbekannten Eimer durch die Angabe eines Namens und einer Git-Repository-URL:

`scoop bucket add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://beispiel.de/repository.git</span>

- Deaktiviere einen Eimer:

`scoop bucket rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>
