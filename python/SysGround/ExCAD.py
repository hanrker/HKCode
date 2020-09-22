import dxfgrabber
import os.path


workpath = "./SysGround"
filePath = "/DXF/test-dxf.dxf"
def ReadDXF(file):
    isFile = os.path.isfile(file)
    
    if(isFile):
        print("The Path is :"+file)
        dxf = dxfgrabber.readfile(file)
        for layer in dxf.layers:
            print(layer.name,layer.color,layer.linetype)

        for e in dxf.entities:
            print(e.dxftype,e.layer)
            if e.dxftype == 'LINE':
                print (e.start,e.end)
            if e.dxftype == 'CIRCLE':
                print (e.center,e.radius)
            if e.dxftype == 'ARC':
                print (e.center,e.radius,e.start_angle,e.end_angle)
    else:
        print("No File")

ReadDXF(workpath + filePath)
file = input("input:")
ReadDXF(file)