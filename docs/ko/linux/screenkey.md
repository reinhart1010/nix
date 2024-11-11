---
layout: page
title: linux/screenkey (한국어)
description: "키 입력을 화면에 표시하는 스크린캐스트 도구."
content_hash: 8cf317a79c726f5541861a69436a249610ddd4ad
last_modified_at: 2024-11-11
related_topics:
  - title: English version
    url: /en/linux/screenkey.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/screenkey.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># screenkey

키 입력을 화면에 표시하는 스크린캐스트 도구.
더 많은 정보: <https://www.thregr.org/~wavexx/software/screenkey/>.

- 현재 눌린 키를 화면에 표시:

`screenkey`

- 현재 눌린 키와 마우스 버튼을 화면에 표시:

`screenkey --mouse`

- screenkey의 설정 메뉴 실행:

`screenkey --show-settings`

- 특정 위치에 screenkey 실행:

`screenkey --position `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">top|center|bottom|fixed</span>

- 화면에 표시되는 키 수정자의 형식 변경:

`screenkey --mods-mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">normal|emacs|mac|win|tux</span>

- screenkey의 외관 변경:

`screenkey --bg-color "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">#a1b2c3</span>`" --font `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hack</span>` --font-color `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">yellow</span>` --opacity `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.8</span>

- 화면에서 창을 드래그하여 screenkey 표시 위치 선택:

`screenkey --position fixed --geometry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$(slop -n -f '%g')</span>
