---
layout: page
title: common/k8sec (한국어)
description: "Kubernetes 시크릿 관리 도구."
content_hash: 349d76ad6c6fa12ef21422fc31a3a84e224fcc7e
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/k8sec.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/k8sec.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># k8sec

Kubernetes 시크릿 관리 도구.
더 많은 정보: <https://github.com/dtan4/k8sec>.

- 모든 시크릿 나열:

`k8sec list`

- 특정 시크릿을 base64로 인코딩된 문자열로 나열:

`k8sec list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀_이름</span>` --base64`

- 시크릿 값 설정:

`k8sec set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key=값</span>

- base64로 인코딩된 값 설정:

`k8sec set --base64 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key=인코딩된_값</span>

- 시크릿 해제:

`k8sec unset `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀_이름</span>

- 파일에서 시크릿 불러오기:

`k8sec load -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀_이름</span>

- 파일로 시크릿 덤프:

`k8sec dump -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀_이름</span>
