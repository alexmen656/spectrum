### **SYTO-9 + propidium iodide:**
SYTO-9 is often used with propidium iodide (PI) in LIVE/DEAD staining. The SYTO-9 stains all bacteria, live and dead, green (emits green fluorescent light when excited with blue light) and therefore shows where the bacteria are, how many there are, etc. PI only stains bacteria with a damaged cell membrane, which essentially means all dead bacteria. So, when you put this together, the alive bacteria will be green, while the dead ones will be red. The best excitation wavelenght here would be around 488nm, which is a cyan/aqua colored light. Using an ESP32-CAM module, we will be able to see how many % of bacteria are roghly still alive. If we pass it through our script, we will get a graph of the bacteria population over time. Also, if the bacteria is only damaged, we can see it glowing in a yellow/orange color as the PI cannot enter the cell in amounts that suffice to displace all syto9.
#### **Concerns:**
###### 1. **Low Pressure:**
   Both SYTO-9 and PI should work in low pressure environments, so this should not be a major concern
###### 2. **Low Temperature:**
   It will not damage the dyes directly, but the cells might get too rigid for the dyes to get inside of them. this is also one reason why we will probably have a heater inside the bacteria chamber as otherwise many aspects could fail
###### 3. **Photobleaching:**
   Especially SYTO-9 is prone to photobleaching, and would start losing its fluorescence when we were to shine light at it for 2 hours straight. However, we can resolve this issue by only turning the LED on when making an image (1-2mins off, the 1min on, take a picture, repeat) and since the dyes dont respond to change in the cell strcuture immediately anyways, there is no point in making more images
###### 4. **Cost:**
   Syto-9 can get extremely expensive. Researching alternatives currently
###### 5. **Toxicity:**
   Both dyes are non-toxic to humans and bacteria
###### 6. **Airline reguations:**
   Both dyes are considered safe to transport and do not require any extra licenses

#### **Statistics summary:**
**Excitation Wavelenght:** 488nm
**Emission Wavelenght:** 498nm/615nm
**Pressure:** Any
**Temperature:** Any
**Concerns:** Possibly [[pigments#3. **Photobleaching **|Photobleaching]]
**Resolved Concerns?:** Yes
**Setup Cost:** Syto 9 is very expensive, PI is manageable

### **Methylene Blue*** 
Methylene Blue