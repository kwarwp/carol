
{'date': 'Mon Oct 08 2018 18:04:14.132 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 8
    Historia()
  module <module> line 6
    cenaSea = Cena(img = "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/The_deep_blue_sea_%286834127561%29.jpg/800px-The_deep_blue_sea_%286834127561%29.jpg")
TypeError: 'module' object is not callable
'''},