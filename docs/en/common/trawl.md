---
layout: page
title: common/trawl (English)
description: "Print out network interface information to the console, much like ifconfig/ipconfig/ip/ifdata."
content_hash: d1e518a3b0d1914645f4b5bea292fb8dfb373521
last_modified_at: 2024-04-18
tldri18n_status: 2
---
# trawl

Print out network interface information to the console, much like ifconfig/ipconfig/ip/ifdata.
More information: <https://github.com/robphoenix/trawl>.

- Show column names:

`trawl -n`

- Filter interface names using a case-insensitive regular expression:

`trawl -f wi`

- List available interfaces:

`trawl -i`

- Include the loopback interface:

`trawl -l`
