from home.views import HeaderCustomisation


def header_customisation_processor(request):
    return {
       'header_customisation': HeaderCustomisation.objects.all(),
    }
