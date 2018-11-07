class BaseStrategy:
    
    stocks = []
    
    def initialize(self, context):
        context.stocks = self.stocks
     
    def handle_data(self, context, data):
        pass

    def _test_args(self):
        pass
    
    def analyze(self, context, perf):
        pass
