---
layout: page
title: linux/aa-disable (Nederlands)
description: "Schakel AppArmor-beveiligingsprofielen uit."
content_hash: f03572d427f4bf11ab1add9bcc28688f91e68aad
last_modified_at: 2024-10-17
related_topics:
  - title: English version
    url: /en/linux/aa-disable.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/aa-disable.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aa-disable

Schakel AppArmor-beveiligingsprofielen uit.
Bekijk ook: `aa-complain`, `aa-enforce`, `aa-status`.
Meer informatie: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-disable.8>.

- Schakel een profiel uit:

`sudo aa-disable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/profiel1 pad/naar/profiel2 ...</span>

- Schakel profielen uit (standaard naar `/etc/apparmor.d`):

`sudo aa-disable --dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/profielen</span>
