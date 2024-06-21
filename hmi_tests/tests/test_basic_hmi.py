import time
import pytest
from test_resources.rtt_data import config
from test_lib.api import ValidationApi
from test_lib.constants import WarningStatus, TelltaleStatus, Buttons


class Test(ValidationApi):

    @pytest.fixture
    def before(self):
        self.setup_logger()
        self.get_url()
        self.icon_db_load()
        self.tpms_icon = config["rtt"]["tpms_icon"]
        self.w123 = "W123"
        self.w456 = "W456"
        yield
        self.press_btn(Buttons.Home.value)
        self.driver.close()

    def test_tpms_on(self, before):
        """
        This test method will verify whether the tire presure icon is ON in the cluster HMI screen
        when tire pressure button is pressed.
        """
        self.press_btn(Buttons.TIRE_PRESSURE.value)
        time.sleep(7)

        frame = self.capture_screen()
        self.verify_telltale_status(TelltaleStatus.ON.value, icon_data=self.tpms_icon, frame_data=frame)

    def test_active_park_warning(self, before):
        """
        This test method will verify whether the warning with id W123 is ON in the clusterHMI screen when
         drive mode button is pressed
        """
        self.press_btn(Buttons.DRIVER_MODE.value)
        time.sleep(4)
        frame = self.capture_screen()
        self.verify_warning_status(WarningStatus.ON.value, warning_id=self.w123, frame_data=frame)

    def test_fuel_economy(self, before):
        """
        This test method will verify whether the warning with id W456 is ON in the clusterHMI screen when
         Fuel Economy button is pressed
        """
        self.press_btn(Buttons.FUEL_ECONOMY.value)
        time.sleep(4)
        frame = self.capture_screen()
        self.verify_warning_status(WarningStatus.ON.value, warning_id=self.w456, frame_data=frame)