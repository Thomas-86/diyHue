import logManager
import socket
from time import sleep
from zeroconf import IPVersion, ServiceBrowser, ServiceInfo, Zeroconf

logging = logManager.logger.get_logger(__name__)

def mdnsListener(ip, port, modelid, brigeid):
    logging.info('<MDNS> listener started')
    ip_version = IPVersion.V4Only
    zeroconf = Zeroconf(ip_version=ip_version)

    props = {
        'modelid':modelid,
        'bridgeid':brigeid
    }

    info = ServiceInfo(
        "_hue._tcp.local.",
        "DIYHue._hue._tcp.local.",
        addresses=[socket.inet_aton(ip)],
        port=port,
        properties=props,
        server="DIYHue.local."
    )
    zeroconf.register_service(info) 