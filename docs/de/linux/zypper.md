---
layout: page
title: linux/zypper (Deutsch)
description: "SUSE & openSUSE Package-Management-Werkzeug."
content_hash: af7e5899985f1cfde34147b90089070271cc258e
last_modified_at: 2023-11-12
related_topics:
  - title: català version
    url: /ca/linux/zypper.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/zypper.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/zypper.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/zypper.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/zypper.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/zypper.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/zypper.html
    icon: bi bi-globe
tldri18n_status: 2
---
# zypper

SUSE & openSUSE Package-Management-Werkzeug.
Weitere Informationen: <https://en.opensuse.org/SDB:Zypper_manual>.

- Synchronisiere die Liste von Paketen und verfügbaren Versionen:

`zypper refresh`

- Installiere ein neues Paket:

`zypper install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>

- Entferne ein Paket:

`zypper remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>

- Aktualisiere installierte Pakete zur neuesten verfügbaren Version:

`zypper update`

- Suche Paket nach einem bestimmten Schema:

`zypper search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">schema</span>

- Zeige Informationen bezüglich der konfigurierten Repositories:

`zypper repos --sort-by-priority`
