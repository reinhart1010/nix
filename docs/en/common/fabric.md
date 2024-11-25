---
layout: page
title: common/fabric (English)
description: "An open-source framework for augmenting humans using AI."
content_hash: c5b0f305ead41acf5fb57f50d31689f07498d30c
last_modified_at: 2024-11-25
tldri18n_status: 2
---
# fabric

An open-source framework for augmenting humans using AI.
Provides a modular framework for solving specific problems using a crowdsourced set of AI prompts.
More information: <https://github.com/danielmiessler/fabric>.

- Run the setup to configure fabric:

`fabric --setup`

- List all available patterns:

`fabric --listpatterns`

- Run a pattern with input from a file:

`fabric --pattern `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern_name</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file</span>

- Run a pattern on a YouTube video URL:

`fabric --youtube "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.youtube.com/watch?v=video_id</span>`" --pattern `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern_name</span>

- Chain patterns together by piping output from one to another:

`fabric --pattern `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern1</span>` | fabric --pattern `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern2</span>

- Run a custom user-defined pattern:

`fabric --pattern `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">custom_pattern_name</span>

- Run a pattern and save the output to a file:

`fabric --pattern `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern_name</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file</span>

- Run a pattern with the specified variables:

`fabric --pattern `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern_name</span>` --variable "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable_name</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>`"`
