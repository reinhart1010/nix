---
layout: page
title: common/weasyprint (English)
description: "Render HTML to PDF or PNG."
content_hash: 93918913e2c7767742dd131acbedc7aa9fe3e67e
last_modified_at: 2023-11-12
related_topics:
  - title: русский version
    url: /ru/common/weasyprint.html
    icon: bi bi-globe
tldri18n_status: 2
---
# weasyprint

Render HTML to PDF or PNG.
More information: <https://weasyprint.org/>.

- Render an HTML file to PDF:

`weasyprint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.html</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output</span>`.pdf`

- Render an HTML file to PNG, including an additional user stylesheet:

`weasyprint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.html</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output</span>`.png --stylesheet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/stylesheet.css</span>

- Output additional debugging information when rendering:

`weasyprint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.html</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output</span>`.pdf --verbose`

- Specify a custom resolution when outputting to PNG:

`weasyprint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.html</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output</span>`.png --resolution `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">300</span>

- Specify a base URL for relative URLs in the input HTML file:

`weasyprint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.html</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output</span>`.png --base-url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_or_filename</span>
