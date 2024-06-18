---
layout: page
title: windows/ftp (Nederlands)
description: "Interactief bestanden overzetten tussen een lokale en een externe FTP-server."
content_hash: 00926057e05bba1c9442160ac8bdec9601e3c5fe
last_modified_at: 2024-06-18
related_topics:
  - title: Deutsch version
    url: /de/windows/ftp.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/ftp.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/ftp.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/ftp.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/ftp.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ftp

Interactief bestanden overzetten tussen een lokale en een externe FTP-server.
Meer informatie: <https://learn.microsoft.com/windows-server/administration/windows-commands/ftp>.

- Verbind interactief met een externe FTP-server:

`ftp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Log in als een anonieme gebruiker:

`ftp -A `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Schakel automatisch inloggen uit bij de eerste verbinding:

`ftp -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Voer een bestand uit met een lijst van FTP-opdrachten:

`ftp -s:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\bestand</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Download meerdere bestanden (glob-expressie):

`mget `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.png</span>

- Upload meerdere bestanden (glob-expressie):

`mput `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.zip</span>

- Verwijder meerdere bestanden op de externe server:

`mdelete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.txt</span>

- Toon hulp:

`ftp --help`
