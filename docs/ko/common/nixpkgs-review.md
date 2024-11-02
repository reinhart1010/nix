---
layout: page
title: common/nixpkgs-review (한국어)
description: "NixOS 패키지 저장소(nixpkgs)에서 풀 리퀘스트를 검토."
content_hash: e16c596f077501c8a47d250cf3c45d3962442f37
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/nixpkgs-review.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nixpkgs-review

NixOS 패키지 저장소(nixpkgs)에서 풀 리퀘스트를 검토.
빌드가 성공하면, 모든 빌드된 패키지를 포함한 `nix-shell`이 시작됩니다.
더 많은 정보: <https://github.com/Mic92/nixpkgs-review#usage>.

- 지정된 풀 리퀘스트에서 변경된 패키지 빌드:

`nixpkgs-review pr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pr_번호|pr_url</span>

- 변경된 패키지를 빌드하고 보고서와 함께 댓글 게시 (`hub`, `gh` 또는 `GITHUB_TOKEN` 환경 변수를 설정해야 함):

`nixpkgs-review pr --post-result `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pr_번호|pr_url</span>

- 변경된 패키지를 빌드하고 보고서 출력:

`nixpkgs-review pr --print-result `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pr_번호|pr_url</span>

- 로컬 커밋에서 변경된 패키지 빌드:

`nixpkgs-review rev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD</span>

- 아직 커밋되지 않은 변경된 패키지 빌드:

`nixpkgs-review wip`

- 스테이징된 변경된 패키지 빌드:

`nixpkgs-review wip --staged`
