---
layout: page
title: common/numfmt (Nederlands)
description: "Converteer getallen naar en van mens-leesbare strings."
content_hash: 173bf7e5aa9f76c6a7e5644cc93ded6e423735d3
last_modified_at: 2024-06-27
related_topics:
  - title: English version
    url: /en/common/numfmt.html
    icon: bi bi-globe
tldri18n_status: 2
---
# numfmt

Converteer getallen naar en van mens-leesbare strings.
Meer informatie: <https://www.gnu.org/software/coreutils/numfmt>.

- Converteer 1.5K (SI-eenheden) naar 1500:

`numfmt --from=si 1.5K`

- Converteer het 5e veld (1-gebaseerd) naar IEC-eenheden zonder de header te converteren:

`ls -l | numfmt --header=1 --field=5 --to=iec`

- Converteer naar IEC-eenheden, opvullen met 5 tekens, links uitgelijnd:

`du -s * | numfmt --to=iec --format="%-5f"`
