---
layout: page
title: common/mmv (한국어)
description: "파일을 대량으로 이동 및 이름 변경."
content_hash: 608a8c1ff1a1fb2bc964f1109bd81c86c8523f30
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/mmv.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/mmv.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mmv

파일을 대량으로 이동 및 이름 변경.
더 많은 정보: <https://manned.org/mmv.1>.

- 특정 확장자를 가진 모든 파일의 확장자 변경:

`mmv "*`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.old_extension</span>`" "#1`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.new_extension</span>`"`

- `report6part4.txt`를 `./french/rapport6partie4.txt`로 복사하고, 유사한 이름을 가진 모든 파일도 함께 복사:

`mmv -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">report*part*.txt</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">./french/rapport#1partie#2.txt</span>`"`

- 모든 `.txt` 파일을 하나의 파일로 합치기:

`mmv -a "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.txt</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">모두.txt</span>`"`

- 파일 이름의 날짜 형식을 "M-D-Y"에서 "D-M-Y"로 변환:

`mmv "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">[0-1][0-9]-[0-3][0-9]-[0-9][0-9][0-9][0-9].txt</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">#3#4-#1#2-#5#6#7#8.txt</span>`"`
