import ssl
from urllib.request import Request, urlopen

from timer import Timer


def worker():
    myssl = ssl.create_default_context()
    myssl.check_hostname = False
    myssl.verify_mode = ssl.CERT_NONE

    with Timer() as t:

        import pdb
        pdb.set_trace()

        print('hint: l / n / s / c')

        req = Request('https://tutorialedge.net',
                      headers={'User-Agent': 'Mozilla/5.0'})
        response = urlopen(req, context=myssl)

    print('hint: print(response.status)')

    print("Elapsed Time: {} seconds".format(t.elapsed))


worker()
