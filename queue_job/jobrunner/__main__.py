import thrive

from .runner import QueueJobRunner


def main():
    thrive.tools.config.parse_config()
    runner = QueueJobRunner.from_environ_or_config()
    runner.run()


if __name__ == "__main__":
    main()
