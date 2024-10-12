---
layout: page
title: common/gh-secret-set (한국어)
description: "GitHub 시크릿 생성 또는 업데이트."
content_hash: addc4950881bbff04909cd521e8bf08494d5ff29
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/common/gh-secret-set.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gh secret set

GitHub 시크릿 생성 또는 업데이트.
더 많은 정보: <https://cli.github.com/manual/gh_secret_set>.

- 현재 저장소에 시크릿 설정 (사용자에게 값 입력을 요청함):

`gh secret set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- 파일에서 값을 읽어와 현재 저장소에 시크릿 설정:

`gh secret set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 특정 저장소에 시크릿 설정:

`gh secret set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` --body `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>` --repo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소유자</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">저장소</span>

- 특정 저장소들에 대해 조직 시크릿 설정:

`gh secret set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` --org `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">조직</span>` --repos "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">저장소1,저장소2,...</span>`"`

- 특정 가시성으로 조직 시크릿 설정:

`gh secret set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` --org `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">조직</span>` --visibility `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">all|private|selected</span>
