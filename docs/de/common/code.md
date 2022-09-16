---
layout: page
title: common/code (Deutsch)
description: "Visual Studio Code."
content_hash: d8d7c36d786208a12b81bb1fc2b8b3f99880ad78
related_topics:
  - title: English version
    url: /en/common/code.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/code.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/code.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/code.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/code.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/code.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/code.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/code.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># code

Visual Studio Code.
Weitere Informationen: <https://github.com/microsoft/vscode>.

- Öffne Visual Studio Code:

`code`

- Öffne bestimmte Dateien und/oder Verzeichnisse:

`code `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei_oder_verzeichnis1 pfad/zu/datei_oder_verzeichnis2 ...</span>

- Vergleiche zwei bestimmte Dateien:

`code --diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei2</span>

- Öffne bestimmte Dateien und/oder Verzeichnisse in einem neuen Fenster:

`code --new-window `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei_oder_verzeichnis1 pfad/zu/datei_oder_verzeichnis2 ...</span>

- Installiere oder lösche bestimmte Erweiterung:

`code --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">install|uninstall</span>`-extension `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">herausgeber.erweiterung</span>

- Liste alle installierten Erweiterungen auf:

`code --list-extensions`

- Liste alle installierten Erweiterungen und deren Version auf:

`code --list-extensions --show-versions`

- Starte Visual Studio Code als Superuser und speichere Benutzerdaten in einem bestimmten Verzeichnis:

`sudo code --user-data-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/verzeichnis</span>
