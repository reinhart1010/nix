---
layout: page
title: common/ntfy (한국어)
description: "HTTP POST 알림을 보내고 받기."
content_hash: 1c2bc43842a93bff070d97cf5c7377569cdfdd56
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/ntfy.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ntfy.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ntfy

HTTP POST 알림을 보내고 받기.
더 많은 정보: <https://github.com/binwiederhier/ntfy>.

- `security` 토픽에 메시지 보내기:

`ntfy pub security "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">현관문이 열렸습니다.</span>`"`

- 제목, 우선순위 및 태그와 함께 보내기:

`ntfy publish --title="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">누군가 당신의 아이템을 구매했습니다</span>`" --priority=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">높음</span>` --tags=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">오리</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이베이</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">누군가 당신의 아이템을 구매했습니다: 오리너구리 조각상</span>`"`

- 오전 8시 30분에 보내기:

`ntfy pub --at=8:30am `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">지연된_토픽</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">학교 갈 시간이야, 졸린이...</span>`"`

- 웹훅 트리거:

`ntfy trigger `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">나의_웹훅</span>

- 토픽 구독하기 (Ctrl-C로 듣기 중지):

`ntfy sub `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">홈_자동화</span>

- 도움말 표시:

`ntfy --help`
