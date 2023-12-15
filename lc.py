import pygatt

UUID25 = "08590f7e-db05-467e-8757-72f6faeb13d4"


class LionChief:
    def __init__(self, mac):
        if not mac:
            raise "LionChief constructor needs mac address"

        self._adapter = pygatt.GATTToolBackend()
        self._adapter.start()
        self._device = self._adapter.connect(mac)

    def _send_cmd(self, values):
        checksum = 256
        for v in values:
            checksum -= v
        while checksum < 0:
            checksum += 256
        values.insert(0, 0)
        values.append(checksum)
        self._device.char_write(UUID25, bytes(values))

    def set_light(self, on):
        self._send_cmd([0x51, 1 if on else 0])

    def set_horn(self, on):
        self._send_cmd([0x48, 1 if on else 0])

    def set_bell(self, on):
        self._send_cmd([0x47, 1 if on else 0])

    def set_bell_pitch(self, pitch):
        pitches = [0xFE, 0xFF, 0, 1, 2]
        if pitch < 0 or pitch >= len(pitches):
            raise "Bell pitch should be between 0 and " + pitch
        self._send_cmd([0x44, 0x02, 0x0E, pitches[pitch]])

    def speak(self):
        self._send_cmd([0x4D, 0, 0])

    def set_speed(self, speed):
        self._send_cmd([0x45, speed])

    def set_reverse(self, on):
        self._send_cmd([0x46, 0x02 if on else 0x01])

    def __del__(self):
        if self._adapter:
            self._adapter.stop()
