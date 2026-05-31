from domain.devices.smart_light import SmartLight
from domain.devices.smart_thermostat import SmartThermostat
from domain.devices.smart_door_lock import SmartDoorLock
from domain.devices.security_camera import SecurityCamera
from domain.devices.smart_speaker import SmartSpeaker


class DeviceFactory:

    @staticmethod
    def create_device(
        device_type,
        device_id,
        name,
        room
    ):

        if device_type == "LIGHT":
            return SmartLight(device_id, name, room)

        elif device_type == "THERMOSTAT":
            return SmartThermostat(
                device_id,
                name,
                room
            )

        elif device_type == "DOOR_LOCK":
            return SmartDoorLock(
                device_id,
                name,
                room
            )

        elif device_type == "CAMERA":
            return SecurityCamera(
                device_id,
                name,
                room
            )

        elif device_type == "SPEAKER":
            return SmartSpeaker(
                device_id,
                name,
                room
            )

        raise ValueError(
            f"Unknown device type: {device_type}"
        )
    

    