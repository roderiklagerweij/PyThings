__author__ = 'Roderik'
import os
import pyrax

class FileUploader:
    def __init__(self):
        self.cf = None
        self.container = None

    def connect_container(self, container):
        print ('Connecting to container', container)
        pyrax.set_setting("identity_type", "rackspace")
        creds_file = os.path.expanduser("~/.rackspace_cloud_credentials")
        pyrax.set_credential_file(creds_file)
        self.cf = pyrax.cloudfiles
        self.container = self.cf.get_container(container)
        print ('Successfully connected to container')

    def upload_file(self, basepath, filename):
        f = open(basepath + '/' + filename, 'rw')
        content = f.read()
        f.close()
        print ('Uploading:', filename,)
        self.cf.store_object(self.container, filename, content)
        print ('Done')

    def upload_folder(self, folder):
        self.cf.upload_folder(folder, container=self.container)

uploader = FileUploader()
uploader.connect_container("PyThings")

print ('Uploading files')
uploader.upload_folder('images')
