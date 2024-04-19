---
layout: page
title: common/blackfire (English)
description: "Monitor, profile and test a PHP application."
content_hash: 5898845566378527e1d576d3b8e320c545ac65d5
last_modified_at: 2024-04-19
related_topics:
  - title: italiano version
    url: /it/common/blackfire.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/blackfire.html
    icon: bi bi-globe
tldri18n_status: 2
---
# blackfire

Monitor, profile and test a PHP application.
More information: <https://blackfire.io>.

- Initialize and configure the Blackfire client:

`blackfire config`

- Launch the Blackfire agent:

`blackfire agent`

- Launch the Blackfire agent on a specific socket:

`blackfire agent --socket="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tcp://127.0.0.1:8307</span>`"`

- Run the profiler on a specific program:

`blackfire run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">php path/to/file.php</span>

- Run the profiler and collect 10 samples:

`blackfire --samples `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">php path/to/file.php</span>

- Run the profiler and output results as JSON:

`blackfire --json run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">php path/to/file.php</span>

- Upload a profiler file to the Blackfire web service:

`blackfire upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- View the status of profiles on the Blackfire web service:

`blackfire status`
