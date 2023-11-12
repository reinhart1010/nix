---
layout: page
title: common/rm (Deutsch)
description: "Lösche Dateien oder Verzeichnisse."
content_hash: 16796f8aeb3f129de5233bfdd95a40373a0a8902
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/rm.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/rm.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/rm.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/rm.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/rm.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/rm.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/rm.html
    icon: bi bi-globe
  - title: svenska version
    url: /sv/common/rm.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/rm.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/rm.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/rm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rm

Lösche Dateien oder Verzeichnisse.
Weitere Informationen: <https://www.gnu.org/software/coreutils/rm>.

- Lösche Dateien an beliebigen Speicherorten:

`rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/anderer/datei</span>

- Lösche ein Verzeichnis und alle seine Unterverzeichnisse rekursiv:

`rm -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/verzeichnis</span>

- Erzwinge das Löschen eines Verzeichnisses, ohne Eingabeaufforderung zur Bestätigung oder Anzeigen von Fehlermeldungen:

`rm -rf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/verzeichnis</span>

- Lösche mehrere Dateien mit Eingabeaufforderung zur Bestätigung für jede Datei:

`rm -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei1 pfad/zu/datei2 ...</span>

- Liste jede Datei auf, wenn sie gelöscht wird:

`rm -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/verzeichnis/*</span>
