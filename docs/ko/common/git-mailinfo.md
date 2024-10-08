---
layout: page
title: common/git-mailinfo (한국어)
description: "이메일 메시지에서 패치 및 작성자 정보를 추출."
content_hash: a1d1207b76cf254a1abf601d54b33524abdb206e
last_modified_at: 2024-10-08
related_topics:
  - title: English version
    url: /en/common/git-mailinfo.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git mailinfo

이메일 메시지에서 패치 및 작성자 정보를 추출.
더 많은 정보: <https://git-scm.com/docs/git-mailinfo>.

- 이메일 메시지에서 패치 및 작성자 데이터 추출:

`git mailinfo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">message|patch</span>

- 추출하지만 앞뒤 공백 제거:

`git mailinfo -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">message|patch</span>

- 본문에서 가위선 (예: "-->* --") 이전의 모든 내용을 제거하고 메시지 또는 패치 추출:

`git mailinfo --scissors `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">message|patch</span>
