---
layout: page
title: common/numfmt (Nederlands)
description: "Converteer getallen naar en van mens-leesbare strings."
content_hash: 47f5739d9fad5ff9775a8f6aea27762a54330e41
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/numfmt.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/numfmt.html
    icon: bi bi-globe
tldri18n_status: 2
---
# numfmt

Converteer getallen naar en van mens-leesbare strings.
Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/numfmt-invocation.html>.

- Converteer 1.5K (SI-eenheden) naar 1500:

`numfmt --from=si 1.5K`

- Converteer het 5e veld (1-gebaseerd) naar IEC-eenheden zonder de header te converteren:

`ls -l | numfmt --header=1 --field=5 --to=iec`

- Converteer naar IEC-eenheden, opvullen met 5 tekens, links uitgelijnd:

`du -s * | numfmt --to=iec --format="%-5f"`
