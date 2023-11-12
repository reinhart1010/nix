---
layout: page
title: common/numfmt (English)
description: "Convert numbers to and from human-readable strings."
content_hash: 0fa87c05a0ed2ba708a6fb7895c579cd30b7e35f
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# numfmt

Convert numbers to and from human-readable strings.
More information: <https://www.gnu.org/software/coreutils/numfmt>.

- Convert 1.5K (SI Units) to 1500:

`numfmt --from=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">si</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.5K</span>

- Convert 5th field (1-indexed) to IEC Units without converting header:

`ls -l | numfmt --header=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` --field=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` --to=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">iec</span>

- Convert to IEC units, pad with 5 characters, left aligned:

`du -s * | numfmt --to=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">iec</span>` --format="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">%-5f</span>`"`
