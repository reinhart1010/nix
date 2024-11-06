---
layout: page
title: common/hut (한국어)
description: "sourcehut용 CLI 도구."
content_hash: fb81cc6f54a0ed69d599ce611a8f36d75e142b45
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/hut.html
    icon: bi bi-globe
tldri18n_status: 2
---
# hut

sourcehut용 CLI 도구.
더 많은 정보: <https://manned.org/hut>.

- `hut`의 구성 파일을 초기화 (`hut`를 사용하는 데 필요한 OAuth2 액세스 토큰을 묻는 메시지가 표시됨):

`hut init`

- Git/Mercurial 저장소 나열:

`hut `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">git|hg</span>` list`

- 공개 Git/Mercurial 저장소를 생성:

`hut `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">git|hg</span>` create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- <https://builds.sr.ht>의 작업 목록 나열:

`hut builds list`

- 작업 상태 표시:

`hut builds show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_아이디</span>

- 작업 컨테이너에 SSH로 연결:

`hut ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_아이디</span>
