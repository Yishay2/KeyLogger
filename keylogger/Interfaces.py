from abc import ABC, abstractmethod

class IKeyLogger(ABC):

    @abstractmethod
    def start_logging(self) -> None:
        pass

    @abstractmethod
    def stop_logging(self) -> None:
        pass

    @abstractmethod
    def get_logged_keys(self) -> dict:
        pass


class IWriter:
    @abstractmethod
    def send_data(self, data: dict, machine_name: str):
        pass
