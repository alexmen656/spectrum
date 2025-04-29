**Biosafety Level:** 1
**Cost:** TBA
**Best suited Variable:** Pressure
**Access:** TBA

Widely researched and commonly used bacteria for various biological Experiments. Survives temperatures up to 70°C, and below 4°C their growth is significantly slowed. They do not die from freezing. They start dying below 10mbar, which is ideal in our case as the low pressure in the high altitude wont immediately kill them. They are very Sensitive to UV radiation, but the styrofoam box should be enough to shield them. Nevertheless, we should consider having a UV sensor near the colony to observe the data and be able to identif causes of mass deaths of e coli.

#### **Stats**
- **Temperature:** Do not die, growth slows rapidly
- **Pressure:** Could die at high altitude from pressure, but it should not cause mass deaths
- **UV Radiation:** Extremely sensitive, should be shielded by box
- **Cosmic Radiation:** Not a concern, mutations in worst case szenarios
- **Movement/shock and vibrations:** Only sudden impacts, like when landing, can have a meaningful impact. Ideally we should have shock absorbers of some sort so the agar and bacteria are not damaged

#### **Predicted Observation**
| **Altitude** | Temperature | Pressure | Observation                                            | Survival   | Notes |
| ------------ | ----------- | -------- | ------------------------------------------------------ | ---------- | ----- |
| 0ft (start)  | 20°C        | 1013mbar | Agar, inside Styrofoam box                             | cca. 100%  |       |
| 5.000ft      | 5-15°C      | 843mbar  | no meaningful effect                                   | cca. 100%  |       |
| 10.000ft     | 0-10°C      | 700mbar  | maybe slight damage, not meaningful                    | cca. 99%   |       |
| 15.000ft     | -5-5°C      | 570mbar  | Cold stress increases                                  | cca. 99%   |       |
| 20.000ft     | -15°C       | 465mbar  | Pressure and temperature start killing bacteria slowly | cca. 96%   |       |
| 25.000ft     | -25°C       | 370mbar  | Large deaths start happening                           | cca. 85%   |       |
| 30.000ft     | -35°C       | 300mbar  | Freezing starts taking out large quantities            | cca. 75%   |       |
| 35.000ft     | -40°C       | 240mbar  | membrane disruption and ice crystal damage             | cca. 65%   |       |
| 40.000ft     | -50°C       | 190mbar  |                                                        | cca. 55%   |       |
| 45.000ft     | -55°C       | 140mbar  |                                                        | cca. 45%   |       |
| 50.000ft     | -60°C       | 100mbar  |                                                        | cca. 35%   |       |
| 55.000ft     | -60°C       | 75 mbar  |                                                        | cca. 25%   |       |
| 60.000ft     | -60°C       | 50 mbar  |                                                        | cca. 15%   |       |
| 65.000ft     | -60°C       | 35 mbar  |                                                        | cca. 10%   |       |
| 70.000ft     | -60°C       | 25 mbar  |                                                        | cca. 5%    |       |
| 75.000ft     | -60°C       | 18 mbar  |                                                        | cca. 4%    |       |
| 80.000ft     | -60°C       | 12 mbar  |                                                        | cca. 2%    |       |
| 85.000ft     | -65°C       | 8 mbar   |                                                        | cca. 1%    |       |
| 90.000ft     | -65°C       | 5 mbar   |                                                        | cca. 0.5%  |       |
| 95.000ft     | -65°C       | 3 mbar   |                                                        | cca. 0.1%  |       |
| 100.000ft    | -65°C       | 1-2 mbar |                                                        | cca. 0.01% |       |

#### **Stabilizing variables**
To reduce the extreme lethality at the higher altitudes, we could try to stabilize some parameters, like temperature or pressure. While stabilizing pressure would help, the low temperatures would still prevent them from reproducing. stabilizing temperature could massively benefit the bacteria, and possibly even allow them to reproduce, making reproduction and possibly evolution and natural selection observable. This is why **stabilizing temperature** might be the best option.

#### **Experiment**
The Setup would consist of a red LED lamp above a petri dish containing the bacteria. below the petri dish, a light sensor (and possibly also espCam) will be detecting the intensity of the light and thus be able to identify the growth Rate of the colony. However, the growth rate will likely stop early on, which is why we need some other way to measure the current active population. A heater will somehow be placed around the petri dish to stabilize its temperature, and the whole setup will be isolated to prevent heat loss. One or more small holes will enable slight gas exchange between inside and outside, making the pressure an observable variable. **TBA** way to measure population size