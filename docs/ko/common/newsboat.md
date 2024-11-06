---
layout: page
title: common/newsboat (한국어)
description: "텍스트 터미널용 RSS/Atom 피드 리더."
content_hash: 72b8f65d2649770b6279ac0e16a45b9a612337e3
last_modified_at: 2024-11-06
related_topics:
  - title: العربية version
    url: /ar/common/newsboat.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/newsboat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# newsboat

텍스트 터미널용 RSS/Atom 피드 리더.
더 많은 정보: <https://newsboat.org/>.

- OPML 파일에서 피드 URL을 처음으로 가져오기:

`newsboat -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">내-피드.xml</span>

- 또는 피드를 수동으로 추가:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com/path/to/feed</span>` >> "${HOME}/.newsboat/urls"`

- Newsboat을 시작하고 시작 시 모든 피드를 새로 고침:

`newsboat -r`

- 비대화형 모드에서 하나 이상의 명령 실행:

`newsboat -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">reload print-unread ...</span>

- 키보드 단축키 보기 (가장 관련 있는 것은 상태 줄에 표시됨):

`?`
