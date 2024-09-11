import asyncio

from bleak import BleakClient, BleakScanner

DEVICE_NAME_PREFIX = "RallyTally"


class BleConnections:
    def __init__(self):
        pass

    async def scan_and_connect(self):
        scanner = BleakScanner()

        while True:
            print("Scanning for devices...")
            devices = await scanner.discover(timeout=5)

            if not devices:
                print("No devices found. Retrying...")
                continue

            print("Discovered devices:")
            for device in devices:
                print(f" - {device.name} ({device.address})")

            for device in devices:
                if device.name and device.name.startswith(DEVICE_NAME_PREFIX):
                    print(f"Found target device: {device.name} ({device.address})")


if __name__ == "__main__":
    ble_connections = BleConnections()
    asyncio.run(ble_connections.scan_and_connect())
