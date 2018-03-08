    import os
    import time
    import shutil

    ## assuming source images are in .\alphabet

    src_dir = os.getcwd() + r".\\alphabet\\"
    msg_dir = os.getcwd() + r".\\message\\"

    # get the char each of the images represents
    def get_file_char_map():
        alpha = {}
        current_ascii = 97
        files = os.listdir( src_dir )
        # assuming files returned are in aplhabetical order
        for file in files:

            if current_ascii == 123:
                char_ascii = 46
            elif current_ascii == 124:
                char_ascii = 32
            else :
                char_ascii = current_ascii

            current_ascii = current_ascii + 1

            print str(char_ascii) + " " + chr(char_ascii) + " " + file
            alpha[chr(char_ascii)] = file
        return alpha


    # copy files accoring to map and message to display
    def copy_files_to_make_message(char_map, message):
        index = 0
        for char in message.lower():
            dst_file = "{:04d}.jpg".format(index)
            shutil.copyfile(src_dir + char_map[char], msg_dir + dst_file)
            # print src_dir + char_map[char] + " " + msg_dir + dst_file;
            index = index + 1


    char_map = get_file_char_map()
    copy_files_to_make_message(char_map, "If you can read this message my program works.")
