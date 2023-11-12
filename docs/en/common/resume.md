---
layout: page
title: common/resume (English)
description: "Easily setup a new resume."
content_hash: 9ac7dde34b037a5beff00e619a4ea6909819fe59
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# resume

Easily setup a new resume.
More information: <https://github.com/jsonresume/resume-cli>.

- Create a new `resume.json` file in the current working directory:

`resume init`

- Validate a `resume.json` against schema tests to ensure it complies with the standard:

`resume validate`

- Export a resume locally in a stylized HTML or PDF format:

`resume export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/html_or_pdf</span>

- Start a web server that serves a local `resume.json`:

`resume serve`
