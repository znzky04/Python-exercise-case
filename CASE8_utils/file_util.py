#File processing related tool modules

def print_file_info(file_name):
    """
    Output the contents of the file to the console
    :param file_name:The path of the file to be read
    :return:None
    """

    f = None
    try:
        f = open(file_name, "r", encoding="UTF-8")
        content = f.read()
        print("The document is as follows:")
        print(content)
    except Exception as e:
        print(f"warning:{e}")
    finally:
        if f:
            f.close()



def append_to_file(file_name,data):
    """
    Appends the specified data to the specified file
    :param file_name: File path
    :param data:data
    :return:None
    """
    f = open(file_name,"a", encoding="UTF-8")
    f.write(data)
    f.write("\n")
    f.close()




if __name__ == '__main__':
    #print_file_info("")
    append_to_file()
