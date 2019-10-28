def makeVo(table_name, result):
    f = open("./{}.py".format(table_name+"Vo"), 'w')

    class_name = table_name[0].upper()
    class_name += table_name[1:]

    f.write("class {}:\n".format(class_name))
    f.write("    def __init__(self, result):\n")

    for i in range(len(result)):
        f.write("        self.{} = result[{}]\n".format(result[i][0], i))
    f.write("\n")

    for i in range(len(result)):
        f.write("    def get_{}(self):\n".format(result[i][0]))
        f.write("        return self.{}\n".format(result[i][0]))
        f.write("\n")
        f.write("    def set_{}(self, value):\n".format(result[i][0]))
        f.write("        self.{} = value\n".format(result[i][0]))
        f.write("\n")

    f.close()


