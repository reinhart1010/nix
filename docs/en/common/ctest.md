---
layout: page
title: common/ctest (English)
description: "CMake test driver program."
content_hash: 2003c4d8e194a34c730459a75a2f27023e9c5285
last_modified_at: 2024-01-31
related_topics:
  - title: italiano version
    url: /it/common/ctest.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ctest.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ctest

CMake test driver program.
More information: <https://gitlab.kitware.com/cmake/community/wikis/doc/ctest/Testing-With-CTest>.

- Run all tests defined in the CMake project, executing 4 jobs at a time in parallel:

`ctest -j`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` --output-on-failure`

- List available tests:

`ctest -N`

- Run a single test based on its name, or filter on a regular expression:

`ctest --output-on-failure -R '^`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">test_name</span>`$'`
