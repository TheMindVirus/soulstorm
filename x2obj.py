class descriptor:
    def __init__(self):
        self.line = 0
        self.name = ""
        self.v_A = 0
        self.v_B = 0
        self.f_A = 0
        self.f_B = 0
        self.vn_A = 0
        self.vn_B = 0
        self.vt_A = 0
        self.vt_B = 0

    def get(self):
        info = ""
        info += "Line: " + str(self.line) + "\n"
        info += "Name: " + str(self.name) + "\n"
        info += " v_A: " + str(self.v_A) + "\n"
        info += " v_B: " + str(self.v_B) + "\n"
        info += " f_A: " + str(self.f_A) + "\n"
        info += " f_B: " + str(self.f_B) + "\n"
        info += "vn_A: " + str(self.vn_A) + "\n"
        info += "vn_B: " + str(self.vn_B) + "\n"
        info += "vt_A: " + str(self.vt_A) + "\n"
        info += "vt_B: " + str(self.vt_B) + "\n"
        return info

def decode(data):
    lines = data.split("\n")

    descriptors = []
    for i in range(0, len(lines)):
        if "  Mesh " in lines[i]:
            terminator = lines[i].find("\x00")
            desc = descriptor()
            
            desc.line = i
            desc.name = lines[i][8:terminator]
            
            desc.v_A = i + 2
            desc.v_B = desc.v_A + int(lines[desc.v_A - 1].replace(";", ""))
            desc.f_A = desc.v_B + 1
            desc.f_B = desc.f_A + int(lines[desc.f_A - 1].replace(";", ""))
            
            desc.vn_A = desc.f_B + 2
            desc.vn_B = desc.vn_A + int(lines[desc.vn_A - 1].replace(";", ""))
            desc.vt_A = desc.vn_B + int(lines[desc.vn_B].replace(";", "")) + 4
            desc.vt_B = desc.vt_A + int(lines[desc.vt_A - 1].replace(";", ""))
            
            descriptors.append(desc)
            #print(desc.get())
            #print(lines[desc.vt_A:desc.vt_B])
            #break

    for desc in descriptors:
        vertdata = lines[desc.v_A:desc.v_B]
        texdata = lines[desc.vt_A:desc.vt_B]
        normdata = lines[desc.vn_A:desc.vn_B]
        facedata = lines[desc.f_A:desc.f_B]

        vertices = []
        texcoords = []
        normals = []
        faces = []

        for line in vertdata:
            vertices.append(line.split(";")[:3])
            idx = len(vertices) - 1
            for i in range(0, 3):
                vertices[idx][i] = "{:.6f}".format(float(vertices[idx][i]))

        for line in texdata:
            texcoords.append(line.split(";")[:2])
            idx = len(texcoords) - 1
            for i in range(0, 2):
                texcoords[idx][i] = "{:.6f}".format(float(texcoords[idx][i]))

        for line in normdata:
            break
            normals.append(line.split(";")[:2])
            idx = len(normals) - 1
            for i in range(0, 2):
                normals[idx][i] = "{:.4f}".format(float(normals[idx][i]))

        for line in facedata:
            faces.append(line.split(";")[1].split(","))
            idx = len(faces) - 1
            for i in range(0, 3):
                faces[idx][i] = "{}".format(int(faces[idx][i]) + 1)

        newdata = "# x2obj.py - Python-Based DirectX to WaveFront OBJ Generator\n"

        for v in vertices:
            newdata += "v " + str(v[0]) + " " + str(v[1]) + " " + str(v[2]) + "\n"

        for vt in texcoords:
            newdata += "vt " + str(vt[0]) + " " + str(vt[1]) + "\n"

        for vn in normals:
            newdata += "vn " + str(vn[0]) + " " + str(vn[1]) + "\n"

        for f in faces:
            newdata += "f " + str(f[0]) + " " + str(f[1]) + " " + str(f[2]) + "\n"

        file = open("./output/" + str(desc.name) + ".obj", "w")
        file.write(newdata)
        file.close()
