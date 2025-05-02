import os, sys
import json
# from PDFWriter import PDFWriter
from xhtml2pdf import pisa
from io import StringIO
from django.template.loader import get_template
from django.template import Context
import argparse
from weasyprint import HTML, CSS
import random
from django.conf import settings
import time
from time import sleep
from django.http import JsonResponse, HttpResponse

# path = '/home/rahul/pdf/'
from online_exam.models import TestStudentResponse
from online_exam.pdf_to_img import pdf_to_jpg_convertor
from user_management.config import pdf_gen_host
from pyvirtualdisplay import Display
import pdfkit


def usingPDFkit(assigned_id):
    try:

        display=Display().start()
        assign_code = random.randint(1000, 9999)
        path = settings.MEDIA_ROOT + 'assign_pdf/'

        options = {'page-size': 'A4', 'margin-top': '0.75in', 'margin-right': '0.75in', 'margin-bottom': '0.75in',
                   'margin-left': '0.75in', 'javascript-delay': '40000'}
        # html_file_name, html_file_extension = os.path.splitext(html_file_path)

        pdf_file = pdfkit.from_url(pdf_gen_host + 'onlineexam/oe/resultpdf/?assigned_id=' + str(assigned_id),
                                   path + str(assigned_id) + '.pdf', options=options)

    except Exception as e:
        pass
        # print(e,'e printing........')
    finally:
        display.stop()

    # http_protocol = 'http://'
    # if request.is_secure():
    #       http_protocol = 'https://'
    # host=http_protocol+request.META['HTTP_HOST']
    pdf_path = 'media/assign_pdf/' + str(assigned_id) + '.pdf'
    zip_file_geting = pdf_to_jpg_convertor(str(assigned_id), pdf_path)

    return zip_file_geting
