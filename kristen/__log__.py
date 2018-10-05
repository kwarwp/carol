
{'date': 'Fri Oct 05 2018 11:20:08.949 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 9
    Historia()    
  module <module> line 7
    DESERTO = Cena(img = "https://cdn.pixabay.com/photo/2016/09/08/13/58/desert-1654439_960_720.jpg")
TypeError: 'module' object is not callable
'''},