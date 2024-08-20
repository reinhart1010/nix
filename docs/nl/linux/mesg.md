---
layout: page
title: linux/mesg (Nederlands)
description: "Controleer of stel in of een terminal berichten van andere gebruikers kan ontvangen, meestal van het `write`-commando."
content_hash: f4f1ab7e706ed18fa2bcfb07d589c95a301e058a
last_modified_at: 2024-08-20
related_topics:
  - title: English version
    url: /en/linux/mesg.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/mesg.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mesg

Controleer of stel in of een terminal berichten van andere gebruikers kan ontvangen, meestal van het `write`-commando.
Zie ook `write`, `talk`.
Meer informatie: <https://manned.org/mesg.1>.

- Controleer of de terminal openstaat voor berichten:

`mesg`

- Sta geen berichten toe van andere gebruikers:

`mesg n`

- Sta berichten toe van andere gebruikers:

`mesg y`

- Schakel [v]erbose modus in, en toon een waarschuwing als het commando niet wordt uitgevoerd vanaf een terminal:

`mesg --verbose`
