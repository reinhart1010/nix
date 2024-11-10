---
layout: page
title: linux/xcowsay (한국어)
description: "Linux 데스크탑에 귀여운 소와 메시지를 표시합니다."
content_hash: f16948fc5fb28c86edf0160b2d2d59fb83a79f88
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/xcowsay.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/xcowsay.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/xcowsay.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># xcowsay

Linux 데스크탑에 귀여운 소와 메시지를 표시합니다.
소는 고정된 시간 동안 표시되거나 텍스트 크기에 따라 계산된 시간 동안 표시됩니다. 소를 클릭하면 즉시 닫힙니다.
더 많은 정보: <https://www.doof.me.uk/xcowsay/>.

- "hello, world"라고 말하는 소를 표시:

`xcowsay "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hello, world</span>`"`

- 다른 명령의 출력을 표시하는 소를 표시:

`ls | xcowsay`

- 지정된 X, Y 좌표에 소를 표시:

`xcowsay --at=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">X</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Y</span>

- 다른 크기의 소를 표시:

`xcowsay --cow-size=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">small|med|large</span>

- 말풍선 대신 생각풍선을 표시:

`xcowsay --think`

- 기본 소 대신 다른 이미지를 표시:

`xcowsay --image=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
