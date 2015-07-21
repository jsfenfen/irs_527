from irs_configs import *
import requests, zipfile

DOWNLOAD_NEW_FILE = False


# http://stackoverflow.com/a/16696317
def download_file(url, file_path):
    local_filename = file_path + "/" + url.split('/')[-1]
    # NOTE the stream=True parameter
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                f.flush()
    return local_filename

def unzip_singlefile(this_zipfile, outfile):
    of = open(outfile, 'w')
    zf = zipfile.ZipFile(this_zipfile, 'r')
    filename = zf.namelist()[0]
    try:
        data = zf.read(filename)
        of.write(data)
    except KeyError:
        print 'ERROR: Did not find %s in zip file' % filename
    else:
        print filename, ':'
    print
    of.close()

if (DOWNLOAD_NEW_FILE):
    # retrieve the bulk files from IRS 
    result = download_file(IRS_FULL_FILE_LOCATION, DATA_LOCATION)
else:
    result = DATA_LOCATION + "/" + 'fullData'

print "file to unzip is %s" % (result)
unzip_singlefile(result, IRS_FILE_OUTPUT)

    
