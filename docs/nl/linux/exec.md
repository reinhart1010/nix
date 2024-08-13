---
layout: page
title: linux/exec (Nederlands)
description: "Voer een commando uit zonder een child-proces te creëren."
content_hash: 079fd4ad945bad12ce674ac0f2fc912884847791
last_modified_at: 2024-08-13
related_topics:
  - title: English version
    url: /en/linux/exec.html
    icon: bi bi-globe
tldri18n_status: 2
---
# exec

Voer een commando uit zonder een child-proces te creëren.
Meer informatie: <https://www.gnu.org/software/bash/manual/bash.html#index-exec>.

- Voer een specifiek commando uit:

`exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando -with -flags</span>

- Voer een commando uit met een (grotendeels) lege omgeving:

`exec -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando -with -flags</span>

- Voer een commando uit als een login-shell:

`exec -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando -with -flags</span>

- Voer een commando uit met een andere naam:

`exec -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">naam</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando -with -flags</span>
