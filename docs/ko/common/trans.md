---
layout: page
title: common/trans (한국어)
description: "Translate Shell은 명령줄 번역기입니다."
content_hash: ce24f4c0793c793bf1d0d5fea3c5cef7d54c781a
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/trans.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/trans.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># trans

Translate Shell은 명령줄 번역기입니다.
더 많은 정보: <https://github.com/soimort/translate-shell>.

- 단어 번역 (언어는 자동으로 감지됨):

`trans "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">번역할_단어나_문장</span>`"`

- 간단한 번역 받기:

`trans --brief "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">번역할_단어나_문장</span>`"`

- 단어를 프랑스어로 번역:

`trans :`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fr</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">단어</span>

- 독일어에서 영어로 단어 번역:

`trans `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">de</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">en</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Schmetterling</span>

- 사전처럼 행동하여 단어의 의미 얻기:

`trans -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">단어</span>
