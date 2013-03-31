"""
Copyright (c) 2013 Shotgun Software, Inc
----------------------------------------------------

Multi Publish

"""

import os
import tank
from tank import TankError

class MultiPublish(tank.platform.Application):

    def init_app(self):
        """
        Called as the application is being initialized
        """
        
        tk_multi_publish = self.import_module("tk_multi_publish")
        
        self._publish_handler = tk_multi_publish.PublishHandler(self)
        
        # register commands:
        display_name = self.get_setting("display_name")
        self.engine.register_command("%s..." % display_name, self._publish_handler.show_publish_dlg)
        
    def destroy_app(self):
        self.log_debug("Destroying tk-multi-publish")