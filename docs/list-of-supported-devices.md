[![Snigg eMobility GmbH logo](/images/cfos-emobility-logo.svg) ![Snigg eMobility GmbH logo](/images/cfos-emobility-logo.svg)](/en/index.htm)

* [Snigg eMobility](#)

  [About Snigg eMobility](/en/contact/mission-statement.htm) [Our partners](/en/cfos-wallbox/installation-partners.htm) [Reference systems](/en/contact/references.htm) [News](https://shop.cfos-emobility.de/blogs/news)
* [Online Shop](#)

  [Online Shop](https://shop.cfos-emobility.de/) ["It's worth spreading the word"](https://shop.cfos-emobility.de/pages/cfos-emobility-partnerprogramm/) [Snigg Smart Charger Solar](https://shop.cfos-emobility.de/collections/wallbox-solar) [Snigg Smart Charger Booster](https://shop.cfos-emobility.de/products/cfos-wallbox-booster) [Snigg Smart Controller](https://shop.cfos-emobility.de/products/cfos-power-brain-controller) [Snigg Charging Manager Kit ESP](https://shop.cfos-emobility.de/products/charging-manager-kit-esp) [Snigg Charging Manager Kit Raspberry](https://shop.cfos-emobility.de/products/charging-manager-kit) [Ladepunkt-Lizenz](https://shop.cfos-emobility.de/products/cfos-charging-manager-ladepunkt-lizenz)
* [Snigg Smart Charger](#)

  [Snigg Smart Charger](/en/cfos-wallbox/cfos-wallbox.htm) [Modbus and S0 meter](/en/cfos-power-brain/modbus-meter-s0-meter.htm) [Commissioning](/en/cfos-wallbox/inbetriebnahme/index.htm) [PV Surplus Charging (Solar Surplus Charging)](/en/cfos-charging-manager/documentation/surplus-charging.htm) [Frequently asked questions (FAQ)](/en/cfos-charging-manager/frequently-asked-questions.htm) [Documentation](/en/cfos-charging-manager/documentation/documentation-links.htm) [What is new?](/en/cfos-power-brain/whats-new.htm)
* [Snigg Smart Charger Booster](#)

  [Snigg Smart Charger Booster](/en/cfos-wallbox-booster/cfos-wallbox-booster.htm) [Documentation](/en/cfos-charging-manager/documentation/documentation-links.htm)
* [Snigg Charging Manager](#)

  [Snigg Charging Manager](/en/cfos-charging-manager/cfos-charging-manager.htm) [Free trial version](/en/cfos-charging-manager/download.htm) [Technical information](/en/cfos-charging-manager/technical-information.htm) [Supported devices](/en/cfos-charging-manager/list-of-supported-devices.htm) [Price list](/en/cfos-charging-manager/price-list.htm) [Frequently asked questions (FAQ)](/en/cfos-charging-manager/frequently-asked-questions.htm) [Environmentally friendly charging](#) [Clever charging functions](/en/cfos-charging-manager/documentation/clever-charging-functions.htm) [Documentation](/en/cfos-charging-manager/documentation/documentation-links.htm) [What is new?](/en/cfos-charging-manager/whats-new.htm)
* [Snigg Smart Controller](#)

  [Snigg Smart Controller](/en/cfos-power-brain/cfos-power-brain.htm) [Modbus Registers](/en/cfos-power-brain/modbus-registers.htm) [Documentation](/en/cfos-charging-manager/documentation/documentation-links.htm)
* [Service](#)

  [Commissioning](/en/cfos-wallbox/inbetriebnahme/index.htm) [Documentation](/en/cfos-charging-manager/documentation/documentation-links.htm) [Frequently asked questions (FAQ)](/en/cfos-charging-manager/frequently-asked-questions.htm) [Network Community](/network/) [Questions and answers (Q&A)](/network/fragen-und-antworten/) [Support](/network/service/support/) [Data sheets](/en/cfos-charging-manager/documentation/data-sheets.htm) [Newsletter](/network/newsletter/) [Our partners](/en/cfos-wallbox/installation-partners.htm) [Our installation partners](/en/cfos-wallbox/installation-partners.htm) [Reference systems](/en/contact/references.htm) [Contact](#)

Supported wallboxes, intermediate meters, inverters, battery storage, OCPP backends, other devices
==================================================================================================

#### [Wallboxes](#wallbox-list)

#### [Inverters, smart meters and battery storage](#inverter-list)

#### [Intermediate meter](#meter-list)

#### [Controllable battery storage (experimental)](#battery-storage-list)

#### [Controllable heat pumps (experimental)](#heatpump-list)

#### [OCPP 1.6 backends](#ocpp-backend-list)

**Note**: The devices and remote stations listed here have been tested with the software version of the respective manufacturer specified in the tables in simple charging processes and simple basic functions. We do not guarantee that the manufacturer will change the functionality through a software update or model update in such a way that the interoperability with the Snigg Charging Manager or Snigg Smart Controller is no longer given. You can ask the respective manufacturer whether the functionality still corresponds to the status indicated in our table.  
 means: Here you can download a counter definition for the corresponding device.

You must check whether the Snigg Charging Manager is compatible with the remote stations by testing your specific use case. To do this, you can [download the free test version of the Snigg Charging Manager for Windows or Raspberry Pi](/en/cfos-charging-manager/download.htm) and test for yourself whether the respective device or the OCPP backend is compatible.

Integration of new wallboxes
----------------------------

**Note**: We are happy to add new, previously unsupported wallboxes. We offer a free OCPP wallbox integration test for this purpose. For wallboxes with other protocols, a corresponding control unit may need to be implemented. This usually involves little effort and is also free of charge. Is your wallbox not yet in our system? [Make an integration enquiry here](#).

Supported EVSEs
---------------

| EVSE | Software status |
| --- | --- |
| [Snigg Smart Controller](/en/cfos-power-brain/cfos-power-brain.htm) | 12/2021 |
| All wallboxes with sufficiently supported OCPP 1.6 (JSON) We have tested the Snigg Charging Manager for compatibility during the OCPP Plugfest and via various backends. If you want to make sure that your OCPP device works with the Snigg Charging Manager, please contact us for a free remote test. | |
| **OCPP** | |
| [Snigg Smart Charger (OCPP 1.6)](/en/cfos-power-brain/cfos-power-brain.htm) | 12/2021 |
| [ABB Terra AC 22 (OCPP 1.6)](https://new.abb.com/ev-charging/terra-ac-wallbox) | 12/2021 |
| [ABB Terra DC (OCPP 1.6)](https://new.abb.com/ev-charging/de/terra-dc-wandladestation) | 09/2023 |
| [ABL eMH2 (OCPP 1.6)](https://www.ablmobility.de/de/produkte/wallbox-emh2.php) | 12/2021 |
| [ABL eMH3 (OCPP 1.6) ohne Eichrecht (mit Eichrecht kommen die ZÃ¤hlerwerte zu selten, evtl. mit neuer ABL firmware behoben)](https://www.ablmobility.de/de/produkte/wallbox-emh3.php) | 07/2022 |
| [ABL eM4 (OCPP 1.6)](https://www.ablmobility.de/de/produkte/wallbox-emh4.php) | 09/2023 |
| [Alfen Eve Single Pro-Line / Double Pro-Line](https://alfen.com/en-de/eve-single-pro-line) (OCPP 1.6) | 08/2023 |
| [Alpitronic Hypercharger](https://www.hypercharger.it/) (OCPP 1.6) Software version as of 1.7.3 required | 02/2023 |
| [Autel MaxiCharger AC Wallbox](https://autelenergy.eu/products/maxicharger-ac-wallbox) (OCPP 1.6) Software version from 1.7.3 required | 02/2023 |
| [Autel MaxiCharger DC Fast](https://autelenergy.eu/products/maxicharger-dc-high-power) (OCPP 1.6) | 05/2024 |
| Bender Controller (OCPP 1.6) various wallbox manufacturers, see below | 12/2023 |
| [BERGER DM30 (DC SchnellladegerÃ¤t)](https://shop.berger-stromversorgungen.de/ladestationen-fuer-elektrofahrzeuge/dc-ladestationen/mobile-dc-ladestationen/452/bevse-dm30-400-950-80) | 02/2022 |
| [BERGER AX32](https://www.berger-stromversorgungen.de/?s=ax32) | 04/2022 |
| [Charge Amps Dawn (OCPP 1.6)](https://www.chargeamps.com/de/product/charge-amps-dawn/) | 02/2024 |
| [Charge Amps Halo (OCPP 1.6)](https://www.chargeamps.com/de/product/charge-amps-halo/) | 08/2023 |
| [CTEK Chargestorm Connected 2 (OCPP 1.6)](https://www.ctek.com/de/ladestationen-fur-elektrofahrzeuge/chargestorm-connected-2) | 08/2023 |
| [Circontrol Raption 50 DC charger (OCPP 1.6)](https://circontrol.com/circontrol-raption-50/) | 05/2024 |
| [DELTA Ladestationen AC & DC (OCPP 1.6)](https://www.deltaevcharging.com/product) | 11/2022 |
| [Eaton Green Motion](https://www.eaton.com/at/de-de/catalog/emobility/green-motion-home.html) (OCPP 1.6) | 11/2024 |
| [ecotap DC60 (OCPP 1.6)](https://www.ecotap.nl/de/dc60/) | 06/2023 |
| [Elexon sxHPC80 und A1 (OCPP 1.6) No phase current values](https://elexon-charging.com) | 11/2023 |
| Elinta CityCharge Mini 2 (OCPP 1.6) No phase current values | 07/2024 |
| [EN Plus Wallboxen mit OCPP 1.6 JSON (z.B. Autoaid, Entratek, AMS Energy, etc.)](https://www.en-plustech.com/) As of firmware 1.3.234. | 09/2023 |
| [EnerCharge ECC320 mit OCPP 1.6 JSON](https://www.keba.com/de/emobility/products/dc-ladestationen/kecontact-dca10-autonomous-charger) Limited range of functions. | 01/2025 |
| [EM2GO Pro Power mit OCPP 1.6 JSON](https://em2go.de/collections/wallboxen) from firmware AC\_DE3\_1.12 | 10/2024 |
| [Etrel INCH (OCPP 1.6)](https://etrel.com/products/interactivecharger/product-page.php) | 10/2024 |
| [EVBox Elvi (OCPP 1.6)](https://evbox.com/de-de/ladestationen/elvi) | 07/2022 |
| [Entratek Power Dot Pro (OCPP 1.6)](https://www.entratek-shop.de/p/wallbox-power-dot-pro-7-5m-11kw-mit-app) | 12/2021 |
| Compleo / Innogy eBox professional S (OCPP 1.6) | 12/2021 |
| [Garo GLB+/GTB+ (OCPP 1.6)](https://www.garoelectric.com/garo-charging-stations/charging-at-home) | 02/2023 |
| Garo Entity Compact, Entity Pro, Entity Pro MID (OCPP 1.6) | 09/2024 |
| GSAB 2S1300DC60Triple DC Charger (OCPP 1.6) | 03/2023 |
| [go-e Charger Gemini 2.0 (OCPP 1.6)](https://shop.go-e.com/de-de/wallbox/go-e-charger-gemini-2-0-11-kw/) | 08/2024 |
| [Hager Witty Share(OCPP 1.6)](https://hager.com/de/katalog/ladestationen/ladestationen) | 08/2023 |
| [INRO Elektrotechnik Pantabox(OCPP 1.6)](https://www.pantabox.de/) | 06/2024 |
| [Kathrein Wallbox AC40 (OCPP 1.6)](https://www.kathrein-ds.com/produkte/emobility-wallbox/kwb-ac40) | 07/2024 |
| [Keba KeContact P30 x-series (OCPP 1.6)](https://www.keba.com/en/emobility/products/x-series/x-series) | 12/2021 |
| [Kempower C800 series (OCPP 1.6)](https://kempower.com/de/solution/kempower-station-charger/) | 11/2023 |
| [Lade.ZEIT AC Charger (OCPP 1.6)](https://www.lade-zeit.de/) | 08/2023 |
| [Mennekes Amtron Professional+ 22kW (OCPP 1.6)](https://www.chargeupyourday.de/ps/amtron/#) | 12/2021 |
| [Phihong / ZEROVA DC EV Chargers (OCPP 1.6)](https://shop.get-power.de/DC-HPC-Ladeloesungen/ZEROVA/) | 02/2023 |
| [Pion Highrock (Bender CC613 controller) (OCPP 1.6)](https://pion-ag.com/produkte/ladesaeulen-highrock/) | 06/2023 |
| [Schneider EVlink G4 Smart und Parkplatz 2, Pro AC (OCPP 1.6)](https://www.se.com/de/de/product-range/63506-evlink-wallbox-g4-smart-kfw-f%C3%B6rderf%C3%A4hig/) | 05/2022 |
| [Siemens SiCharge D (OCPP 1.6)](https://www.siemens.com/de/de/produkte/energie/emobility/sicharge-d.html) | 06/2024 |
| SBRS DC Twin (OCPP 1.6) | 12/2024 |
| [StarCharge Athena 60, Saturn 22 (OCPP 1.6)](https://www.starcharge.com/Aurora?id=1278?product=Athena60) | 01/2024 |
| [Technagon (OCPP 1.6)](https://technagon.de/en/produkte/) | 12/2022 |
| [Technivolt 1100 Smart (OCPP 1.6)](https://www.technivolt.eu/de/wallboxen/technivolt_1100_smart) | 12/2022 |
| [Vestel EVC04 / Webasto Unite (OCPP 1.6), Vestel firmware v3.131.0+ required](https://www.vestel-echarger.com/EVC04.html) | 11/2023 |
| Wallbe Pro (Compleo) (OCPP 1.6) | 12/2022 |
| [Wallbox Copper SB, Commander 2 (OCPP 1.6) ab Wallbox Firmware 5.17.73](https://wallbox.com/de_de/copper) | 01/2024 |
| [Wallbox Pulsar (OCPP 1.6), eingeschrÃ¤nkt, da kein RFID LEser](https://wallbox.com/de_de/pulsar) | 08/2024 |
| [Webasto Live (OCPP 1.6)](https://charging.webasto.com/int/products/webasto-live/) | 01/2022 |
| [WEG WEMOB WALL (OCPP 1.6)](https://www.weg.net/catalog/weg/MC/fr/WDC_CRITICAL_POWER_WEMOB2) | 04/2025 |
| [weeyu AC EV Charger (OCPP 1.6)](https://www.wyevcharger.com/ac-charging-station/) | 02/2023 |
| [XCharge C6EU (OCPP 1.6)](https://www.xcharge.com/) | 07/2025 |
| [Zaptec Go (OCPP 1.6)](https://www.zaptec.com/de/ladeloesungen/zaptec-go) | 03/2025 |
| **Modbus, HTTP, etc.** | |
| [ABL eMH1](https://www.ablmobility.de/de/ladestation/wallbox-emh1.php) (Modbus ASCII) | 12/2021 |
| [Alfen Eve Single/Double (Modbus)](https://alfen.com/eve-single-pro-line) | 07/2022 |
| [Alphatec AW1eM (Modbus)](https://shop.alphatec-systeme.de/emobility/wallbox-ladesaeule/?p=1) | 08/2022 |
| [Alpitronic Hypercharger 4.0](https://www.hypercharger.it/) (Modbus)From model 4.0 (HYC\_400) | 03/2024 |
| Bender Controller, Modbus TCPvarious wallbox manufacturers, see below | 12/2023 |
| [Chargepoint Cloud](https://www.chargepoint.com/) Wallboxen, die dort eingebunden sind, z.B. die CP4320 (proprietÃ¤r). Lange Reaktionszeit beachten. Status derzeit unklar, experiementell | 03/2023 |
| [Circontrol eHome (Modbus)](https://circontrol.com/ev-charging/ac-wallbox/ehome-series/) | 03/2023 |
| [Compleo Solo advanced (Modbus)](https://www.compleo-cs.com/ladeloesungen/wallbox/compleo-solo) | 03/2022 |
| [DELTA Ladestationen AC & DC (Modbus)](https://www.deltaevcharging.com/product) | 11/2022 |
| [easee Home / One / Charge](https://easee.com/de/zuhause-laden/) (Cloud HTTP), Support abgekÃ¼ndigt, nicht empfohlen! | 04/2022 |
| [Eaton Green Motion](https://www.eaton.com/at/de-de/catalog/emobility/green-motion-home.html)(Modbus) | 11/2024 |
| [elexon A1 (Modus, AIX ACCT)](https://www.elexon-charging.com/wp-content/uploads/2022/04/elexon_DB_A1Serie_EN_052020.pdf) | 07/2022 |
| [go-e HOME+ Mobile, go-eCharger HOMEfix](https://go-e.co/produkte/go-echarger-home/) und [SMARTFOX Car Charger](https://www.smartfox.at/car-charger.html) (HTTP) | 12/2021 |
| [hesotec eSat eBox](https://electrify.hesotec.de/produkte/) (Modbus). Attention: The box cannot provide sufficient OCPP (as of 03/2023). | 10/2022 |
| [Heidelberg / Amperfied Energy Control, connect.home, connect.business, connect.solar and Walther-Werke BASICEVO PRO](https://wallbox.heidelberg.com/#wallbox-energy-control) (Modbus) | 01/2023 |
| Compleo / Innogy eBox professional S (Modbus) | 12/2021 |
| [Juice Charger me (Modbus, wie Mennekes Amtron Professional)](https://en.juice-world.com/juice-charger-me) (Modbus) | 12/2021 |
| Keba KeContact P30 [c-series](https://www.keba.com/en/emobility/products/c-series/c-series) and [x-series](https://www.keba.com/en/emobility/products/x-series/x-series), BMW Wallbox Plus/Connect via Keba UDP, Keba P30 Green Edition via Modbus TCP | 06/2023 |
| [Mennekes Amtron Professional+ 22kW (Modbus)](https://www.chargeupyourday.de/ps/amtron/#) | 12/2021 |
| Gautzsch Netz Do (Modbus) | 03/2022 |
| OBO Bettermann [Ion](https://www.obo.de/produkte/gebaeudeinstallation/produkthighlights/ion-wallbox/) | 05/2023 |
| [Schneider EVlink G4 Smart und Parkplatz 2 & 3, Pro AC (Modbus, 1 connector)](https://www.se.com/de/de/product-range/63506-evlink-wallbox-g4-smart-kfw-f%C3%B6rderf%C3%A4hig/) | 05/2022 |
| [SMA EV Charger (HTTP)](https://www.sma.de/en/products/e-mobility-charging-solutions/sma-ev-charger-74-22). [Wichtiger Hinweis!](/en/cfos-charging-manager/documentation/wallbox-instructions.htm) | 02/2023 |
| [Technagon Modbus](https://technagon.de/en/produkte/) | 12/2022 |
| Tesla Wall Connector Gen 2 (only max. 1 on one RS485 port, unfortunately produces many communication errors), not Gen 3 | 06/2023 |
| [Tinkerforge Warp 2](https://www.warp-charger.com/) | 02/2023 |
| Wallbe Eco 2.0/2.0s, Pro, Pro plus (Modbus) | 12/2022 |
| [Vestel EVC04 (Modbus)](https://www.vestel-echarger.com/EVC04.html) | 05/2022 |
| Webasto Next (Modbus TCP) | 02/2024 |
| [weeyu AC EV Charger (Modbus)](https://www.wyevcharger.com/ac-charging-station/) | 02/2023 |
| [WeidmÃ¼ller EV Smart models (Modbus)](https://www.weidmueller.com/int/solutions/e_mobility/ac_smart_family.jsp) | 04/2023 |

Bender Controller
-----------------

The following wallbox models have a Bender controller on board and should work with the Snigg Charging Manager. We would be pleased to receive feedback on how it works with these devices.

|  |
| --- |
| Ebee wallbox / Optec |
| Ensto Chago Wallbox |
| Garo GLB, GLB+, GTB+, LS4 und LS4 compact |
| Juice Charger Me |
| Mennekes Amtron ChargeControl, Amedio Professional |
| Pion |
| Spelsberg Smart Pro Polar |
| StÃ¶hr Design-Line Business / Design-Tower |
| Ubitricity (Bender controller) |
| Walther-Werke smartEVO Duo+ |
| Webasto live |

Supported inverters, smart meters and battery storage systems
-------------------------------------------------------------

| Inverter | Software status |
| --- | --- |
| Inverters can also be integrated as generation meters. Many inverters support **SunSpec**, i.e. you can use SunSpec Solar Inverter / Meter as the meter type. This also applies to the grid reference meters / smart meters installed in solar systems. Here is a selection of devices tested by our customers. Similar devices will probably also work. **Note: Fronius, Kostal and SMA have very good SunSpec support. This means that if the manufacturer specifies SunSpec for the model of inverter, smart meter or battery storage system, it should work well with the Snigg Charging Manager.** Please report successfully tested devices to us and we will add them to the list here. | |
| Deye LP1/LP3 und Deye Hochvolt Wechselrichter | 10/2024 |
| E3/DC GmbH, S10 E AIO Blackline (SunSpec) | 12/2021 |
| E3/DC GmbH, S10 X Compact (Modbus) | 09/2023 |
| Fronius, Smart Meter, alle Modelle mit SunSpec | 02/2022 |
| Fronius, Symo und Primo, alle Modelle mit SunSpec | 12/2021 |
| [Hoymiles HMS-1600 inverter](/files/meter-definitions/hoymiles.json) | 06/2024 |
| KACO new energy, blueplanet, alle Modelle mit SunSpec | 12/2021 |
| [Kostal, Piko 10 (HTTP)](/files/meter-definitions/meter_kostal_pico10.json) | 05/2023 |
| KOSTAL, PLENTICORE, alle Modelle mit SunSpec | 12/2021 |
| KOSTAL, Smart Energy Meter, alle Modelle mit SunSpec | 12/2021 |
| [Kostal Piko 8.5 and Kostal BA Sensor Module](/files/meter-definitions/kostal-meter-definitions.zip) | 11/2021 |
| RCT DC10 (via RS485) | 06/2025 |
| SENEC (via HTTP) | 06/2023 |
| [Senertec Dachs BHKW](/files/meter-definitions/meter_dachs.json) | 02/2023 |
| SMA, alle Modelle mit SunSpec | 12/2021 |
| SMA, alle Tripower (STPxx000-tl) | 12/2021 |
| [SMA, Cluster Controller](/files/meter-definitions/sma_cluster_ctl.json) | 09/2024 |
| [SMA, Data Manager (PV-production)](/files/meter-definitions/sma_data_manager.json) | 09/2024 |
| [SMA, Data Manager Grid (PV-production)](/files/meter-definitions/sma_datamgr_grid.json) | 09/2024 |
| SMA Sunny Boy | 12/2021 |
| SMA STPxx-3SE-40 / STP SE Battery | 08/2024 |
| SMA, Sunny Home Manager 2.0 (as grid reference meter, via UDP multicast) | 12/2021 |
| SMA Sunny Island 4.4 | 12/2021 |
| SMA Sunny Tripower 8.0 STP8-3AV-40 | 12/2021 |
| Sofar HYD/G3 | 10/2024 |
| SolarEdge, alle Modelle mit SunSpec | 12/2021 |
| SolarEdge NetzbezugszÃ¤hler mit SunSpec **Liefert manchmal falsche Werte, ggf. anderen bidirektionen ZÃ¤hler benutzen.** | 06/2023 |
| Solar-Log | 12/2021 |
| [Solarman Logger (IGEN Tech)](/files/meter-definitions/solarman_logger.json) | 08/2023 |
| Sonnen ZÃ¤hler (Batteriespeicher, Erzeugung und Verbrauch) | 12/2021 |
| Sungrow Hybrid Inverter ARM\_SAPPHIRE-H\_V (SunSpec) | 07/2022 |
| Sungrow, Inverter and battery storage, Modbus | 05/2023 |
| [Varta Element S4 memory](/files/meter-definitions/varta_element_s4.json) | 02/2023 |
| [Varta Element S4 Mains supply meter](/files/meter-definitions/varta_element_s4_grid.json) | 02/2023 |
| Victron (diverse) | 09/2023 |

Supported intermediate meters
-----------------------------

| Intermediate meter | Software status |
| --- | --- |
| [ABB B23 112-100](https://new.abb.com/products/de/2CMA100164R1000/wirkenergiemessung-kl-b)- Supplier: [Stark Elektronik](https://www.stark-elektronik.de/epages/63653058.sf/de_DE/?ObjectPath=/Shops/63653058/Products/STB23112100) | 12/2021 |
| [ABB B24 112-100](https://new.abb.com/products/de/2CMA100178R1000/wirkenergiemessung-kl-b)- Supplier: [Stark Elektronik](https://www.stark-elektronik.de/epages/63653058.sf/de_DE/?ObjectPath=/Shops/63653058/Products/STB24112100) | 12/2021 |
| [Bauer BSM](https://www.bzr-bauer.de/produkte/bsm/) | 07/2022 |
| [Carlo Gavazzi EM300/ET300 (experimental)](/files/meter-definitions/meter_cgavazzi.json) | 11/2023 |
| DTSU666 DTSU666H | 01/2021 |
| [EARU EA777](/files/meter-definitions/earu_ea777.json) | 05/2022 |
| [Eastron SDM630, SDM630MCT, SDM72DM-V2](https://www.eastroneurope.com/products/view/sdm630modbus) | 12/2021 |
| [Eastron SDM72D-M V1](https://www.eastroneurope.com/products/view/sdm72modbus) | 12/2021 |
| [Eastron SDM72DM V1.1/1.5](/files/meter-definitions/eastron_sdm72d-modb-ext.json) | 05/2022 |
| [Eastron SDM72DM V1.1/1.5. active power = power L1+L2+L3](/files/meter-definitions/eastron_sdm72d-modb-ext2.json) | 03/2023 |
| Elgris Smart Meter LAN / WLAN | 07/2022 |
| [Elgris Smart Meter LAN, Alternative](/files/meter-definitions/meter_elgris_lan2.json) | 10/2024 |
| [EMH iML e-moc](https://emh-metering.com/produkte/e-mobility/iml-e-moc-fuer-kompakte-e-mobility-loesungen/) | 04/2024 |
| energielenker, ModbusMeter 5A | 08/2024 |
| [FHEM (fhem.de)](/files/meter-definitions/cfos-meter-fhem.json) | 05/2022 |
| [Gossen Metrawatt EM288x](/files/meter-definitions/gossen_metrawatt_em228x.json) | 04/2023 |
| [Hager ECA/ECR Modbus (experimental)](/files/meter-definitions/hager_eca_ecr.json) | 02/2023 |
| [HomeWizard P1 Meter](https://www.homewizard.com/p1-meter/) | 12/2023 |
| [IAMMETER Energy Meter Modbus](/files/meter-definitions/meter_iammeter_mb.json) | 09/2022 |
| [IME CE4DF3DTxxx](/files/meter-definitions/ime-cont-d4-pd.json) | 12/2022 |
| [IME CE4DF3DTxxx V3](/files/meter-definitions/ime-cont-d4-pd_v3.json) | 04/2023 |
| Janitza UMG 96 RM (und Ã¤hnliche UMG xxx) | 08/2023 |
| [KDK PRO380-Modbus](/files/meter-definitions/meter_kdk_pro380.json) | 05/2022 |
| [k'electric KE 80P](/files/meter-definitions/meter_kelectric_ke-80p_modbus.json) | 05/2022 |
| KLEFR 693-4x | 06/2023 |
| [Lovato DMEDxxx](https://catalogue.lovatoelectric.com/gl_en/Products/Metering-instruments-and-current-transformers/CAP25/pc) | 06/2023 |
| Lovato ED341MID7E | 02/2024 |
| Orno OR-WE-516 | 12/2021 |
| [Orno OR-WE-517](https://orno.pl/de/produkt/1087/3-phasen-stromzaehler-80a-rs-485-anschluss-mehrtarif-3-module-din-th-35mm) | 12/2021 |
| [Phoenix Contact EMpro (HTTP)](https://www.phoenixcontact.com/en-pc/products/energy-monitoring/energy-measuring-devices-and-energy-meters) | 05/2023 |
| [Pilot SPM9513](/files/meter-definitions/pilot-spm9513.json) | 12/2021 |
| [Powerfox](https://powerfox.energy) | 12/2021 |
| [Schneider IEM3255](/files/meter-definitions/meter_schneider_iem3255.json) | 05/2022 |
| Shelly 3EM, 1PM, Shelly Relay, Plus 1PM, Plus 2PM, Plus 2PM K2, Pro 3EM | 12/2021 |
| [Siemens Pac2200](/files/meter-definitions/siemens-pac2200-clp.json) | 04/2022 |
| [SmartPI](/files/meter-definitions/smart_pi_http.json) | 05/2022 |
| SML ZÃ¤hler, diverse Hager EHZ363WA, EasyMeter Q3A / Q3C | 05/2022 |
| SML [Optical read heads](/en/cfos-charging-manager/documentation/optical-reader-sml.htm) | 04/2022 |
| [Socomec, COUNTIS E28](/files/meter-definitions/socomec-countis-e28.json) | 04/2022 |
| [spot-hinta.fi Electricity prices](/files/meter-definitions/spot_hinta_fi.json) | 08/2023 |
| [Tasmota (example for Logarex LK13BE](/files/meter-definitions/tasmota_smartmeter.json) | 04/2022 |
| Tibber Pulse (via SML HTTP meter) | 12/2023 |
| TQ EM210 | 08/2024 |
| [Voltoplus surplus regulator](/files/meter-definitions/voltoplus_http.json) | 01/2024 |
| [Wago 879-30 3000 4PU, 3020 4 PS, 3040 2PU CT, etc.](/files/meter-definitions/wago_879-3020-4ps.json) | 04/2022 |
| YTL DTS 353 und DEM4A | 05/2023 |
| YTL DEM4B | 10/2024 |
| [ZZ4 D513020](https://top-messtechnik.com/Digital-electricity-meter-ZZ4) | 12/2021 |

Controllable battery storage (experimental)
-------------------------------------------

The Snigg Charging Manager can read out the current power and SoC of various battery storage systems. Some models can also be actively controlled using battery charging rules. We are currently testing the following systems:

|  |  |
| --- | --- |
| Fronius Hybrid-Wechselrichter | 04/2023 |
| Huawei Sun2000 | 04/2023 |
| Kostal Plenticore Hybrid | 04/2023 |
| SMA Hybrid / STPxx-3SE-40 | 10/2024 |
| Sungrow Hybrid | 04/2023 |
| Victron Batteriespeicher | 04/2023 |

Controllable heat pumps (experimental)
--------------------------------------

Please get in touch if you own an appliance listed here. We would like to gain more experience with heat pumps.

|  |  |
| --- | --- |
| Vaillant VRC700/720 WÃ¤rmepumpe | 07/2024 |

Supported OCPP 1.6 backends
---------------------------

|  |  |
| --- | --- |
| be.energized | 05/2023 |
| chargecloud | 08/2022 |
| chargeIQ  [Configuration guide](/files/instructions-cfos-charging-manager-with-chargeiq.pdf) | 02/2023 |
| [clever-PV](https://www.clever-pv.com/) | 08/2024 |
| eCarUp | 08/2022 |
| eOperate | 08/2022 |
| eRound | 04/2024 |
| LISY2 | 04/2023 |
| Germancharge | 02/2024 |
| Monta | 08/2022 |
| OLI Move | 06/2023 |
| Parkstrom / Elektra | 05/2023 |
| [PRO.mobility](https://www.pro-mobility.info/) | 07/2025 |
| Spectra Moon | 08/2022 |
| Steve | 08/2022 |
| **Your backend not listed?** [**Contact us.**](#) | |

###### Thank you for testing EVSEs and meters to:

**Adrian A.** | **Alexander B.** | **Andreas M.** | **Andreas S.** | **Axel S.** | **Benedict S.** | **Berger Stromversorungen** | **Bert C.** | **Chris B.** | **Detlef K.** | **Dhidet** | **Elektro KlauÃner** | **energielenker** | **Frank M.** | **Get It Done** | **Guido S.** | **Heiko P.** | **Hendrik J.** | **Horst A.** | **Hymes Energy** | **Jan H.** | **Jarkko H.** | **Jonas D.** | **JÃ¼rgen F.** | **Klaus S.** | **Manuel G.** | **Marco L.** | **Marc-Oliver O.** | **Marco T.** | **Markus K.** | **Martin S.** | **Matthias S.** | **Max H.** | **MaXx** | **Michael S.** | **Miha S.** | **MMS Communication** | **Rainer Z.** | **RenÃ© P.** | **Simon K.** | **Stephan B.** | **Stefan E.** | **Stefan M.** | **Stefan W.** | **Thomas B.** | **Wilfried S.**

Wir haben **#diebestenuserderwelt**:  
Our customers help us a great deal in testing meters and other devices, providing us with important information, suggestions for improvement and, last but not least, finding errors.

Documentation
-------------

[Here you will find instructions and help for Snigg Smart Charger, Snigg Smart Controller and Snigg Charging Manager](/en/cfos-charging-manager/documentation/documentation-links.htm)

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

[Ø§ÙØ¹Ø±Ø¨ÙØ©](/ar/cfos-charging-manager/list-of-supported-devices.htm)

[ÐÐµÐ»Ð°ÑÑÑÐºÐ°Ñ](/be/cfos-charging-manager/list-of-supported-devices.htm)

[ÐÑÐ»Ð³Ð°ÑÐ¸Ñ](/bg/cfos-charging-manager/list-of-supported-devices.htm)

[Äesky](/cs/cfos-charging-manager/list-of-supported-devices.htm)

[Dansk](/da/cfos-charging-manager/list-of-supported-devices.htm)

[Deutsch](/de/cfos-charging-manager/list-of-supported-devices.htm)

[ÎÎ»Î»Î·Î½Î¹ÎºÎ¬](/el/cfos-charging-manager/list-of-supported-devices.htm)

[English](/en/cfos-charging-manager/list-of-supported-devices.htm)

[Castellano](/es/cfos-charging-manager/list-of-supported-devices.htm)

[ÙØ§Ø±Ø³Û](/fa/cfos-charging-manager/list-of-supported-devices.htm)

[Suomi](/fi/cfos-charging-manager/list-of-supported-devices.htm)

[FranÃ§ais](/fr/cfos-charging-manager/list-of-supported-devices.htm)

[××©×¨×××](/he/cfos-charging-manager/list-of-supported-devices.htm)

[à¤¹à¤¿à¤¨à¥à¤¦à¥](/hi/cfos-charging-manager/list-of-supported-devices.htm)

[Magyar](/hu/cfos-charging-manager/list-of-supported-devices.htm)

[Bahasa Indonesia](/id/cfos-charging-manager/list-of-supported-devices.htm)

[Italiano](/it/cfos-charging-manager/list-of-supported-devices.htm)

[æ¥æ¬èª](/ja/cfos-charging-manager/list-of-supported-devices.htm)

[íêµ­ì´](/ko/cfos-charging-manager/list-of-supported-devices.htm)

[Ð¼Ð°ÐºÐµÐ´Ð¾Ð½ÑÐºÐ¸](/mk/cfos-charging-manager/list-of-supported-devices.htm)

[Bahasa Malaysia](/ms-my/cfos-charging-manager/list-of-supported-devices.htm)

[Nederlands](/nl/cfos-charging-manager/list-of-supported-devices.htm)

[Norsk](/no/cfos-charging-manager/list-of-supported-devices.htm)

[Polski](/pl/cfos-charging-manager/list-of-supported-devices.htm)

[PortuguÃªs](/pt/cfos-charging-manager/list-of-supported-devices.htm)

[RomÃ¢nÄ](/ro/cfos-charging-manager/list-of-supported-devices.htm)

[Ð ÑÑÑÐºÐ¸Ð¹](/ru/cfos-charging-manager/list-of-supported-devices.htm)

[SlovenÅ¡Äina](/sl/cfos-charging-manager/list-of-supported-devices.htm)

[Ð¡ÑÐ¿ÑÐºÐ¸](/sr-cyrl-cs/cfos-charging-manager/list-of-supported-devices.htm)

[Svenska](/sv/cfos-charging-manager/list-of-supported-devices.htm)

[à¹à¸à¸¢](/th/cfos-charging-manager/list-of-supported-devices.htm)

[TÃ¼rkÃ§e](/tr/cfos-charging-manager/list-of-supported-devices.htm)

[Ð£ÐºÑÐ°ÑÐ½ÑÑÐºÐ°](/uk/cfos-charging-manager/list-of-supported-devices.htm)

[Tiáº¿ng Viá»t](/vi/cfos-charging-manager/list-of-supported-devices.htm)

[ç®ä½ä¸­æ](/zh-cn/cfos-charging-manager/list-of-supported-devices.htm)

[ç¹é«ä¸­æ](/zh-tw/cfos-charging-manager/list-of-supported-devices.htm)

---

Practice random kindness and senseless acts of beauty

![Snigg eMobility GmbH Logo](/images/cfos-emobility-logo.svg)

Cookies
=======

We use cookies. Many are necessary to run the website and its functions, others are for statistical or marketing purposes. By choosing "Accept essential cookies only" we will respect your privacy and not set cookies that are not necessary for the operation of the site.

Accept all Accept essential cookies only

[Privacy Policy](/en/contact/contact.htm#privacy?hide-cookie-banner=yes)