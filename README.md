# Fire-Warning-And-Extinguishing-IoT-System
The Smart Fire Warning and Extinguishing IoT System is a comprehensive project designed to detect and respond to fire hazards using a combination of hardware and software components. The system leverages Arduino as the central processing unit, alongside various sensors and actuators, to detect fire-related threats and take automated actions to mitigate the danger.

### Key Technologies and Components:
1. Arduino:
- The core microcontroller used to manage the sensors and actuators.
- Integrated with temperature and smoke sensors to monitor environmental conditions.
- Controls devices such as buzzers and water pumps to respond to fire threats.

2. YOLOv8:
- An advanced object detection model used for image recognition.
- Detects flames from security camera footage, enhancing the accuracy of fire detection.

3. ThingSpeak:
- A cloud platform for the Internet of Things that allows data to be stored, analyzed, and visualized.
- Integrated with Arduino to upload sensor data, enabling remote monitoring and triggering of alerts or actions.

4. Python:
- Used for the software components that handle image recognition and cloud communication.
- Python scripts run the YOLOv8 model to detect flames and interact with the ThingSpeak API for data management.

5. Code:
- Arduino code is written to handle sensor data acquisition and control the actuators (buzzer, pump) based on sensor readings.
- Python code handles image processing using YOLOv8 and updates the system status on ThingSpeak.

### Project Directions and Capabilities:
- Fire Detection: Combines data from temperature and smoke sensors with visual flame detection using YOLOv8 to provide a robust fire detection mechanism.
- Automated Response: When a fire is detected, the system automatically sounds an alarm and activates a water pump to extinguish the fire.
- Remote Monitoring and Control: The system sends real-time data to ThingSpeak, which can be monitored through the Blynk app, allowing users to take manual control if necessary.

The project represents an integration of IoT and AI technologies to enhance fire safety, providing both automated and remote-controlled solutions to manage fire hazards effectively. 

## Contact us
Contact me via email: dangkimthanh281003@gmail.com
