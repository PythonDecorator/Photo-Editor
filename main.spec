# -*- mode: python -*-
a = Analysis(['main.py'],
         pathex=['C:\\Users\\XPS\\Desktop\\Pro Portfolio\\Photo Editor'],
         datas=[('C:\\Users\\XPS\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\customtkinter', 'customtkinter/')],
         hiddenimports=[],
         hookspath=None,
         runtime_hooks=None)

for d in a.datas:
    if 'pyconfig' in d[0]:
        a.datas.remove(d)
        break

a.datas += [('files\\image\\logo.ico', 'C:\\Users\\XPS\\Desktop\\Pro Portfolio\\Photo Editor\\files\\image\\logo.ico', 'DATA')]
pyz = PYZ(a.pure)
exe = EXE(pyz,
      a.scripts,
      a.binaries,
      a.zipfiles,
      a.datas,
      name='PhotoEditor.exe',
      debug=False,
      strip=None,
      upx=True,
      console=False,
      icon='C:\\Users\\XPS\\Desktop\\Pro Portfolio\\Photo Editor\\files\\image\\logo.ico')
