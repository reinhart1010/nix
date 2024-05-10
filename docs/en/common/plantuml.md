---
layout: page
title: common/plantuml (English)
description: "Create UML diagrams from a plain text language and render them in different formats."
content_hash: 0be80864710932ca115f67aba085ae502c5232d8
last_modified_at: 2024-05-10
related_topics:
  - title: Deutsch version
    url: /de/common/plantuml.html
    icon: bi bi-globe
tldri18n_status: 2
---
# plantuml

Create UML diagrams from a plain text language and render them in different formats.
More information: <https://plantuml.com/en/command-line>.

- Render diagrams to default format (PNG):

`plantuml `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">diagram1.puml</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">diagram2.puml</span>

- Render a diagram in given format (e.g. `png`, `pdf`, `svg`, `txt`):

`plantuml -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">format</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">diagram.puml</span>

- Render all diagrams of a directory:

`plantuml `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/diagrams</span>

- Render a diagram to the output directory:

`plantuml -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">diagram.puml</span>

- Render a diagram without storing the diagram's source code (Note: It's stored by default when the `-nometadata` option isn't specified):

`plantuml -nometadata `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">diagram.png</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">diagram.puml</span>

- Retrieve source from a `plantuml` diagram's metadata:

`plantuml -metadata `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">diagram.png</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">diagram.puml</span>

- Render a diagram with the configuration file:

`plantuml -config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">config.cfg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">diagram.puml</span>

- Display help:

`plantuml -help`
