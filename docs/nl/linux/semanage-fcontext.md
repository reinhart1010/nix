---
layout: page
title: linux/semanage-fcontext (Nederlands)
description: "Beheer persistente SELinux-beveiligingscontextregels op bestanden/mappen."
content_hash: cc00366b001105544e89e0509ea6814feb7fcac8
last_modified_at: 2025-01-03
related_topics:
  - title: English version
    url: /en/linux/semanage-fcontext.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/semanage-fcontext.html
    icon: bi bi-globe
tldri18n_status: 2
---
# semanage fcontext

Beheer persistente SELinux-beveiligingscontextregels op bestanden/mappen.
Bekijk ook: `semanage`, `matchpathcon`, `secon`, `chcon`, `restorecon`.
Meer informatie: <https://manned.org/semanage-fcontext>.

- Toon alle bestandslabelregels:

`sudo semanage fcontext --list`

- Toon alle door de gebruiker gedefinieerde bestandslabelregels zonder koppen:

`sudo semanage fcontext --list --locallist --noheading`

- Voeg een door de gebruiker gedefinieerde regel toe die elk pad labelt dat overeenkomt met een PCRE-regex:

`sudo semanage fcontext --add --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">samba_share_t</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'/mnt/share(/.*)?'</span>

- Verwijder een door de gebruiker gedefinieerde regel met behulp van zijn PCRE-regex:

`sudo semanage fcontext --delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'/mnt/share(/.*)?'</span>

- Herlabel een map recursief door de nieuwe regels toe te passen:

`restorecon -R -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/map</span>
