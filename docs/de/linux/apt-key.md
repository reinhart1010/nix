---
layout: page
title: linux/apt-key (Deutsch)
description: "Schlüssel-Management-Tool für den APT-Paket-Manager auf Debian und Ubuntu."
content_hash: 286125f2c6aa6d6327a857f841aac4959b15a2ec
last_modified_at: 2024-09-18
related_topics:
  - title: català version
    url: /ca/linux/apt-key.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/apt-key.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/apt-key.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/apt-key.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/apt-key.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apt-key.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/apt-key.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt-key.html
    icon: bi bi-globe
tldri18n_status: 2
---
# apt-key

Schlüssel-Management-Tool für den APT-Paket-Manager auf Debian und Ubuntu.
Notiz: `apt-key` ist veraltet (außer für `apt-key del` in Maintainerskripten).
Weitere Informationen: <https://manned.org/apt-key.8>.

- Liste alle vertrauten Schlüssel auf:

`apt-key list`

- Füge einen Schlüssel hinzu:

`apt-key add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">public_key_file.asc</span>

- Lösche einen Schlüssel:

`apt-key del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_id</span>

- Füge einen Remote-Schlüssel hinzu:

`wget -qO - `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://host.tld/filename.key</span>` | apt-key add -`

- Füge einen Schlüssel von einem Schlüsselserver hinzu nur mit der Schlüssel-ID:

`apt-key adv --keyserver `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pgp.mit.edu</span>` --recv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">KEYID</span>
