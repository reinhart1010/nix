---
layout: page
title: common/iperf (English)
description: "Measure network bandwidth between computers."
content_hash: d50f0ab9cd86b254d8eb1372b7eb2354baec5609
---
# iperf

Measure network bandwidth between computers.
More information: <https://iperf.fr>.

- Run on server:

`iperf -s`

- Run on server using UDP mode and set server port to listen on 5001:

`iperf -u -s -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5001</span>

- Run on client:

`iperf -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server_address</span>

- Run on client every 2 seconds:

`iperf -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server_address</span>` -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>

- Run on client with 5 parallel threads:

`iperf -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server_address</span>` -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>

- Run on client using UDP mode:

`iperf -u -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server_address</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5001</span>
