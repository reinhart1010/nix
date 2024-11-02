---
layout: page
title: common/pbmtolj (한국어)
description: "PBM 파일을 HP LaserJet 파일로 변환."
content_hash: 5a6d64aeaf032e7f3a433837cbfd7f191984dfc6
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/pbmtolj.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pbmtolj.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pbmtolj

PBM 파일을 HP LaserJet 파일로 변환.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pbmtolj.html>.

- PBM 파일을 HP LaserJet 파일로 변환:

`pbmtolj `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/output.lj</span>

- 지정된 방법으로 출력 파일 압축:

`pbmtolj -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">packbits|delta|compress</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/output.lj</span>

- 필요한 해상도 지정:

`pbmtolj -resolution `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">75|100|150|300|600</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/output.lj</span>
