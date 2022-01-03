import bottle
import cipher

@bottle.route("/encrypt")
def encrypt():
    return bottle.static_file("/encrypt.html",root = "")

@bottle.route("/decrypt")
def decrypt():
    return bottle.static_file("/decrypt.html", root = "")


@bottle.post("/encrypt")
def encrypt():
    plaintext = bottle.request.forms.get("plaintext")
    key = bottle.request.forms.get("key")
    ciphertext = cipher.start("encipher", key, plaintext)
    info = {"plaintext": plaintext,
            "ciphertext": ciphertext}
    return bottle.template("encrypted.tpl", info)

@bottle.post("/decrypt")
def decrypt():
    ciphertext = bottle.request.forms.get("ciphertext")
    key = bottle.request.forms.get("key")
    plaintext = cipher.start("decipher", key, "", ciphertext)
    info = {"plaintext": plaintext,
            "ciphertext": ciphertext}
    return bottle.template("decrypted.tpl", info)



@bottle.get("/static/<filename>")
def getStaticFile(filename):
    return bottle.static_file(filename, root = "")

@bottle.get("/dynamic/<filename>")
def getDynamicFile(filename):
    info = {}
    return bottle.template(filename, info)


@bottle.post("/static/<filename>")
def getStaticFile(filename):
    return bottle.static_file(filename, root = "")
    


@bottle.route("/")
def init():
    return bottle.static_file("index.html", root = "")

    
bottle.run(bottle.app(), port=8080, debug= True, reloader=True)
init()
