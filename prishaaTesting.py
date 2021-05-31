

import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.Ax63aOKTHo1nJFj0CQJOCIGkssrURtzlXtd_luYR3ofkEr8o8Wr3YFnP9vXYdOmaajrVSdk2rdv9iY4RGtk5YkNbkwGcTbPyvDmLIBefDiMldnz9hENmETWQkq0H65T8TtMwiNjwMBE'
    transferData = TransferData(access_token)
    fileName = input("enter file name:")
    e = '/test dropbox/'
    file_from = fileName
    file_to = e+fileName  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()