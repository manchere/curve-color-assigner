import maya.cmds as cmds

def setRGBColor(ctrl, color=(1, 0, 1)):
    rgb = ("R", "G", "B")

    cmds.setAttr(ctrl + ".overrideEnabled", 1)
    cmds.setAttr(ctrl + ".overrideRGBColors", 1)

    for channel, color in zip(rgb, color):
        cmds.setAttr(ctrl + ".overrideColor%s" % channel, color)


def assignColor(colore = []):
    for i in cmds.ls(sl=True):
        setRGBColor(i, colore)


def colorChange():
    if cmds.colorEditor(query=False, result=True):
        values = cmds.colorEditor(query=True, rgb=True)
        assignColor(values)


if cmds.window('color_curve', exists=True):
    cmds.deleteUI('color_curve')

cmds.window('color_curve', title='Curve Color Assign', w=150)
cmds.columnLayout(adjustableColumn=True)

cmds.frameLayout(label='Select a color', cll=False, bgc=[0.7, 0, 0.3], w=200)

btn = cmds.button('Assign', c='colorChange()')

cmds.showWindow()