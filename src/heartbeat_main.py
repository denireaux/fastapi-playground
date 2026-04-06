import os
import time
import logging
from itertools import count

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger(__name__)

def main():
    heartbeat_limit = int(os.getenv("HEARTBEAT_LIMIT", 100))
    
    log.info(f"Heartbeat service started. Limit: {heartbeat_limit} cycles.")

    try:
        for i in count(1):
            if i <= heartbeat_limit:
                log.info(f"Heartbeat {i}/{heartbeat_limit} - System Active")
                time.sleep(5)
            else:
                log.info("Reached heartbeat limit. Shutting down service.")
                break
    except KeyboardInterrupt:
        log.info("External shutdown signal received.")

    log.info("Service execution finished.")

if __name__ == "__main__":
    main()
