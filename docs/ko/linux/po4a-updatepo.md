---
layout: page
title: linux/po4a-updatepo (한국어)
description: "문서의 번역(PO 형식)을 업데이트합니다."
content_hash: d6b807ddfa02a3d7be25c794d6656f478e5b6028
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/po4a-updatepo.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/po4a-updatepo.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># po4a-updatepo

문서의 번역(PO 형식)을 업데이트합니다.
더 많은 정보: <https://po4a.org/man/man1/po4a-updatepo.1.php>.

- 원본 파일의 수정 사항에 따라 PO 파일 업데이트:

`po4a-updatepo --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">text</span>` --master `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/원본.txt</span>` --po `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/결과물.po</span>

- 사용 가능한 형식 나열:

`po4a-updatepo --help-format`

- 원본 파일의 수정 사항에 따라 여러 PO 파일 업데이트:

`po4a-updatepo --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">text</span>` --master `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/원본.txt</span>` --po `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/po1.po</span>` --po `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/po2.po</span>
