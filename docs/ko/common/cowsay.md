---
layout: page
title: common/cowsay (한국어)
description: "무언가를 말하거나 생각하는 ASCII 문자(기본적으로 cow)를 생성."
content_hash: c428828f16c3b2c172d67644c926deb91c908918
related_topics:
  - title: English version
    url: /en/common/cowsay.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/cowsay.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cowsay.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cowsay

무언가를 말하거나 생각하는 ASCII 문자(기본적으로 cow)를 생성.
더 많은 정보: <https://github.com/tnalpgge/rank-amateur-cowsay>.

- "Hello world"라고 말하는 ASCII cow 출력:

`cowsay "Hello world"`

- 풍선에 표준 입력의 텍스트 사용:

`echo "Hello" | cowsay`

- 사용 가능한 모든 문자 나열:

`cowsay -l`

- "Hello"라고 말하는 ASCII dragon 출력:

`cowsay -f dragon "Hello"`

- 돌로 된 생각하는 ASCII cow 출력:

`cowthink -s "I'm just a cow, not a great thinker..."`
