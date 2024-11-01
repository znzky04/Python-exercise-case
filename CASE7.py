#Case7:Read write and manipulate documents

fr = open("G:\\AIvoice\\pythonPractice\\CASE7example.txt", "r", encoding="UTF-8")
fw = open("G:\\AIvoice\\pythonPractice\\CASE7example.txt.bak", "w", encoding="UTF-8")


for line in fr:
    line = line.strip()

    fields = line.split(",")

    if fields[-1] == "ppp":
        fw.write(line + "\n")

fw.write("Rimi,3-23,Bass,ppp \n")
fw.write("OTae,12-4,guitar,ppp \n")

fr.close()
fw.close()