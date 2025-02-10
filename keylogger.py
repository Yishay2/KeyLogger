import keyboard

class KeyLogger:

    def __init__(self):
        self.data = None
        self.path = "log.txt"
        self._listen = self.Listen()

    class Listen:

        def __init__(self):
            pass

        def _get_keyword(self):
            pass

        def _get_active_window(self):
            pass

        def _get_time(self):
            pass


    def _save_to_file(self):
        pass

    def _upload_to_server(self):
        pass

    def _encrypt(self):
        pass

    def exit(self):
        pass


keylogger = KeyLogger()
