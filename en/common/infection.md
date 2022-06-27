---
layout: page
title: common/infection (English)
description: "A mutation testing framework for PHP."
content_hash: ca5038a458e69bac435ec0ac409250c1dee700b9
---
# infection

A mutation testing framework for PHP.
More information: <https://infection.github.io>.

- Analyze code using the configuration file (or create one if it does not exist):

`infection`

- Use a specific number of threads:

`infection --threads `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number_of_threads</span>

- Specify a minimum Mutation Score Indicator (MSI):

`infection --min-msi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percentage</span>

- Specify a minimum covered code MSI:

`infection --min-covered-msi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percentage</span>

- Use a specific test framework (defaults to PHPUnit):

`infection --test-framework `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">phpunit|phpspec</span>

- Only mutate lines of code that are covered by tests:

`infection --only-covered`

- Display the mutation code that has been applied:

`infection --show-mutations`

- Specify the log verbosity:

`infection --log-verbosity `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">default|all|none</span>
