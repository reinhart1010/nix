---
layout: page
title: common/sphinx-build (English)
description: "Sphinx documentation generator."
content_hash: 5ffd1e5b8ac69dc0face531b82a6434ab6d8d4d3
last_modified_at: 2024-10-12
tldri18n_status: 2
---
# sphinx-build

Sphinx documentation generator.
More information: <https://www.sphinx-doc.org/en/master/man/sphinx-build.html>.

- Build documentation:

`sphinx-build -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">html|epub|text|latex|man|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source_dir</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/build_dir</span>

- Build documentations intended for readthedocs.io (requires the sphinx-rtd-theme pip package):

`sphinx-build -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">html</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/docs_dir</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/build_dir</span>
