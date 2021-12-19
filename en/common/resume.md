---
layout: page
title: common/resume (English)
description: "CLI tool to easily setup a new resume."
content_hash: b83f7a1d53d6de1771dca2395bbbaa5139605ed0
---
# resume

CLI tool to easily setup a new resume.
More information: <https://github.com/jsonresume/resume-cli>.

- Create a new `resume.json` file in the current working directory:

`resume init`

- Validate a `resume.json` against schema tests to ensure it complies with the standard:

`resume validate`

- Export a resume locally in a stylized HTML or PDF format:

`resume export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/html_or_pdf</span>

- Start a web server that serves a local `resume.json`:

`resume serve`
