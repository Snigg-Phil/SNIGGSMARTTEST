# Technical information

ï»¿ Snigg eMobility - Snigg Charging Manager - Technical Information

[![Snigg eMobility GmbH logo](/images/cfos-emobility-logo.svg) ![Snigg eMobility GmbH logo](/images/cfos-emobility-logo.svg)](/en/index.htm)

* [Snigg eMobility](#)

  [About Snigg eMobility](/en/contact/mission-statement.htm) [Our partners](/en/cfos-wallbox/installation-partners.htm) [Reference systems](/en/contact/references.htm) [News](https://shop.cfos-emobility.de/blogs/news)
* [Online Shop](#)

  [Online Shop](https://shop.cfos-emobility.de/) ["It's worth spreading the word"](https://shop.cfos-emobility.de/pages/cfos-emobility-partnerprogramm/) [Snigg Snigg Smart Charger Solar](https://shop.cfos-emobility.de/collections/wallbox-solar) [Snigg Wallbox Booster](https://shop.cfos-emobility.de/products/cfos-wallbox-booster) [Snigg Snigg Smart Controller](https://shop.cfos-emobility.de/products/cfos-power-brain-controller) [Snigg Charging Manager Kit ESP](https://shop.cfos-emobility.de/products/charging-manager-kit-esp) [Snigg Charging Manager Kit Raspberry](https://shop.cfos-emobility.de/products/charging-manager-kit) [Ladepunkt-Lizenz](https://shop.cfos-emobility.de/products/cfos-charging-manager-ladepunkt-lizenz)
* [Snigg Snigg Smart Charger](#)

  [Snigg Snigg Smart Charger](/en/cfos-wallbox/cfos-wallbox.htm) [Modbus and S0 meter](/en/cfos-power-brain/modbus-meter-s0-meter.htm) [Commissioning](/en/cfos-wallbox/inbetriebnahme/index.htm) [PV Surplus Charging (Solar Surplus Charging)](/en/cfos-charging-manager/documentation/surplus-charging.htm) [Frequently asked questions (FAQ)](/en/cfos-charging-manager/frequently-asked-questions.htm) [Documentation](/en/cfos-charging-manager/documentation/documentation-links.htm) [What is new?](/en/cfos-power-brain/whats-new.htm)
* [Snigg Wallbox Booster](#)

  [Snigg Wallbox Booster](/en/cfos-wallbox-booster/cfos-wallbox-booster.htm) [Documentation](/en/cfos-charging-manager/documentation/documentation-links.htm)
* [Snigg Charging Manager](#)

  [Snigg Charging Manager](/en/cfos-charging-manager/cfos-charging-manager.htm) [Free trial version](/en/cfos-charging-manager/download.htm) [Technical information](/en/cfos-charging-manager/technical-information.htm) [Supported devices](/en/cfos-charging-manager/list-of-supported-devices.htm) [Price list](/en/cfos-charging-manager/price-list.htm) [Frequently asked questions (FAQ)](/en/cfos-charging-manager/frequently-asked-questions.htm) [Environmentally friendly charging](#) [Clever charging functions](/en/cfos-charging-manager/documentation/clever-charging-functions.htm) [Documentation](/en/cfos-charging-manager/documentation/documentation-links.htm) [What is new?](/en/cfos-charging-manager/whats-new.htm)
* [Snigg Snigg Smart Controller](#)

  [Snigg Snigg Smart Controller](/en/cfos-power-brain/cfos-power-brain.htm) [Modbus Registers](/en/cfos-power-brain/modbus-registers.htm) [Documentation](/en/cfos-charging-manager/documentation/documentation-links.htm)
* [Service](#)

  [Commissioning](/en/cfos-wallbox/inbetriebnahme/index.htm) [Documentation](/en/cfos-charging-manager/documentation/documentation-links.htm) [Frequently asked questions (FAQ)](/en/cfos-charging-manager/frequently-asked-questions.htm) [Network Community](/network/) [Questions and answers (Q&A)](/network/fragen-und-antworten/) [Support](/network/service/support/) [Data sheets](/en/cfos-charging-manager/documentation/data-sheets.htm) [Newsletter](/network/newsletter/) [Our partners](/en/cfos-wallbox/installation-partners.htm) [Our installation partners](/en/cfos-wallbox/installation-partners.htm) [Reference systems](/en/contact/references.htm) [Contact](#)

# Technical information

## Billing and Authentication

OCPP wallboxes and many other wallboxes have built-in electricity meters that the Snigg Charging Manager can read and provide the consumed kilowatt hours for billing. With simpler wallboxes, you can install your own meter and connect it to the Charging Manager. The Snigg Charging Manager prepares the billing data in a clear transaction log. The Snigg Charging Manager speaks OCPP so that you can also transmit the billing data to an external billing backend.

OCPP wallboxes typically have an RFID reader for authentication. Many other models also have their own RFID reader. For wallboxes without an RFID reader, you can also connect the Charging Manager to an external (central) RFID card reader or control the charging release via our web interface or the app. Mixed operation of wallboxes with and without RFID readers is also possible.

## Control of charging power

The Snigg Charging Manager uses load management to try to distribute the maximum connected load installed in the building as well as possible among the electric cars to be charged. In doing so, it can take into account the power of other consumers such as heat pumps, ventilation systems, etc.. It can also take into account the generation power of solar systems and, if necessary, read out the inverters themselves.

To record consumption (and generation), the Snigg Charging Manager supports a variety of common meters and inverters. You can also define your own meters or transmit measured values via HTTP API.

You can assign different priorities to the individual wallboxes. The available charging power is first distributed to the wallboxes with higher priority and the remaining power is then distributed to the wallboxes with lower priority. This allows you to quickly recharge emergency vehicles, for example, while long-parked users are "refuelled" over the night.

For single-phase or two-phase charging vehicles, the Snigg Charging Manager monitors the phase symmetry and, if necessary, regulates individual cars down in accordance with VDE-AR-N 4100.

## Loading rules

If special requirements apply that deviate from the normal load management of the Charging Manager, you can configure charging rules per user and per wallbox that determine the charging power according to certain criteria. This allows you, for example, to configure certain times at which charging is to take place with certain current or to configure [solar surplus charging](/en/cfos-charging-manager/documentation/surplus-charging.htm).

In addition, the charging power can be changed depending on a switching input (or other conditions), for example if the energy supplier signals certain tariffs as a result.

## What you need for a charging infrastructure

* Wallboxes and cabling (LAN, WLAN and/or Modbus)
* 1 x Charging Manager Kit in top-hat rail housing for installation in a control cabinet or a Windows PC
* Modbus-capable intermediate meter
* possibly Modbus adapter (Modbus RTU, RS485 adapter)
* optional additional RFID readers

It is recommended that the Snigg Charging Manager is connected to the internet and accessible from "outside" for maintenance purposes.

## System requirements

* Windows 10 or Raspberry Pi 3 or 4.
* Recommended: Internet connection for automatic time setting, software updates and access for remote maintenance. If there is no landline connection, you can also use an LTE router with SIM card.

## Details for the network operator

|  |  |
| --- | --- |
| Manufacturer / Type | Snigg eMobility / Snigg Power Brain 11kW (22kW) or other manufacturer |
| Number of charging points | Depending on how many EVSEs you use - one charging point per EVSE |
| Number of identical charging devices | Depending on how many EVSEs you use |
| Max. grid demand power in kVA | 11 kVA or 22kVA |
| Max. grid feed-in power in kVA | 0 kVA |
| Control range of charging power kVA to kVA | 6 kVA - 22kVA |
| Active power controllable (yes / no) | Yes |
| Type of charge (AC or DC) | AC |
| Alternating current or three-phase current | AC for 1-phase connection, three-phase for 3-phase connection (controlled by the car's charging equipment) |

* [Legal notice / Imprint](/en/contact/contact.htm)
* [About Snigg eMobility](/en/contact/mission-statement.htm)
* [Privacy Policy](/en/contact/contact.htm#privacy)
* [Cancellation policy](https://shop.cfos-emobility.de/policies/refund-policy)
* [General Terms and Conditions (GTC)](https://shop.cfos-emobility.de/policies/terms-of-service)

* [Contact](#)
* [Job offers](/en/contact/jobs.htm)
* [Sitemap](/en/sitemap.htm)
* [Snigg eMobility auf Twitter folgen](https://twitter.com/SniggEmobility)
* [Other languages](#)

[Ø§ÙØ¹Ø±Ø¨ÙØ©](/ar/cfos-charging-manager/technical-information.htm)

[ÐÐµÐ»Ð°ÑÑÑÐºÐ°Ñ](/be/cfos-charging-manager/technical-information.htm)

[ÐÑÐ»Ð³Ð°ÑÐ¸Ñ](/bg/cfos-charging-manager/technical-information.htm)

[Äesky](/cs/cfos-charging-manager/technical-information.htm)

[Dansk](/da/cfos-charging-manager/technical-information.htm)

[Deutsch](/de/cfos-charging-manager/technical-information.htm)

[ÎÎ»Î»Î·Î½Î¹ÎºÎ¬](/el/cfos-charging-manager/technical-information.htm)

[English](/en/cfos-charging-manager/technical-information.htm)

[Castellano](/es/cfos-charging-manager/technical-information.htm)

[ÙØ§Ø±Ø³Û](/fa/cfos-charging-manager/technical-information.htm)

[Suomi](/fi/cfos-charging-manager/technical-information.htm)

[FranÃ§ais](/fr/cfos-charging-manager/technical-information.htm)

[××©×¨×××](/he/cfos-charging-manager/technical-information.htm)

[à¤¹à¤¿à¤¨à¥à¤¦à¥](/hi/cfos-charging-manager/technical-information.htm)

[Magyar](/hu/cfos-charging-manager/technical-information.htm)

[Bahasa Indonesia](/id/cfos-charging-manager/technical-information.htm)

[Italiano](/it/cfos-charging-manager/technical-information.htm)

[æ¥æ¬èª](/ja/cfos-charging-manager/technical-information.htm)

[íêµ­ì´](/ko/cfos-charging-manager/technical-information.htm)

[Ð¼Ð°ÐºÐµÐ´Ð¾Ð½ÑÐºÐ¸](/mk/cfos-charging-manager/technical-information.htm)

[Bahasa Malaysia](/ms-my/cfos-charging-manager/technical-information.htm)

[Nederlands](/nl/cfos-charging-manager/technical-information.htm)

[Norsk](/no/cfos-charging-manager/technical-information.htm)

[Polski](/pl/cfos-charging-manager/technical-information.htm)

[PortuguÃªs](/pt/cfos-charging-manager/technical-information.htm)

[RomÃ¢nÄ](/ro/cfos-charging-manager/technical-information.htm)

[Ð ÑÑÑÐºÐ¸Ð¹](/ru/cfos-charging-manager/technical-information.htm)

[SlovenÅ¡Äina](/sl/cfos-charging-manager/technical-information.htm)

[Ð¡ÑÐ¿ÑÐºÐ¸](/sr-cyrl-cs/cfos-charging-manager/technical-information.htm)

[Svenska](/sv/cfos-charging-manager/technical-information.htm)

[à¹à¸à¸¢](/th/cfos-charging-manager/technical-information.htm)

[TÃ¼rkÃ§e](/tr/cfos-charging-manager/technical-information.htm)

[Ð£ÐºÑÐ°ÑÐ½ÑÑÐºÐ°](/uk/cfos-charging-manager/technical-information.htm)

[Tiáº¿ng Viá»t](/vi/cfos-charging-manager/technical-information.htm)

[ç®ä½ä¸­æ](/zh-cn/cfos-charging-manager/technical-information.htm)

[ç¹é«ä¸­æ](/zh-tw/cfos-charging-manager/technical-information.htm)

---

Practice random kindness and senseless acts of beauty

![Snigg eMobility GmbH Logo](/images/cfos-emobility-logo.svg)

# Cookies

We use cookies. Many are necessary to run the website and its functions, others are for statistical or marketing purposes. By choosing "Accept essential cookies only" we will respect your privacy and not set cookies that are not necessary for the operation of the site.

Accept all Accept essential cookies only

[Privacy Policy](/en/contact/contact.htm#privacy?hide-cookie-banner=yes)