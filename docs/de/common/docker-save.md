---
layout: page
title: common/docker-save (Deutsch)
description: "Exportiere eines oder mehrere Docker Images in ein Archiv."
content_hash: 2f6f29b5b1d801d3d2cfe6f823e5b5e63b932dd1
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/docker-save.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-save.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-save.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-save.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker save

Exportiere eines oder mehrere Docker Images in ein Archiv.
Weitere Informationen: <https://docs.docker.com/engine/reference/commandline/save/>.

- Speichere ein Image über die Standardausgabe in ein Tar-Archiv:

`docker save `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zur/datei.tar</span>

- Speichere ein Image in ein Tar-Archiv:

`docker save --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zur/datei.tar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag</span>

- Speichere alle Tags eines Images:

`docker save --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zur/datei.tar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image_name</span>

- Speichere nur bestimmte Tags eines Images:

`docker save --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zur/datei.tar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image_name:tag1 image_name:tag2 ...</span>
