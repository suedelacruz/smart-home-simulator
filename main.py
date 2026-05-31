from domain.devices.smart_light import SmartLight
from domain.sensors.motion_sensor import MotionSensor

from domain.automation.automation_rule import AutomationRule

from services.automation_engine import AutomationEngine
from services.notification_service import NotificationService


print("=== SMART HOME SIMULATOR ===\n")


hallway_light = SmartLight(
    "L001",
    "Hallway Light",
    "Hallway"
)


notification_service = NotificationService()


def turn_on_hallway_light():

    hallway_light.turn_on()

    print(
        "[ACTION] Hallway light turned ON"
    )

    notification_service.send_notification(
        "Motion detected in hallway"
    )


engine = AutomationEngine()

motion_rule = AutomationRule(
    "motion_detected",
    turn_on_hallway_light
)

engine.add_rule(
    motion_rule
)


motion_sensor = MotionSensor(
    "MS001",
    "Hallway Motion Sensor",
    "Hallway"
)

motion_sensor.add_observer(
    engine
)


print("Simulating motion detection...\n")

motion_sensor.detect()


print("\nDevice Status:")

print(
    hallway_light.get_status()
)

print(
    "\nSimulation completed."
)