from ImagePi.Plugin import Plugin, run_arguments

class testplugin1(Plugin):

  def run_thread(self, ndv, *args, *kwargs):
    self.ipy.log('sum:',ndv.arr.sum())
