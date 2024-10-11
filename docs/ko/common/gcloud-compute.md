---
layout: page
title: common/gcloud-compute (한국어)
description: "Google Cloud 인프라에서 VM을 생성, 실행 및 관리."
content_hash: 8977cea4538b8eb7462a4d18e7cb1af7b8d4be6b
last_modified_at: 2024-10-11
related_topics:
  - title: English version
    url: /en/common/gcloud-compute.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gcloud-compute.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gcloud compute

Google Cloud 인프라에서 VM을 생성, 실행 및 관리.
같이 보기: `gcloud`.
더 많은 정보: <https://cloud.google.com/sdk/gcloud/reference/compute>.

- Compute Engine 영역 나열:

`gcloud compute zones list`

- VM 인스턴스 생성:

`gcloud compute instances create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인스턴스_이름</span>

- VM 인스턴스 세부 정보 표시:

`gcloud compute instances describe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인스턴스_이름</span>

- 프로젝트 내 모든 VM 인스턴스 나열:

`gcloud compute instances list`

- 영구 디스크 스냅샷 생성:

`gcloud compute disks snapshot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">디스크_이름</span>` --snapshot-names `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스냅샷_이름</span>

- 스냅샷 세부 정보 표시:

`gcloud compute snapshots describe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스냅샷_이름</span>

- 스냅샷 삭제:

`gcloud compute snapshots delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스냅샷_이름</span>

- SSH를 사용하여 VM 인스턴스에 연결:

`gcloud compute ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인스턴스_이름</span>
