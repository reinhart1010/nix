---
layout: page
title: common/numfmt (English)
description: "Convert numbers to and from human-readable strings."
content_hash: b0506e33e5f133b849f0323643ae0f2813b6137d
last_modified_at: 2024-06-26
tldri18n_status: 2
---
# numfmt

Convert numbers to and from human-readable strings.
More information: <https://www.gnu.org/software/coreutils/numfmt>.

- Convert 1.5K (SI Units) to 1500:

`numfmt --from=si 1.5K`

- Convert 5th field (1-indexed) to IEC Units without converting header:

`ls -l | numfmt --header=1 --field=5 --to=iec`

- Convert to IEC units, pad with 5 characters, left aligned:

`du -s * | numfmt --to=iec --format="%-5f"`
