---
layout: page
title: common/protector (한국어)
description: "GitHub 저장소의 브랜치를 보호하거나 보호 해제."
content_hash: d2900a94db8805c6ff8b30758fc3ac0b550250b8
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/protector.html
    icon: bi bi-globe
tldri18n_status: 2
---
# protector

GitHub 저장소의 브랜치를 보호하거나 보호 해제.
더 많은 정보: <https://github.com/jcgay/protector>.

- GitHub 저장소의 브랜치 보호 (브랜치 보호 규칙 생성):

`protector `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">브랜치_정규식</span>` -repos `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">조직/저장소</span>

- 보호될 브랜치 미리보기 (해제에도 사용 가능):

`protector -dry-run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">브랜치_정규식</span>` -repos `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">조직/저장소</span>

- GitHub 저장소의 브랜치 보호 해제 (브랜치 보호 규칙 삭제):

`protector -free `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">브랜치_정규식</span>` -repos `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">조직/저장소</span>
