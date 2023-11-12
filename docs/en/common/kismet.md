---
layout: page
title: common/kismet (English)
description: "A wireless network and device detector, sniffer, wardriving tool, and WIDS (wireless intrusion detection) framework."
content_hash: cf53d669e7a5cba495356b938ca791189c20b9ea
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# kismet

A wireless network and device detector, sniffer, wardriving tool, and WIDS (wireless intrusion detection) framework.
More information: <https://www.kismetwireless.net/>.

- Capture packets from a specific wireless interface:

`sudo kismet -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlan0</span>

- Monitor multiple channels on a wireless interface:

`sudo kismet -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlan0,wlan1</span>` -m`

- Capture packets and save them to a specific directory:

`sudo kismet -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlan0</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output</span>

- Start Kismet with a specific configuration file:

`sudo kismet -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlan0</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/config.conf</span>

- Monitor and log data to an SQLite database:

`sudo kismet -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlan0</span>` --log-to-db`

- Monitor using a specific data source:

`sudo kismet -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlan0</span>` --data-source=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rtl433</span>

- Enable alerts for specific events:

`sudo kismet -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlan0</span>` --enable-alert=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_ap</span>

- Display detailed information about a specific AP's packets:

`sudo kismet -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlan0</span>` --info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">BSSID</span>
