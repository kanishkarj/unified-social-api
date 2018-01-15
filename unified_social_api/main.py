from importlib import import_module
from .exceptions import NotFoundError


def get_object(service, keyword):
    '''Returns service object related to keyword

    Arguments:
    service - Will be in the form <social_media>.<entity>.
    keyword - Identifier of <entity>
    '''

    try:
        module = import_module('.{0}'.format(service), 'unified_social_api.social_medias')
    except ImportError:
        raise NotFoundError('Service "{0} not known"'.format(service))

    service, _, entity = service.partition('.')

    try:
        obj = getattr(module, entity)
    except AttributeError:
        err = 'Entity name "{0}" does not match the class name'
        raise NameError(err.format(entity))

    return obj(keyword)
