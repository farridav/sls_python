from ..common.utils import do_thing


def lambda_handler(event, context):
    print('into handler one')
    do_thing()
