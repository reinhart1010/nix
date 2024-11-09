---
layout: page
title: linux/po4a-translate (한국어)
description: "PO 파일을 문서 형식으로 다시 변환."
content_hash: 3cb4266436ff455e74f78753a06c8fbfd0ba917b
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/po4a-translate.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/po4a-translate.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># po4a-translate

PO 파일을 문서 형식으로 다시 변환.
제공된 PO 파일은 `po4a-gettextize`로 생성된 POT 파일의 번역본이어야 합니다.
더 많은 정보: <https://po4a.org/man/man1/po4a-translate.1.php>.

- 번역된 PO 파일을 문서로 다시 변환:

`po4a-translate --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">텍스트</span>` --master `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/원본.doc</span>` --po `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/결과.po</span>` --localized `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/번역된.txt</span>

- 사용 가능한 모든 형식 나열:

`po4a-translate --help-format`
