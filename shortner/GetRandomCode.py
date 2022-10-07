from random import choice
from string import ascii_letters, digits
from django.conf import settings

SIZE = getattr(settings, "MAX_URL_CHAR", 7)
AVAILABLE_CHARS = ascii_letters + digits

def get_random_code(chars=AVAILABLE_CHARS):
    return "".join( [choice(chars) for _ in range(SIZE)] )

def get_shortned_url(model_instance):
    random_code = get_random_code()

    model_class = model_instance.__class__

    if model_class.objects.filter(short_url=random_code).exists():
        return get_shortned_url(model_instance)

    return random_code