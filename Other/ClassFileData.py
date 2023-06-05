class FileData:
    name = []
    city = []

    def importDateFromFileName():
        list = []
        with open("NameList.txt", "r") as file:
            for line in file:
                line = str(str.splitlines(line))
                line =(line.replace("[", "").replace('"', "").replace("'", "").replace("]",""))
                list.append(line)
            file.close()
        return list
    
    def importDateFromFileCity():
        list = []
        with open("CityList.txt", "r") as file:
            for line in file:
                line = str(str.splitlines(line))
                line =(line.replace("[", "").replace('"', "").replace("'", "").replace("]",""))
                list.append(line)
            file.close()
        return list