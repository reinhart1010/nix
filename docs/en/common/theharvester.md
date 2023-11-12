---
layout: page
title: common/theharvester (English)
description: "A tool designed to be used in the early stages of a penetration test."
content_hash: 8fc05b969db45787d9487490957fbf83bd9497ca
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# theHarvester

A tool designed to be used in the early stages of a penetration test.
More information: <https://github.com/laramies/theHarvester>.

- Gather information on a domain using Google:

`theHarvester --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domain_name</span>` --source google`

- Gather information on a domain using multiple sources:

`theHarvester --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domain_name</span>` --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">google,bing,crtsh</span>

- Change the limit of results to work with:

`theHarvester --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domain_name</span>` --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">google</span>` --limit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">200</span>

- Save the output to two files in XML and HTML format:

`theHarvester --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domain_name</span>` --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">google</span>` --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_file_name</span>

- Output all available options:

`theHarvester --help`
