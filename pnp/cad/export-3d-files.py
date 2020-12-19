#
# Exports 3D printing files to STL
#

FREECADPATH = '/usr/lib/freecad/lib/'
import sys
sys.path.append(FREECADPATH)
import FreeCAD
import MeshPart

assembly = FreeCAD.open("assembly.FCStd")

for obj in assembly.Objects:
    if ("b_FDM" in obj.Name):
        shape = obj.Shape.copy(False)
        shape.Placement = obj.getGlobalPlacement()
        mesh = assembly.addObject("Mesh::Feature", "Mesh")
        mesh.Mesh=MeshPart.meshFromShape(Shape=shape, LinearDeflection=0.01, AngularDeflection=0.025, Relative=False)
        mesh.Label=obj.Name
        mesh.Mesh.write("3D-Prints/" + obj.Name.split("_00")[2][1:].split("_Body")[0] + ".stl")

FreeCAD.closeDocument(assembly.Name)