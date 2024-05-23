---
layout: page
title: common/idnits (English)
description: "Check internet-drafts for submission nits."
content_hash: 3e115e6f022992492b2336cee22b080a5a3eac95
last_modified_at: 2024-05-23
tldri18n_status: 2
---
# idnits

Check internet-drafts for submission nits.
Looks for violations of Section 2.1 and 2.2 of the requirements listed on <https://www.ietf.org/id-info/checklist>.
More information: <https://github.com/ietf-tools/idnits>.

- Check a file for nits:

`idnits `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.txt</span>

- Count nits without displaying them:

`idnits --nitcount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.txt</span>

- Show extra information about offending lines:

`idnits --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.txt</span>

- Expect the specified year in the boilerplate instead of the current year:

`idnits --year `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2021</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.txt</span>

- Assume the document is of the specified status:

`idnits --doctype `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">standard|informational|experimental|bcp|ps|ds</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.txt</span>
