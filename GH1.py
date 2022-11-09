#import settings from the project
import os
#import path,Media_Root from settings
from django.conf.urls.static import static


urlpatterns=[
    url(r'^download/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT})]
    
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)




# APPLICTION VIEWSviews
def download(request,path):
    filepath=os.path.join(settings,MEDIA_ROOT,Path)
    if os.path.exists(filepath):
        with os.open(filepath,"rb") as fp:
            response=HttpResponse(fp.read(),content_type="img")
            response["content-disposition"]='inline;filename='+os.path.basename(filepath)
            return response 