---
layout: page
title: common/protector (English)
description: "Protect or unprotect branches on GitHub repositories."
content_hash: b0fd7a1d407a11d545cb0fd07ba843ba92e1caa9
---
# protector

Protect or unprotect branches on GitHub repositories.
More information: <https://github.com/jcgay/protector>.

- Protect branches of a GitHub repository (create branch protection rules):

`protector `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branches_regex</span>` -repos `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">organization/repository</span>

- Use the dry run to see what would be protected (can also be used for freeing):

`protector -dry-run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branches_regex</span>` -repos `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">organization/repository</span>

- Free branches of a GitHub repository (delete branch protection rules):

`protector -free `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branches_regex</span>` -repos `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">organization/repository</span>
