---
layout: page
title: common/sudo (polski)
description: "Wykonuje pojedyncze polecenie jako superuser lub inny użytkownik."
content_hash: 84227531f5ce5f86007156d6dca33894a8cb044f
last_modified_at: 2024-03-10
related_topics:
  - title: English version
    url: /en/common/sudo.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/sudo.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/sudo.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/sudo.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># sudo

Wykonuje pojedyncze polecenie jako superuser lub inny użytkownik.
Więcej informacji: <https://www.sudo.ws/sudo.html>.

- Uruchom polecenie jako superuser:

`sudo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">less /var/log/syslog</span>

- Edytuj plik jako superuser w domyślnym edytorze:

`sudo -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/etc/fstab</span>

- Uruchom polecenie jako inny użytkownik i/lub grupa:

`sudo -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uzytkownik</span>` -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grupa</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id -a</span>

- Powtórz ostatnie polecenie poprzedzone `sudo` (tylko w Bash, Zsh, etc.):

`sudo !!`

- Uruchom domyślną powłokę z uprawnieniami superuser:

`sudo -i`
