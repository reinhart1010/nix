---
layout: page
title: common/numfmt (English)
description: "Convert numbers to and from human-readable strings."
content_hash: 69f06b018c760ea1a40bb3e77bc82848322ba4a6
last_modified_at: 2025-03-02
related_topics:
  - title: 한국어 version
    url: /ko/common/numfmt.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/numfmt.html
    icon: bi bi-globe
tldri18n_status: 2
---
# numfmt

Convert numbers to and from human-readable strings.
More information: <https://www.gnu.org/software/coreutils/manual/html_node/numfmt-invocation.html>.

- Convert 1.5K (SI Units) to 1500:

`numfmt --from=si 1.5K`

- Convert 5th field (1-indexed) to IEC Units without converting header:

`ls -l | numfmt --header=1 --field=5 --to=iec`

- Convert to IEC units, pad with 5 characters, left aligned:

`du -s * | numfmt --to=iec --format="%-5f"`
