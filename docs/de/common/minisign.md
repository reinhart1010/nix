---
layout: page
title: common/minisign (Deutsch)
description: "Ein denkbar einfaches Werkzeug, um Dateien zu signieren und Signaturen zu verifizieren."
content_hash: 39c954a9f29e12755c927ea05e125f4b506c865e
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/minisign.html
    icon: bi bi-globe
tldri18n_status: 2
---
# minisign

Ein denkbar einfaches Werkzeug, um Dateien zu signieren und Signaturen zu verifizieren.
Weitere Informationen: <https://jedisct1.github.io/minisign/>.

- Generiere ein neues Schlüsselpaar im Standardpfad:

`minisign -G`

- Signiere eine Datei:

`minisign -Sm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>

- Signiere eine Datei und füge dabei einen vertrauenswürdigen (signierten) und einen nicht vertrauenswürdigen (unsignierten) Kommentar in der Signatur an:

`minisign -Sm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>` -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Nicht vertrauenswürdiger Kommentar</span>`" -t "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Vertrauenswürdiger Kommentar</span>`"`

- Verifiziere eine Datei und die vertrauenswürdigen Kommentare in ihrer Signatur gegen die angegebene Datei mit dem öffentlichen Schlüssel:

`minisign -Vm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/öffentlicher_schlüssel.pub</span>

- Verifiziere eine Datei und die vertrauenswürdigen Kommentare in ihrer Signatur gegen den angegebenen, in Base64 codierten öffentlichen Schlüssel:

`minisign -Vm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>` -P "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">öffentlicher_schlüssel_base64</span>`"`
