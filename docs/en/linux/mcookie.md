---
layout: page
title: linux/mcookie (English)
description: "Generates random 128-bit hexadecimal numbers."
content_hash: 1d9d3f3167d6c769be712f5afca3c22156268313
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# mcookie

Generates random 128-bit hexadecimal numbers.
More information: <https://manned.org/mcookie>.

- Generate a random number:

`mcookie`

- Generate a random number, using the contents of a file as a seed for the randomness:

`mcookie --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Generate a random number, using a specific number of bytes from a file as a seed for the randomness:

`mcookie --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` --max-size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number_of_bytes</span>

- Print the details of the randomness used, such as the origin and seed for each source:

`mcookie --verbose`
