include("$(PORT_DIR)/boards/manifest.py")
freeze("modules")
freeze_as_mpy("dtn7zero_modules", "abc.py")
freeze_as_mpy("dtn7zero_modules", "cbor.py")
freeze_as_mpy("dtn7zero_modules", "__future__.py")
freeze_as_mpy("dtn7zero_modules", "typing.py")
freeze_as_mpy("dtn7zero_modules", "wlan.py")
package("py_dtn7", base_path="dtn7zero_modules")
package("dtn7zero", base_path="dtn7zero_modules")
package("sx127x", base_path="dtn7zero_modules")
require("ssd1306")
