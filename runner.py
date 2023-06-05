from parsers.smb_info import SMBInfo

if __name__ == "__main__":
    smb_info = SMBInfo()
    print(smb_info.token)
    print(smb_info.locations_array)
    print(smb_info.start_urls)