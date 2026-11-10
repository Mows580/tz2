from aiomisc import entrypoint

from src.bootstrap.app import AppService
from src.config import ApplicationConfig

def main() -> None:
    config = ApplicationConfig()
    service = AppService(config=config)

    with entrypoint(service) as loop:
        loop.run_forever()

if __name__ == "__main__":
    main()