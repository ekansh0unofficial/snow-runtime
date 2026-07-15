class DoctorApplication:
    def __init__(self, session_service, config_service, secret_service):
        self.session_service = session_service
        self.config_service = config_service
        self.secret_service = secret_service

    def health_check(self):
        pass

    def check_connection(self) -> bool:
        pass

    def check_config(self):
        pass
