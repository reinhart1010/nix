---
layout: page
title: linux/nmcli-connection (Türkçe)
description: "NetworkManager ile bağlantı yönetimi."
content_hash: cd7e9580800b71a9416a878b169148917fd4e173
related_topics:
  - title: English version
    url: /en/linux/nmcli-connection.html
    icon: bi bi-globe
---
# nmcli connection

NetworkManager ile bağlantı yönetimi.
Daha fazla bilgi: <https://networkmanager.dev/docs/api/latest/nmcli.html>.

- Tüm NetworkManager bağlantılarını listele (ad, UUID, tür ve aygıtı gösterir):

`nmcli connection`

- UUID belirterek bağlantıyı etkinleştir:

`nmcli connection up uuid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uuid</span>

- Bağlantıyı devre dışı bırak:

`nmcli connection down uuid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uuid</span>

- IPv4 ve IPv6 otomatik olarak yapılandırılan bir bağlantı oluştur:

`nmcli connection add ifname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arayüz_adı</span>` type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ethernet</span>` ipv4.method `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">auto</span>` ipv6.method `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">auto</span>

- Statik bir yalnızca IPv6 bağlantısı oluştur:

`nmcli connection add ifname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arayüz_adı</span>` type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ethernet</span>` ip6 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2001:db8::2/64</span>` gw6 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2001:db8::1</span>` ipv6.dns `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2001:db8::1</span>` ipv4.method `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ignore</span>

- Statik bir yalnızca IPv4 bağlantısı oluştur:

`nmcli connection add ifname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arayüz_adı</span>` type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ethernet</span>` ip4 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10.0.0.7/8</span>` gw4 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10.0.0.1</span>` ipv4.dns `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10.0.0.1</span>` ipv6.method `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ignore</span>

- Bir OVPN dosyasından OpenVPN kullanan bir VPN bağlantısı oluştur:

`nmcli connection import type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">openvpn</span>` file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vpn_yapılandırması.ovpn/dosyasının/yolu</span>
