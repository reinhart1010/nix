---
layout: page
title: common/chmod (Deutsch)
description: "Ändere die Zugriffsberechtigungen einer Datei oder eines Verzeichnisses."
content_hash: 080239e8e409f9728f07a78b1dbea322a0ddf2fc
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/chmod.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/chmod.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/chmod.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/chmod.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/chmod.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/chmod.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/chmod.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/common/chmod.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/chmod.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/chmod.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/chmod.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/chmod.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/chmod.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/chmod.html
    icon: bi bi-globe
tldri18n_status: 2
---
# chmod

Ändere die Zugriffsberechtigungen einer Datei oder eines Verzeichnisses.
Weitere Informationen: <https://www.gnu.org/software/coreutils/chmod>.

- Gib dem Besitzer einer Datei ([u]ser) das Recht, sie auszuführen (e[x]ecute):

`chmod u+x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>

- Gib dem Besitzer ([u]ser) Rechte zum Lesen ([r]ead) und Schreiben ([w]rite) einer Datei / einem Verzeichnis:

`chmod u+rw `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei_oder_verzeichnis</span>

- Entferne die Ausführrechte (e[x]ecute) der Besitzer[g]ruppe:

`chmod g-x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>

- Gib [a]llen Benutzern Rechte zum Lesen ([r]ead) und Ausführen (e[x]ecute) einer Datei:

`chmod a+rx `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>

- Gib anderen ([o]thers) (nicht in der Besitzer[g]ruppe) die gleichen Rechte wie der Besitzer[g]ruppe:

`chmod o=g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>

- Entferne alle Rechte der anderen ([o]thers):

`chmod o= `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>

- Ändere Rechte rekursiv, indem der Besitzer[g]ruppe und anderen ([o]thers) die Rechte zum Schreiben ([w]rite) geben werden:

`chmod -R g+w,o+w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/verzeichnis</span>

- Gib [a]llen Benutzern rekursiv Rechte zum Lesen ([r]ead) von Dateien und Ausführen (e[X]ecute) von Unterverzeichnissen innerhalb eines Verzeichnisses:

`chmod -R a+rX `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/verzeichnis</span>
