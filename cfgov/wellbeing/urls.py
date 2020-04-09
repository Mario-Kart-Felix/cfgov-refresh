from django.conf.urls import url

from core.views import TranslatedTemplateView
from wellbeing.views import ResultsView


try:
    from django.urls import re_path
except ImportError:
    from django.conf.urls import url as re_path


urlpatterns = [
    url(
        r'^$',
        TranslatedTemplateView.as_view(
            template_name='wellbeing/home.html'
        ),
        name='fwb_home_en'
    ),
    url(
        r'^results/$',
        ResultsView.as_view(),
        name='fwb_results_en'
    ),
    url(
        r'^about/$',
        TranslatedTemplateView.as_view(
            template_name='wellbeing/about.html'
        ),
        name='fwb_about_en'
    ),
    url(
        r'^error/$',
        TranslatedTemplateView.as_view(
            template_name='wellbeing/error.html'
        ),
        name='fwb_error_en'
    ),

    url(
        r'^es/$',
        TranslatedTemplateView.as_view(
            template_name='wellbeing/home.html',
            language='es'
        ),
        name='fwb_home_es'
    ),
    url(
        r'^results/es/$',
        ResultsView.as_view(language='es'),
        name='fwb_results_es'
    ),
    url(
        r'^about/es/$',
        TranslatedTemplateView.as_view(
            template_name='wellbeing/about.html',
            language='es'
        ),
        name='fwb_about_es'
    ),
    url(
        r'^error/es/$',
        TranslatedTemplateView.as_view(
            template_name='wellbeing/error.html',
            language='es'
        ),
        name='fwb_error_es'
    ),
]
