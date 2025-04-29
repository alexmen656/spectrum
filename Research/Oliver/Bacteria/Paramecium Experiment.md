Our next iteration of the experiment currently looks like this: We will have Paramecium organisms (single celled, but much easier to handle compared to bacteria) inside sealed (or not, we are not sure whether we can afford to have such low pressure) conatainers, of which we will have about 5-10 on the payload. We will look at these under a microscope before and after the flight to analyze how many have survived, and we are currently also considering adding an ESP32-CAM with some sort of microscope extesion to observe 1 of the containers on the inside.
### **Risks**
1. Paramecium are not really built for extreme environmental conditions, like subzero temperatures or vacuum like pressures. This could lead to all of our organisms dying. (This is also a reason why adding a camera would be good, so that we still have some data)
   **Importance:** HIGH
2. Transporting the organisms on a plane could kill them, although I am pretty sure we can figure something out to prevent this.
   **Importance:** MEDIUM
3. We are not sure how well our camera and esp32 will work at such low temperatures, we might have to add additional isolation to them
   **Importance:** MEDIUM/HIGH
4. Low pressure could cause the water to boil before freezing. We could seal the containers to prevent the pressure from changing, but this would also defeat part of our project as it is also observing the survival as pressure changes.
   **Importance:** MEDIUM

### **Alternatives**
1. Instead of Paramecium, we could use something like tardigrades instead, which would likely survive the conditions, and are therefore better suited. However, they are also harder to obtain and handle and if they are too resistant then there is not much to observe
2. We could use a gel or something instead of water, which does not boil and therefore it would be easier to handle the pressure. But this is also harder to handle than water and requires many extra steps

### **The microscope**
As mentioned a few times already, it would be extremely useful to have some way of observing the bacteria mid flight, not just before and after. This is why it would be ideal to have some sort of microscope extension for the ESP32-CAM to observe the organisms.

**1. [Matchboxscope](https://github.com/Matchboxscope/Matchboxscope)**
This is a Project I found on github which uses the esp32-cam to make a small microscope. This seems like a nice option, although I will have to research a bit further. The only problem with it is that it is not designed for fluid containers

### **How to obtain the organisms**
To get the required organisms, we will probably grow the by ourself as we were told it is pretty easy to do. We will take a water sample from a nearby pond, add it to normal water, add some yeast as food for the paramecium and check it under a microscope every couple of days to check whether they are actually growing or not. 
