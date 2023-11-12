---
layout: page
title: common/phpspec (English)
description: "A Behaviour Driven Development tool for PHP."
content_hash: 9ec24a59f7a965ebe94798e9eb72d5c49eb65d26
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# phpspec

A Behaviour Driven Development tool for PHP.
More information: <https://phpspec.net>.

- Create a specification for a class:

`phpspec describe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">class_name</span>

- Run all specifications in the "spec" directory:

`phpspec run`

- Run a single specification:

`phpspec run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/class_specification_file</span>

- Run specifications using a specific configuration file:

`phpspec run -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/configuration_file</span>

- Run specifications using a specific bootstrap file:

`phpspec run -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/bootstrap_file</span>

- Disable code generation prompts:

`phpspec run --no-code-generation`

- Enable fake return values:

`phpspec run --fake`
