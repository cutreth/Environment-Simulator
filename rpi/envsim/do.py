from models import Config


def getActiveConfig():
    active_config = Config.objects.filter()[:1].get()
    return active_config
