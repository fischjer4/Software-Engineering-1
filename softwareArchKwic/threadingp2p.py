import threading

class messenger(threading.Thread):
    def run(self, **kwargs): #This is a very specific name that is special to threads. this is the 'main' for when a thread is used
        for x in xrange(10):
            if 'age' in kwargs and 'word' in kwargs and 'name' in kwargs:
                print(str(kwargs['age'])+ "  "+str(kwargs['word']) + "    "+str(kwargs['name']))
def ya(**kwargs):
    if 'age' in kwargs and 'word' in kwargs and 'name' in kwargs:
        print(str(kwargs['age'])+ "  "+str(kwargs['word']) + "    "+str(kwargs['name']))
def main():
    i = messenger()
    x = messenger()
    pi = threading.Thread(target=i.run, kwargs=({'age': 20, 'name': 'Jeremy is sending to Madelin', 'word': 'almost 21'}))
    px = threading.Thread(target=ya, kwargs=({'age': 20, 'name': 'Madelin is now reading Jeremy\'s message', 'word': 'Just turned!'}))

    pi.start() 
    px.start() 
main()
