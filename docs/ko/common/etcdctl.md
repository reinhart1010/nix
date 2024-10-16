---
layout: page
title: common/etcdctl (한국어)
description: "고가용성 키-값 쌍 저장소인 `etcd`와 상호작용."
content_hash: 5c52329f5e51f3f8c825bb7344da2fd1ba420e88
last_modified_at: 2024-10-16
related_topics:
  - title: English version
    url: /en/common/etcdctl.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/etcdctl.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># etcdctl

고가용성 키-값 쌍 저장소인 `etcd`와 상호작용.
더 많은 정보: <https://etcd.io/docs/latest/dev-guide/interacting_v3/>.

- 지정된 키와 연관된 값을 표시:

`etcdctl get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">자신의_키</span>

- 키-값-쌍을 저장:

`etcdctl put `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">자신의_키</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">자신의_값</span>

- 키-값 쌍 삭제:

`etcdctl del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">자신의_키</span>

- 파일에서 값을 읽어 키-값 쌍을 저장:

`etcdctl put `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">자신의_파일</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.txt</span>

- etcd 키 저장소의 스냅샷을 저장:

`etcdctl snapshot save `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스냅샷.db</span>

- etcd 키 저장소의 스냅샷을 복원 (나중에 etcd 서버를 다시 시작):

`etcdctl snapshot restore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스냅샷.db</span>

- 사용자 추가:

`etcdctl user add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">자신의_유저</span>

- 주요 변경사항 살펴보기:

`etcdctl watch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">자신의_키</span>
