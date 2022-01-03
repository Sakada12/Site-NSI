import bottle

@bottle.route("/")
def init():
    return bottle.static_file("index.html", root = "")
@bottle.get("/static/<filename>")
def getStaticFile(filename):
    return bottle.static_file(filename, root = "")
@bottle.post("/static/<filename>")
def getStaticFile(filename):
    return bottle.static_file(filename, root = "")


    
bottle.run(bottle.app(), port=8080, debug= True, reloader=True)
