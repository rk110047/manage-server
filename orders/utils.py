import random
import string

def random_string_generator(size=10,char=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(char) for _ in range(size))


def unique_id_generator(instance):
    '''for unique order_id generation'''

    order_new_id        =   random_string_generator()
    klass           =   instance.__class__
    qs              =   klass.objects.filter(order_id=order_new_id).exists()

    return unique_id_generator(instance) if qs else order_new_id
