import unittest

from domain.devices.smart_light import SmartLight


class TestSmartHome(unittest.TestCase):

    def test_light_turn_on(self):

        light = SmartLight(
            "L1",
            "Kitchen Light",
            "Kitchen"
        )

        light.turn_on()

        self.assertTrue(
            light.power_state
        )

    def test_light_turn_off(self):

        light = SmartLight(
            "L1",
            "Kitchen Light",
            "Kitchen"
        )

        light.turn_off()

        self.assertFalse(
            light.power_state
        )

    def test_factory_creates_light(self):

        from factories.device_factory import DeviceFactory

        device = DeviceFactory.create_device(
            "LIGHT",
            "L1",
            "Kitchen Light",
            "Kitchen"
        )

        self.assertEqual(
            device.__class__.__name__,
            "SmartLight"
        )

    def test_owner_role(self):

        from domain.users.owner import Owner

        owner = Owner(
            "U1",
            "Sue"
        )

        self.assertEqual(
            owner.get_role(),
            "Owner"
        )

    def test_guest_role(self):

        from domain.users.guest import Guest

        guest = Guest(
            "U2",
            "John"
        )

        self.assertEqual(
            guest.get_role(),
            "Guest"
        )

    def test_room_add_device(self):

        from domain.house.room import Room

        room = Room("Kitchen")

        light = SmartLight(
            "L1",
            "Kitchen Light",
            "Kitchen"
        )

        room.add_device(light)

        self.assertEqual(
            len(room.devices),
            1
        )

    def test_house_add_room(self):

        from domain.house.house import House
        from domain.house.room import Room

        house = House()

        room = Room("Kitchen")

        house.add_room(room)

        self.assertEqual(
            len(house.rooms),
            1
        )

    def test_logger_singleton(self):

        from services.logger import Logger

        logger1 = Logger()

        logger2 = Logger()

        self.assertTrue(
            logger1 is logger2
        )


if __name__ == "__main__":
    unittest.main()
