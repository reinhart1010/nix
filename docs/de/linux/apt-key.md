---
layout: page
title: linux/apt-key (Deutsch)
description: "Schlüssel-Management-Tool für den APT-Paket-Manager auf Debian und Ubuntu."
content_hash: fb78deb3b24142bab5169470b596624380e994b0
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
  - title: português (Brasil) version
    url: /pt_BR/linux/apt-key.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt-key.html
    icon: bi bi-globe
---
# apt-key

Schlüssel-Management-Tool für den APT-Paket-Manager auf Debian und Ubuntu.
Notiz: `apt-key` ist deprecated (außer für `apt-key del` in Maintainer Scripts).
Weitere Informationen: <https://manpages.debian.org/latest/apt/apt-key.8.html>.

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
