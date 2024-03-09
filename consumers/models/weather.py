"""Contains functionality related to Weather"""
import logging
import json

logger = logging.getLogger(__name__)


class Weather:
    """Defines the Weather model"""

    def __init__(self):
        """Creates the weather model"""
        self.temperature = 70.0
        self.status = "sunny"

    def process_message(self, message):
        """Handles incoming weather data"""
        logger.info("weather process_message is incomplete - skipping")
        #
        #
        # TODO: Process incoming weather messages. Set the temperature and status.
        #
        #
        weather_data = json.loads(message.value())
        try:
            self.temperature = weather_data['temperature']
            self.status = weather_data['status']
        except:
            logger.error("unable to find unpack message from topic %s", message.topic())