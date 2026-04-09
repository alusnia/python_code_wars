class Binding():
    def __init__(self, url, method, action):
        self.url = url
        self.method = {method: action}
        
    def mod(self, method, action):
        self.method[method] = action

class Router(object):
    def __init__(self):
        self.__urls = set()
        self.__bindings: list[Binding] = []
    
    def bind(self, url, method, action):
        if url in self.__urls:
            for binding in self.__bindings:
                if binding.url == url:
                    binding.mod(method, action)
                else:
                    continue
        else:
            binding = Binding(url, method, action)
            self.__urls.add(url)
            self.__bindings.append(binding)
            
    def runRequest(self, url, method):
        if url in self.__urls:
            for binding in self.__bindings:
                if binding.url == url:
                    return binding.method[method]()
        else:
            return 'Error 404: Not Found'
