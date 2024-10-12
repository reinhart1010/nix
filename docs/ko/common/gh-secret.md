---
layout: page
title: common/gh-secret (한국어)
description: "GitHub 시크릿 관리."
content_hash: 9a6acd9738d0a4be700886b916dbfedca54318be
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/common/gh-secret.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gh secret

GitHub 시크릿 관리.
더 많은 정보: <https://cli.github.com/manual/gh_secret>.

- 현재 저장소의 시크릿 키 나열:

`gh secret list`

- 특정 조직의 시크릿 키 나열:

`gh secret list --org `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">조직</span>

- 특정 저장소의 시크릿 키 나열:

`gh secret list --repo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소유자</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">저장소</span>

- 현재 저장소에 시크릿 설정 (사용자가 값을 입력해야 함):

`gh secret set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- 파일에서 값을 가져와 현재 저장소에 시크릿 설정:

`gh secret set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 특정 저장소에 대한 조직 시크릿 설정:

`gh secret set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` --org `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">조직</span>` --repos `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">저장소1,저장소2</span>

- 현재 저장소의 시크릿 제거:

`gh secret remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- 특정 조직의 시크릿 제거:

`gh secret remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` --org `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">조직</span>
