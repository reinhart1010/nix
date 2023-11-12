---
layout: page
title: common/cp (Deutsch)
description: "Kopiere Dateien und Verzeichnisse."
content_hash: afe1fd41c36be1d54afde7d99433f21aa1073210
last_modified_at: 2023-11-12
related_topics:
  - title: català version
    url: /ca/common/cp.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/cp.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/cp.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/cp.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/cp.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/cp.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/cp.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/cp.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/cp.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cp.html
    icon: bi bi-globe
  - title: नेपाली version
    url: /ne/common/cp.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/cp.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/cp.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/cp.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/cp.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/cp.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/cp.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># cp

Kopiere Dateien und Verzeichnisse.
Weitere Informationen: <https://www.gnu.org/software/coreutils/cp>.

- Kopiere eine Datei an einen anderen Ort:

`cp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/kopie</span>

- Kopiere eine Datei an einen anderen Ort und behalte den Dateinamen:

`cp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/zielverzeichnis</span>

- Kopiere ein Verzeichnis rekursiv (falls der Zielort bereits existiert, wird das Verzeichnis in das Zielverzeichnis kopiert):

`cp -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/verzeichnis</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/zielverzeichnis</span>

- Kopiere ein Verzeichnis rekursiv und gib alle Dateien aus, während sie kopiert werden:

`cp -vr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/verzeichnis</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/zielverzeichnis</span>

- Kopiere alle Textdateien in einem Verzeichnis und warte auf eine Bestätigung, falls eine Datei überschrieben werden soll:

`cp -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/pfad/zu/*.txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/zielverzeichnis</span>

- Folge symbolischen Links vor dem Kopieren:

`cp -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">link</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/zielverzeichnis</span>
