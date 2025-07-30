# Frequently asked questions

ï»¿ Snigg eMobility - Snigg Charging Manager - Frequently asked questions

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

# Frequently asked questions

##### Does the Snigg Charging Manager also support the integration of a solar system / photovoltaics?

Yes, we support the integration of numerous inverters and battery storage systems. There are charging rules for [PV surplus charging](https://www.cfos-emobility.de/en/cfos-charging-manager/documentation/surplus-charging.htm). Our "Solar" wallboxes can be switched between single-phase and three-phase charging and the Snigg Charging Manager supports this with automatic phase [switching](https://www.cfos-emobility.de/en/cfos-charging-manager/documentation/phase-switching.htm). You can also charge with PV surplus with our Snigg Power Brain wallboxes without phase switching. In terms of solar / photovoltaics, we probably have the most comprehensive software support on the market (as of the end of 2023).

##### I have electric cars that charge 1- or 2-phase. What do I have to consider?

The Snigg Snigg Smart Controller can charge electric cars in 1-, 2- and 3-phase mode. However, your energy supplier and the VDE stipulate that all phases must be loaded as evenly as possible. The power of individual phases may not differ from the others by more than 4.6 kW. If you have several cars that do not use 3-phase charging, have your electrician connect the wallboxes in such a way that all phases are rotated compared to other wallboxes (phase rotation). You can then configure the phase rotation in the Snigg Charging Manager. The Snigg Charging Manager then knows on which phases the power is being drawn and can take this into account accordingly.

##### What is the power consumption of the Snigg Snigg Smart Charger?

In standby and with a car plugged in, it consumes less than 1.5W. While a car is being charged, EVSE incl. relay and contactor need approx. 8W.

##### What wiring options are available?

Of course, you must have the Snigg Snigg Smart Controller supplied with three-phase current by an electrician. In addition, you can log the EVSE into your home network via WLAN or dial into your hotspot and operate it via a web interface. You are then ready to go  
  
We recommend that all Snigg Snigg Smart Controllers be connected to your WLAN. This will allow the Charging Manager to communicate with the "slaves" via your home network. Extra cabling with twisted pair wires is only necessary if you want to connect additional Modbus RTU devices  
  
WLAN is sufficient if your Snigg Snigg Smart Charger is within range of your WLAN router or an access point. You can then reach all devices (e.g. other wallboxes via WLAN or network cabling) that can be addressed via IP in your home network. Only if you want to address additional devices that require cabling via RS-485 do you need to lay an additional twisted two-wire connection. See the list of devices supported by us.  
  
Thanks to the RS 485 interface, you can also control the Snigg Snigg Smart Chargeres via two-wire / Modbus RTU.

##### Does the Snigg Charging Manager have to be configured before the first operation?

If you operate a single Snigg Snigg Smart Charger, it will charge at 16A (11kW) or 32A (22kW) without further configuration, depending on the model. Unless you want to use additional capabilities, you do not need to configure any Charging Manager options. If you want to operate several Snigg Snigg Smart Chargers and/or third-party EVSEs on one connection, you will need to configure the Snigg Charging Manager if simultaneous charging on all EVSEs will overbook your house connection power.

##### How can I operate several Snigg Snigg Smart Chargers at the same time?

You can simply install 2 or more Snigg Snigg Smart Chargers. One is then the load manager, i.e. master (the Snigg Charging Manager is already integrated in the Snigg Snigg Smart Controller) and the other(s) are "slaves". Then set e.g. 11kW or more as the house connection power and the power is dynamically divided depending on whether 1 or 2 cars are charging. I.e. as long as there are not really several cars charging or they are charging on different phases, the charging car receives the full power.  
You can also connect an intermediate meter that measures the power consumption of your house (without EVSEs). This way, you could make the entire house connection power available for charging when it is not currently needed in the house.

##### Is there an app for Snigg Snigg Smart Controller or the Snigg Charging Manager?

Yes, see [App Download and Functions.](/en/cfos-charging-manager/documentation/app-functions.htm)

##### Which EVSEs from other manufacturers can I control using the Charging Manager / Snigg Snigg Smart Controller as part of load management?

In the [description of the Snigg Charging Manager](/en/cfos-charging-manager/cfos-charging-manager.htm) (integrated in the Snigg Snigg Smart Controller or available as a software solution for Windows and Raspberry Pi), you will find a (constantly expanding) list of currently supported EVSEs. In addition, all EVSEs that have sufficient OCPP 1.6 functionality are supported.

##### How can I manually set the maximum charge current?

The Snigg Snigg Smart Controller has a web interface that allows you to enable charging and set the maximum charge current. You can access the Snigg Snigg Smart Controller's hotspot from your computer and cell phone using your browser. Alternatively, you can also connect the Snigg Snigg Smart Controller to your home network via WLAN and then access the Web interface from your home network

##### Can the charging current of the Snigg Snigg Smart Charger be (virtually) continuously adjusted?

Yes, you can set the maximum charging power in mA in the wallbox settings. The maximum charging current is then signalled to the car in approx. 0.1 A increments. You therefore have full control. When load management is activated, the Charging Manager determines the current available to the wallbox every few seconds.

##### Is there any way to wake up a "sleeping" car?

Some electric cars are put into a standby mode after some time without charging. Example: the car is connected to the EVSE, but charging is not enabled due to a charging rule. Later, when the charging rule is fulfilled and the car is in standby mode, charging does not start by itself.  
  
In principle, the Snigg Snigg Smart Charger can wake up cars from standby mode. We are currently collecting empirical data on this. If you would like to test this function, please contact us!  
  
You can test whether a car is "awake" in standby mode if you first deactivate "Charging" under the menu item "Snigg Snigg Smart Controller Configuration" and deactivate the EVSE, i.e. switch off both switches. Now wait 30 seconds and switch both back on.  
  
Does the car wake up?  
  
Putting the car into standby mode can probably be done by setting the charge current to **0mA** and waiting until the car is in standby mode, then setting it back to **16A**.  
We are very interested in your test results!

##### Why is an Internet connection necessary?

An Internet connection is required so that the Snigg Snigg Smart Chargeres can supply themselves with the time. Once they are logged into your home WLAN, you can access them conveniently via browser. Otherwise, you would always have to log in to the EVSE's respective hotspot to use the Web interface  
  
An Internet connection is required for the software updates that we regularly offer for download.

##### How is the web interface implemented?

The Web interface of Snigg Snigg Smart Controller is written in HTML and Javascript. Additionally, we use Bootstrap. The display should work well on both desktop screens and cell phones. A reasonably modern web browser is required

##### Do I need a meter at all for load management?

**No**. If you do not install a meter at all, the Snigg Charging Manager makes default assumptions: The existing power allocated for charging cars is then simply divided by the number of cars currently charging. It is then assumed that each car always consumes the maximum power that has just been allocated. The use of the phases is adjustable here, but fixed.  
For single-phase charging cars, several wallboxes should always be installed out of phase and this phase rotation should be configured accordingly in the Snigg Charging Manager. The Charging Manager can then, for example, provide 16 A each to two cars charging simultaneously with a total output of 11 kW (3 x 16 A).

##### I want to measure currents over 80A. How do I use a transformer meter?

The Snigg Charging Manager can handle various meters, including transformer meters. We recommend the Lovato DME 330, which is supplied with foldable 200A transformer coils that are even equipped with a 2m supply cable insulated for 700V. You can set the transformer factor for a transformer meter in the Snigg Charging Manager.

##### What is secure communication?

The Snigg Snigg Smart Controller supports secure SSL encryption for OCPP, the web interface and the HTTP API. Additionally, you can import SSL certificates to authenticate your communication partner. This will prevent anyone from misusing your EVSE to modify data (e.g. charging currents)  
Software updates from Snigg Snigg Smart Controller are also secure. The corresponding firmware is digitally signed by us. This means that a firmware update can only be performed with authentic firmware

##### Can I use the Snigg Snigg Smart Charger to control charging currents via an HTTP API? If so, in which steps?

Yes. The Snigg Snigg Smart Controller has a [Modbus RTU and TCP interface](https://www.cfos.de/de/cfos-power-brain/modbus-registers.htm). You control the EVSE by setting the corresponding Modbus registers. If you do not have Modbus support in your automation software, you can also read and set the Modbus registers through the HTTP API. Here you will find a [description of the HTTP API](https://www.cfos.de/de/cfos-power-brain/http-api.htm). The charging current is specified in 0.1A steps. Since the Snigg Snigg Smart Controller has WLAN, you do not need any additional network cabling.

##### What is OCPP?

OCPP is a standard protocol specially developed for EVSEs. With OCPP a world opens up: You can use OCPP for example

* Make the status of your EVSE visible to yourself and others on the Internet. So you can see if it is currently occupied, if someone is loading, etc.
* Connect your EVSE to backends for billing purposes. This allows you to integrate your EVSE into the networks of large charging station operators and earn money with your EVSE and/or conveniently bill it if several people use it
* Integrate your EVSE into a load management system. Thanks to Snigg Charging Manager, we offer a load management system that can also be used by EVSEs without OCPP. However, most other providers require OCPP.

The Snigg Snigg Smart Charger is one of the most affordable wallboxes with a sophisticated and comprehensive OCPP 1.6 implementation, including various professional features.

##### Does the Snigg Snigg Smart Controller also run with OpenWB?

As of November 2020, we are not aware of any support for the Snigg Snigg Smart Controller in OpenWB. However, since the Snigg Snigg Smart Controller can be conveniently controlled remotely via an HTTP API, we assume that support will come soon. Here are links to our Modbus and HTTP API documentation:  
[Documentation Modbus register](https://www.cfos.de/de/cfos-power-brain/modbus-registers.htm)  
[Documentation HTTP API](https://www.cfos.de/de/cfos-power-brain/http-api.htm)

##### How can I use the RS485 interface of the Snigg Snigg Smart Controller?

The following options are available here:

* You can connect other Modbus devices supported by us to the interface and read and remotely control them
* You can remote control the Snigg Snigg Smart Controller via Modbus RTU. However, this is only recommended if there is appropriate wiring anyway. Otherwise, we recommend Modbus TCP, HTTP or OCPP via WLAN

##### How do I set up a Snigg Snigg Smart Charger in conjunction with another Snigg Snigg Smart Charger or a EVSE from another manufacturer?

To do this, you must use the Charging Manager. In the web interface, click on "Configuration" in the menu. First set the available total power for all EVSEes under "Max. Total Power", set the available total power for all EVSE. Under "Power Reserve" you should set a reserve that is not touched so that the fuse does not blow in the event of an overload. If you have a private household, we recommend 2500W as a reserve. Under "Max Total EVSE Power" you can enter the maximum power for which the supply line to your EVSEes is designed, if this is the limiting factor. Otherwise enter 0 there.  
  
By default, an EVSE is set up, namely the Snigg Snigg Smart Charger with address "localhost". With localhost, the Charging Manager addresses its own devices. If you now add another wallbox, e.g. a Snigg Power Brain wallbox, you must enter the IP address that it has in your network as the address, e.g. **192.168.2.102:4701**. If the wallbox to be connected is addressed via RS-485 interface, enter COM1,baudrate,8,n,1 here.  
  
The Charging Manager distributes the available charging power among the configured and currently charging EVSEs (load management).

##### Which connection to other devices is better? IP (house network via the router / internet) or Modbus RTU (two-wire)?

The Snigg Charging Manager polls all configured devices for their status every few seconds. Since several devices can be addressed simultaneously via IP and only all devices one after the other with a two-wire connection, we recommend IP connections. Then the Charging Manager can react more quickly

##### What happens if the connection to a device fails?

In this case, the Charging Manager assumes that the wallbox is drawing the last reported power and reports errors in the overview. It is OK if the connection is interrupted for a few seconds in between. However, you should otherwise ensure stable and reliable connections. In Modbus mode, the wallbox has a fail-safe function, i.e. if no more Modbus communication is received for an adjustable number of seconds, the wallbox switches off automatically or switches to an adjustable minimum charging current. With OCPP, you can also achieve this behaviour using "Charging Profiles". If a wallbox is unavailable for the Snigg Charging Manager for longer than 3 minutes, its fail-safe current is assumed as charging power if a car was plugged in. This power is counted as "fault current" and deducted from the charging power for other cars.

##### Is it possible to hang the Snigg Snigg Smart Charger on the house facade?

The Snigg Snigg Smart Charger has an IP55 housing. As long as you also ensure that it does not rain into the charging cable plug (it has a protective cap), you should be able to install the wallbox outdoors without any problems (please avoid direct sunlight).

##### Which languages does the user interface support?

German and English are currently supported. Other languages could be added if required.

##### Is there a key switch for access restriction?

Access restriction works via the web interface, via RFID and via the app. However, you can also have an electrician retrofit a key switch with simple steps. The CP signal, i.e. the orange wire, must then be routed via the key switch. When the switch is open, the Snigg Snigg Smart Controller does not notice that a car is plugged in and therefore does not release the charge. The warranty remains intact even with such a modification.

##### What wire cross-sections must be used to connect the Snigg Snigg Smart Charger 11kW or 22kW?

The wallbox may only be installed by a qualified specialist who must know which wire cross-sections and fuses are required. This depends, among other things, on the cable length. In contrast to cookers, instantaneous water heaters and other household appliances, a wallbox is a continuous consumer and is therefore subject to stricter safety requirements. Therefore, please do not install it yourself, but always consult a specialist.

##### I have two (or more) EVSEs. Can I connect them in series on one power connection, i.e. go from one to the other with the power supply?

No. The EVSEs must be wired in a star configuration starting from a distributor and each must be protected with a type A RCD and circuit breaker. The DC residual current sensor built into the Snigg Snigg Smart Charger reacts at 6mA residual current (direct current). If you were to connect several EVSEs in series, they could each deliver less than 6mA residual current but more than 6mA in total. This would then not be detected. Therefore, this series connection is not permitted.

##### Can I attach a key switch to the EVSE?

You can connect a potential-free switch (e.g. key switch or ripple control receiver) to one of the two S0 inputs on the Snigg Snigg Smart Charger, e.g. to [S0-2](/en/cfos-power-brain/modbus-meter-s0-meter.htm), as shown in our [documentation on S0 meters](/en/cfos-power-brain/modbus-meter-s0-meter.htm). You can then query this input using [charging rules](/en/cfos-charging-manager/documentation/charging-rules.htm) and thus influence the charging. Some network operators / energy suppliers require that the charging power of the wallbox(es) can be reduced or set to 0 by means of ripple control receivers if necessary. In order to fulfil this requirement for grid-serving control, you can enter a formula as follows in the Charging Manager settings for the parameter "Max. total power (W)" instead of a fixed value: PB.input2 ? 25000 : 0  
If the S0-2 input is set (switch closed), the Charging Manager takes 25 kW as the house connection power, otherwise 0 kW. You can adjust the specific power values according to your application.

##### How can an LED be connected as a status indicator?

Snigg Power Brain controllers from Rev. 1.1 (recognisable by the angled pin header) have a 330 Ohm resistor at the LED output (3.3V). Any LED designed for a current above 5 mA can be connected there. Snigg Power Brain controllers of Rev. 1.0 (the pin header is not accessible without opening the Power Brain housing) do not have a resistor. Any LED with the appropriate series resistor can be connected to the LED output (3.3V) here

##### How can the energy consumed be read out via the user interface?

The tiles on the start page show the consumed kWh of the EVSE, as well as the imported and exported energy of the meters. In addition, you can download a transaction log under "Configuration" in which all charging processes are logged with kWh. If you set up individual users, they can also download their transaction log. The transaction logs are CSV files that you can process in Excel, for example.

##### How can the Snigg Snigg Smart Charger or the Snigg Charging Manager be reset to the factory settings?

Under "System Configuration" -> Files there is a button for resetting the Snigg Charging Manager configuration or the entire system.

##### What should be done if the Snigg Snigg Smart Charger is no longer displayed on the network?

If the Snigg Snigg Smart Charger has lost the connection to the WLAN, you can first restart your router or access point. If this does not help, you can disconnect the EVSE from the power supply for a few seconds. After the restart, it should log back into the WLAN. If this does not happen after a few minutes, the Snigg Snigg Smart Charger will automatically start its own Wi-Fi access point so that you can use it to connect to the EVSE and check the configuration.

##### How can I reset the S0 meter of the Snigg Snigg Smart Controller?

Under "Configuration" -> "Modbus Test" you can describe a register with a desired value for the kWh of the meter. The address of the meter is localhost: **4702** for S0 meter 1 or **localhost:4703** for S0 meter 2. The slave Id is **2** for S0 meter 1 and **3** for S0 meter 2. Enter **8058** as the register, type "64 bit qword", number **1**, value to be written the desired meter reading in Wh. Then click on "Write".

##### How should I install my meters for load management?

After you have set the maximum house connection power in the Charging Manager settings, you can measure in two ways

* You install one or more consumption meters (for consumption without EVSE) and generation meters (or read your solar inverters). The Charging Manager then calculates the power available for charging the electric cars as the house connection power minus the consumption meter plus the generation meter. If you do not install a meter, the Charging Manager will divide the house connection power among the charging EVSEs. If you do not want to measure the house consumption, you can configure the house connection power lower according to the maximum house consumption (static)
* You install a grid reference meter. This measures the power that flows through your house connection, including all consumers, generators and EVSEs. However, you must then install at least one meter that measures the consumption of the EVSE. The load management of the Charging Manager then calculates the charging power for the electric cars as the house connection power minus the difference between the mains supply and the EVSE. In other words, it subtracts the EVSE power from the grid supply to determine how much energy is consumed or generated elsewhere. Typically, a meter is assigned to each EVSE. However, you can also connect all EVSE to one meter and thus possibly save meters if you do not need individual metering for the EVSE (for billing purposes). If you have a generation source (PV system), you need a bidirectional meter as a grid reference meter to be able to distinguish between purchase and feed-in

You tell the Charging Manager which function the installed meters have by specifying the role of the meter in the meter configuration.

##### Do I need a calibrated or MID certified meter for billing purposes (with the tax office)?

In Germany, all meters used for billing purposes must be "calibrated". This calibration is carried out in the EU by means of MID certification. A MID-compliant meter is therefore suitable for billing purposes. It may be necessary to install this outside the wallbox. You may relocate the MID meter installed in the Snigg Snigg Smart Charger to an external housing without invalidating the warranty.

##### Does the EVSE have to be serviced or checked after a certain period of time?

There is no special obligation to do this in a private environment. In a commercial environment, you must have the EVSE checked annually by an electrician.

##### How do I install a software or firmware update?

Under "Configuration" -> Firmware update, you can check for new versions and install them by clicking on "Update now". The EVSE will then restart.

##### What is the load capacity of the 12V at the S0 terminal?

The 12V of the S0 terminal may be loaded with a maximum of 25 mA. They are actually only used to supply a voltage for possible S0 meters or switching contacts. For each S0 meter and contact that you supply with this 12V, you still have to subtract 5 mA each. This means that only 20 mA or 15 mA are available.

##### What does the flashing of the LED mean?

The LED of the Snigg Snigg Smart Controller flashes in a pattern that repeats every 3 seconds.  represents an illuminated LED and  a non-illuminated LED in the following explanation.

|  |  |
| --- | --- |
|  | Standby (LED off) |
|  | VehicleDetected (LED flashes briefly every 3 seconds) |
|  | Charging (LED flashes: 1.5 seconds on, 1.5 seconds off) |
|  | ChargingVentilation (LED flashes: 1 second on, 2 seconds off) |
|  | NoPower (LED flashes four times) |
|  | Error (LED flashes twice with a pulse of 2) |

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

[Ø§ÙØ¹Ø±Ø¨ÙØ©](/ar/cfos-charging-manager/frequently-asked-questions.htm)

[ÐÐµÐ»Ð°ÑÑÑÐºÐ°Ñ](/be/cfos-charging-manager/frequently-asked-questions.htm)

[ÐÑÐ»Ð³Ð°ÑÐ¸Ñ](/bg/cfos-charging-manager/frequently-asked-questions.htm)

[Äesky](/cs/cfos-charging-manager/frequently-asked-questions.htm)

[Dansk](/da/cfos-charging-manager/frequently-asked-questions.htm)

[Deutsch](/de/cfos-charging-manager/frequently-asked-questions.htm)

[ÎÎ»Î»Î·Î½Î¹ÎºÎ¬](/el/cfos-charging-manager/frequently-asked-questions.htm)

[English](/en/cfos-charging-manager/frequently-asked-questions.htm)

[Castellano](/es/cfos-charging-manager/frequently-asked-questions.htm)

[ÙØ§Ø±Ø³Û](/fa/cfos-charging-manager/frequently-asked-questions.htm)

[Suomi](/fi/cfos-charging-manager/frequently-asked-questions.htm)

[FranÃ§ais](/fr/cfos-charging-manager/frequently-asked-questions.htm)

[××©×¨×××](/he/cfos-charging-manager/frequently-asked-questions.htm)

[à¤¹à¤¿à¤¨à¥à¤¦à¥](/hi/cfos-charging-manager/frequently-asked-questions.htm)

[Magyar](/hu/cfos-charging-manager/frequently-asked-questions.htm)

[Bahasa Indonesia](/id/cfos-charging-manager/frequently-asked-questions.htm)

[Italiano](/it/cfos-charging-manager/frequently-asked-questions.htm)

[æ¥æ¬èª](/ja/cfos-charging-manager/frequently-asked-questions.htm)

[íêµ­ì´](/ko/cfos-charging-manager/frequently-asked-questions.htm)

[Ð¼Ð°ÐºÐµÐ´Ð¾Ð½ÑÐºÐ¸](/mk/cfos-charging-manager/frequently-asked-questions.htm)

[Bahasa Malaysia](/ms-my/cfos-charging-manager/frequently-asked-questions.htm)

[Nederlands](/nl/cfos-charging-manager/frequently-asked-questions.htm)

[Norsk](/no/cfos-charging-manager/frequently-asked-questions.htm)

[Polski](/pl/cfos-charging-manager/frequently-asked-questions.htm)

[PortuguÃªs](/pt/cfos-charging-manager/frequently-asked-questions.htm)

[RomÃ¢nÄ](/ro/cfos-charging-manager/frequently-asked-questions.htm)

[Ð ÑÑÑÐºÐ¸Ð¹](/ru/cfos-charging-manager/frequently-asked-questions.htm)

[SlovenÅ¡Äina](/sl/cfos-charging-manager/frequently-asked-questions.htm)

[Ð¡ÑÐ¿ÑÐºÐ¸](/sr-cyrl-cs/cfos-charging-manager/frequently-asked-questions.htm)

[Svenska](/sv/cfos-charging-manager/frequently-asked-questions.htm)

[à¹à¸à¸¢](/th/cfos-charging-manager/frequently-asked-questions.htm)

[TÃ¼rkÃ§e](/tr/cfos-charging-manager/frequently-asked-questions.htm)

[Ð£ÐºÑÐ°ÑÐ½ÑÑÐºÐ°](/uk/cfos-charging-manager/frequently-asked-questions.htm)

[Tiáº¿ng Viá»t](/vi/cfos-charging-manager/frequently-asked-questions.htm)

[ç®ä½ä¸­æ](/zh-cn/cfos-charging-manager/frequently-asked-questions.htm)

[ç¹é«ä¸­æ](/zh-tw/cfos-charging-manager/frequently-asked-questions.htm)

---

Practice random kindness and senseless acts of beauty

![Snigg eMobility GmbH Logo](/images/cfos-emobility-logo.svg)

# Cookies

We use cookies. Many are necessary to run the website and its functions, others are for statistical or marketing purposes. By choosing "Accept essential cookies only" we will respect your privacy and not set cookies that are not necessary for the operation of the site.

Accept all Accept essential cookies only

[Privacy Policy](/en/contact/contact.htm#privacy?hide-cookie-banner=yes)