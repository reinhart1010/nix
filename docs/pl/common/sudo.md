---
layout: page
title: common/sudo (polski)
description: "Wykonuje pojedyncze polecenie jako superuser lub inny użytkownik."
content_hash: 2e2606ac42a19a4fe11beecd6482fcd1c06cf689
related_topics:
  - title: English version
    url: /en/common/sudo.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/sudo.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/sudo.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sudo

Wykonuje pojedyncze polecenie jako superuser lub inny użytkownik.
Więcej informacji: <https://www.sudo.ws/sudo.html>.

- Uruchom polecenie jako superuser:

`sudo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">less /var/log/syslog</span>

- Edytuj plik jako superuser w domyślnym edytorze:

`sudo -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/etc/fstab</span>

- Uruchom polecenie jako inny użytkownik i/lub grupa:

`sudo -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uzytkownik</span>` -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grupa</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id -a</span>

- Powtórz ostatnie polecenie poprzedzone `sudo` (tylko w `bash`, `zsh`, etc.):

`sudo !!`

- Uruchom domyślną powłokę z uprawnieniami superuser:

`sudo -i`
